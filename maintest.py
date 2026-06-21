
# Start the server
if __name__ == "__main__":
    # KEY CHANGE: Use HTTP transport for remote access
    # Note: Depending on your FastMCP version, you may need transport="sse" instead of "http"
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
