#!/usr/bin/env python3
import asyncio
import json
import subprocess
import sys

async def test_mcp():
    # 启动服务器
    proc = await asyncio.create_subprocess_exec(
        sys.executable,
        "main.py",
        "--agent", "get_current_time",
        "--runtime", "local",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    print("服务器启动中...")
    await asyncio.sleep(2)
    
    # 发送初始化请求
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "clientInfo": {"name": "test-client", "version": "1.0"}
        }
    }
    
    print(f"发送初始化请求...")
    proc.stdin.write((json.dumps(init_request) + "\n").encode())
    await proc.stdin.drain()
    
    # 读取响应
    response_line = await asyncio.wait_for(proc.stdout.readline(), timeout=10)
    print(f"收到响应: {response_line.decode().strip()}")
    
    # 发送list_tools请求
    list_request = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {}
    }
    
    print(f"发送list_tools请求...")
    proc.stdin.write((json.dumps(list_request) + "\n").encode())
    await proc.stdin.drain()
    
    # 读取响应
    response_line = await asyncio.wait_for(proc.stdout.readline(), timeout=10)
    response = json.loads(response_line.decode())
    
    print(f"\n✅ 成功获取工具列表:")
    if "result" in response and "tools" in response["result"]:
        tools = response["result"]["tools"]
        for tool in tools:
            print(f"  - {tool['name']}: {tool['description']}")
        print(f"\n总计: {len(tools)} 个工具")
        return True
    else:
        print(f"❌ 响应格式错误: {response}")
        return False
    
    # 清理
    proc.terminate()
    await proc.wait()

if __name__ == "__main__":
    asyncio.run(test_mcp())