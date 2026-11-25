# Connect a Local MCP Server to Cursor

This guide explains how to connect a locally running **Model Context
Protocol (MCP)** server to the Cursor editor.

## 1. Choose where to store the configuration

Cursor supports both project-specific and global MCP configuration.

  -----------------------------------------------------------------------------------
  Configuration           File location                       When to use it
  ----------------------- ----------------------------------- -----------------------
  Project-specific        `<project-root>/.cursor/mcp.json`   The server should be
                                                              available only in one
                                                              project

  Global                  `~/.cursor/mcp.json`                The server should be
                                                              available across your
                                                              Cursor projects
  -----------------------------------------------------------------------------------

On Windows, the global path is typically:

``` text
%USERPROFILE%\.cursor\mcp.json
```

For a project-specific setup, create a `.cursor` directory in your
project root if it does not already exist, then create `mcp.json` inside
it.

> **Important:** Cursor uses `.cursor/mcp.json` and the `mcpServers`
> root key. Do not copy a VS Code configuration unchanged: VS Code
> commonly uses `.vscode/mcp.json` and a `servers` root key.

## 2. Add your MCP server configuration

The configuration tells Cursor how to launch your local MCP server.

### Python MCP server

Example for Windows:

``` json
{
  "mcpServers": {
    "my-python-mcp": {
      "command": "C:\\path\\to\\project\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\project\\server.py"
      ],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

Example for macOS or Linux:

``` json
{
  "mcpServers": {
    "my-python-mcp": {
      "command": "/absolute/path/to/project/.venv/bin/python",
      "args": [
        "/absolute/path/to/project/server.py"
      ]
    }
  }
}
```

Replace the example paths and environment variables with the values for
your project. If your server does not need an API key, remove the `env`
section.

### Node.js MCP server

``` json
{
  "mcpServers": {
    "my-node-mcp": {
      "command": "node",
      "args": [
        "/absolute/path/to/project/dist/index.js"
      ],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

Use the actual path to your compiled JavaScript entry point. If Node.js
is not available on Cursor's PATH, use the absolute path to the Node
executable.

## 3. Connect through Cursor Settings

You can also open the configuration file from Cursor:

1.  Open Cursor.
2.  Open **Settings** (`Ctrl + ,` on Windows/Linux or `Cmd + ,` on
    macOS).
3.  Find **Tools & Integrations** or the **MCP** section (the label can
    vary by Cursor version).
4.  Choose the option to add or open an MCP server configuration.
5.  Add your server entry to the appropriate `mcp.json` file and save
    it.

## 4. Verify the connection

1.  Return to Cursor's MCP settings.
2.  Find your server in the configured server list.
3.  Check whether Cursor reports it as connected and displays its tools.
4.  If it does not connect, use the refresh or reconnect control if
    available.
5.  Open Cursor's **Output** panel and select the Cursor/MCP log channel
    to inspect startup errors. The exact channel label can vary by
    version.

Once connected, open Cursor Chat and use **Agent** mode to ask Cursor to
use one of the MCP tools. Tool availability can depend on the selected
mode and Cursor version.

## 5. Troubleshooting

### The server does not appear

-   Confirm the file is named `mcp.json`.
-   For a project-level setup, confirm the path is exactly
    `.cursor/mcp.json` under the workspace root.
-   Confirm the top-level JSON key is `mcpServers`, not `servers`.
-   Save the file, then refresh the MCP server list or restart Cursor.

### The server fails to start

-   Use absolute paths for the Python/Node executable and server entry
    point.
-   Confirm the executable and script exist.
-   Run the same command and arguments manually in a terminal to check
    for startup errors.
-   Confirm required packages are installed in the environment used by
    Cursor.
-   Check that environment variables are present and correctly named.

### The server starts but no tools appear

-   Confirm the server registers tools correctly.
-   Check the MCP logs for initialization or protocol errors.
-   For a `stdio` server, keep standard output (`stdout`) reserved for
    MCP protocol messages. Send diagnostic logs to standard error
    (`stderr`) instead; extra text on `stdout` can break the connection.

### VS Code configuration is not working in Cursor

Cursor does not automatically use `.vscode/mcp.json` as its project MCP
configuration. Create or move the Cursor configuration to
`.cursor/mcp.json`, and change the root key to `mcpServers` where
necessary.

## 6. Example: two local Python MCP servers

You can define multiple servers in the same `mcpServers` object:

``` json
{
  "mcpServers": {
    "calculator-stdio": {
      "command": "C:\\path\\to\\project\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\project\\mcp\\calculator_stdio.py"
      ]
    },
    "calculator-http": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8002/mcp"
      ]
    }
  }
}
```

This is an illustrative configuration. Make sure the paths, command, and
HTTP endpoint match your actual setup. The HTTP example uses
`mcp-remote` to connect to an MCP server exposed at the specified local
endpoint.

## Further reading

-   [Cursor MCP documentation](https://cursor.com/docs/mcp)
-   [Model Context Protocol
    documentation](https://modelcontextprotocol.io/)

------------------------------------------------------------------------

**Quick checklist**

-   [ ] The configuration is in the correct `mcp.json` location.
-   [ ] The top-level key is `mcpServers`.
-   [ ] Commands and script paths are valid.
-   [ ] Required environment variables are configured.
-   [ ] Cursor shows the server as connected and lists its tools.
-   [ ] The tools are available in Cursor Agent mode.
