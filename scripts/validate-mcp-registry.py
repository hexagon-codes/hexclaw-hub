#!/usr/bin/env python3
"""mcp-registry.json 契约校验（测试闭环）。

数据连接器走 MCP（架构决策：MCP = 唯一数据底座）。registry 是 MCP server 一键装的单源，
但凭证注入契约（env / 连接串 arg / flag）各包各异，历史上多处写错（redis 写成 env、mongodb
变量名错、sqlite 指向已下架 npm 包、mysql env 名错）。本脚本把已核对的契约钉死，防回归。

运行：  python3 scripts/validate-mcp-registry.py
退出码：0 全绿；1 有契约违例（打印每条 FAIL）。
也可在 pytest 下运行：  pytest scripts/validate-mcp-registry.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "mcp-registry.json")

# 与后端 hexclaw api/handler_misc.go 对齐。
ALLOWED_COMMANDS = {"npx", "node", "uvx", "uv", "python", "python3", "docker", "deno", "bun", "go", "cargo"}
# args 危险字符（后端 mcpDangerousArgChars：放行 `~`，其余 shell 元字符/控制字符仍禁）。
DANGEROUS_ARG_CHARS = set("`$|;&><(){}!\\'\"\n\r\x00")
# command 危险字符（后端 mcpDangerousChars：含 `~`）。
DANGEROUS_CMD_CHARS = DANGEROUS_ARG_CHARS | {"~"}


def load():
    with open(REGISTRY, encoding="utf-8") as f:
        return json.load(f)


def server(reg, name):
    for s in reg["servers"]:
        if s.get("name") == name:
            return s
    raise AssertionError(f"registry 缺少 server: {name}")


def test_structure():
    reg = load()
    assert isinstance(reg, dict) and reg.get("version"), "缺少顶层 version"
    assert isinstance(reg.get("servers"), list) and reg["servers"], "servers 必须为非空数组"


def test_every_server_valid_shape():
    reg = load()
    seen = set()
    for s in reg["servers"]:
        name = s.get("name")
        assert name, f"server 缺 name: {s}"
        assert name not in seen, f"重复 server 名: {name}"
        seen.add(name)
        cmd = s.get("command", "")
        assert cmd in ALLOWED_COMMANDS, f"{name}: 命令 {cmd!r} 不在白名单（后端会拒）"
        assert not (set(cmd) & DANGEROUS_CMD_CHARS), f"{name}: command 含危险字符"
        args = s.get("args", [])
        assert isinstance(args, list), f"{name}: args 必须为数组"
        for a in args:
            assert isinstance(a, str), f"{name}: arg 非字符串: {a!r}"
            bad = set(a) & DANGEROUS_ARG_CHARS
            assert not bad, f"{name}: arg {a!r} 含后端会拒的危险字符 {bad}"
        env = s.get("env")
        if env is not None:
            assert isinstance(env, dict), f"{name}: env 必须为对象"


def test_no_dead_sqlite_npm_package():
    """官方 @modelcontextprotocol/server-sqlite npm 包已下架（404）——任何 server 都不得再 pin。"""
    reg = load()
    for s in reg["servers"]:
        joined = " ".join(s.get("args", []))
        assert "@modelcontextprotocol/server-sqlite" not in joined, (
            f"{s['name']}: 引用了已下架的 npm 包 @modelcontextprotocol/server-sqlite，应改用 PyPI uvx mcp-server-sqlite"
        )


def test_mysql_env_contract():
    s = server(load(), "mysql")
    env = s.get("env", {})
    for k in ("MYSQL_HOST", "MYSQL_PORT", "MYSQL_USER", "MYSQL_PASS", "MYSQL_DB"):
        assert k in env, f"mysql env 缺 {k}（@benborla29 包用 MYSQL_PASS/MYSQL_DB/MYSQL_PORT）"
    assert "MYSQL_PASSWORD" not in env and "MYSQL_DATABASE" not in env, (
        "mysql 不应使用 MYSQL_PASSWORD/MYSQL_DATABASE（该包真名是 MYSQL_PASS/MYSQL_DB）"
    )


def test_redis_url_is_arg_not_env():
    s = server(load(), "redis")
    assert "REDIS_URL" not in (s.get("env") or {}), "redis 不读 REDIS_URL 环境变量（README: URL as argument）"
    assert any(a.startswith("redis://") for a in s.get("args", [])), "redis 连接 URL 必须作为命令行 arg"


def test_mongodb_env_var_name():
    s = server(load(), "mongodb")
    env = s.get("env", {})
    assert "MDB_MCP_CONNECTION_STRING" in env, "mongodb 官方包读 MDB_MCP_CONNECTION_STRING"
    assert "MONGODB_URI" not in env, "mongodb 不读 MONGODB_URI"


def test_sqlite_uses_uvx():
    s = server(load(), "sqlite")
    assert s.get("command") == "uvx", "sqlite 官方为 PyPI 包，命令应为 uvx"
    args = s.get("args", [])
    assert "mcp-server-sqlite" in args and "--db-path" in args, "sqlite 应为 uvx mcp-server-sqlite --db-path <path>"


def test_postgres_url_is_arg():
    s = server(load(), "postgres")
    assert not (s.get("env") or {}), "postgres 官方 server 无 env 入口"
    assert any(a.startswith("postgresql://") for a in s.get("args", [])), "postgres 连接串必须作为命令行 arg"


def _all_tests():
    return [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]


if __name__ == "__main__":
    failures = 0
    for fn in _all_tests():
        try:
            fn()
            print(f"  PASS  {fn.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"  FAIL  {fn.__name__}: {e}")
    total = len(_all_tests())
    print(f"\n{total - failures}/{total} passed")
    sys.exit(1 if failures else 0)
