import contextlib

from fastapi import FastAPI
from mcp.server.mcpserver import MCPServer

# Initialize official MCP server
mcp = MCPServer("Calculator MCP")


# Register calculator tools
@mcp.tool()
def multiply_numbers(a: float, b: float) -> dict:
    """Multiply two numbers."""
    return {"result": a * b}


@mcp.tool()
def add_numbers(a: float, b: float) -> dict:
    """Add two numbers."""
    return {"result": a + b}


@mcp.tool()
def subtract_numbers(a: float, b: float) -> dict:
    """Subtract two numbers."""
    return {"result": a - b}


@mcp.tool()
def divide_numbers(a: float, b: float) -> dict:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    return {"result": a / b}


# Create MCP ASGI application
mcp_app = mcp.streamable_http_app()


# Manage MCP session lifecycle
@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with mcp.session_manager.run():
        yield


# Initialize FastAPI
app = FastAPI(
    title="Calculator API",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok"}


# Mount MCP application AFTER FastAPI routes
app.mount("/", mcp_app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8002)


# python fastapi-official_mcp_calculator.py

# npx @modelcontextprotocol/inspector http://127.0.0.1:8002/mcp
