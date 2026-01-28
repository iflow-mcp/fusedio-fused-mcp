from setuptools import setup, find_packages

setup(
    name="iflow-mcp_fusedio_fused-mcp",
    version="0.1.1",
    description="Fused MCP: Setting up MCP Servers for Data Scientists",
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.49.0",
        "fused[all]>=1.15.0",
        "jupyterlab>=4.3.6",
        "mcp[cli]>=1.4.1",
        "python-dotenv>=1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "iflow-mcp-fusedio-fused-mcp=main:main",
        ],
    },
    package_data={
        "udfs": ["*/*.py", "*/*.txt", "*/*.md", "*/*.json"],
    },
    include_package_data=True,
)