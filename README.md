# Todoist MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Model Context Protocol (MCP) server for interacting with Todoist's API, providing a structured way to manage your Todoist tasks, projects, sections, and labels programmatically. Just use natural langguage while talking to your AI Agent and it will hit the MCP server and do the tasks for you. 

## Features

- **Task Management**: Create, read, update, and delete tasks
- **Project Organization**: Manage projects and their hierarchy
- **Sections**: Organize tasks within projects using sections
- **Labels**: Create and manage task labels
- **Due Dates**: Set and manage due dates with natural language processing
- Uses Python MCP SDK for MCP Server and integrates Todoist SDK for all the above tasks.

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management
- Todoist API token (get it from [Todoist Integrations](https://todoist.com/app/settings/integrations))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/trickster026/todoist-mcp.git
   cd todoist-mcp
   ```


2. Install development dependencies:
   ```bash
   uv sync
   ```

## Configuration

### Windsurf
Go to `/home/<user>/.codeium/windsurf/mcp_config.json` and add the following:

```json
{
    "mcpServers": {
        "todoist-mcp": {
            "command": "/ABSOLUTE/PATH/TO/PARENT/FOLDER/uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER",
                "run",
                "server.py"
            ]
            "env": {
                "TODOIST_API_TOKEN": "your_api_token_here"
            }
        }
    }
}
```

### Example
```json
{
    "mcpServers": {
        "todoist-mcp": {
            "command": "uv",
            "args": [
                "--directory",
                "/home/trickster026/todoist-mcp/src/",
                "run",
                "server.py"
            ],
            "env": {
                "TODOIST_API_TOKEN": "your_api_token_here"
            }
        }
    }
}
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Todoist API](https://developer.todoist.com/rest/v2/)
- [uv](https://github.com/astral-sh/uv)

## Future Work
- Refactor Code
- Documentation Enhancements - Add more examples and better documentation.
- Add steps for other AI Agents Setup