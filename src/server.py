import logging
from typing import Optional
from mcp.server.fastmcp import FastMCP

from todoist_client import TodoistClient


mcp = FastMCP("Todoist MCP", dependencies=["todoist-api-python"])

# Service Initialization
todoist_client = TodoistClient()


@mcp.tool()
async def get_tasks(project_id: Optional[str] = None):
    tasks = await todoist_client.get_tasks(project_id=project_id)
    logging.info(tasks)
    return tasks


def main():
    mcp.run()


if __name__ == "__main__":
    main()
