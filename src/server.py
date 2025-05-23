import logging
from typing import Optional, List
from mcp.server.fastmcp import FastMCP
from todoist_client import TodoistClient


mcp = FastMCP("Todoist MCP", dependencies=["todoist-api-python"])

# Service Initialization
todoist_client = TodoistClient()


@mcp.tool()
async def get_tasks(
    project_id: Optional[str] = None,
    section_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    label: Optional[str] = None,
    ids: Optional[List[str]] = None,
    limit: Optional[int] = None,
):

    tasks = await todoist_client.get_tasks(
        project_id=project_id,
        section_id=section_id,
        parent_id=parent_id,
        label=label,
        ids=ids,
        limit=limit,
    )
    logging.info(tasks)
    return tasks


@mcp.tool()
async def add_task(
    content: str,
    description: Optional[str] = None,
    project_id: Optional[str] = None,
    section_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    labels: Optional[List[str]] = None,
    priority: Optional[int] = None,
    due_string: Optional[str] = None,
    due_date: Optional[str] = None,
    due_datetime: Optional[str] = None,
    due_lang: str = "en",
    assignee_id: Optional[str] = None,
    order: Optional[int] = None,
    auto_reminder: Optional[bool] = None,
    auto_parse_labels: Optional[bool] = None,
    duration: Optional[int] = None,
    duration_unit: Optional[str] = None,
    deadline_date: Optional[str] = None,
    deadline_lang: str = "en",
):
    args_list = {
        "content": content,
        "description": description,
        "project_id": project_id,
        "section_id": section_id,
        "parent_id": parent_id,
        "labels": labels,
        "priority": priority,
        "due_string": due_string,
        "due_date": due_date,
        "due_datetime": due_datetime,
        "due_lang": due_lang,
        "assignee_id": assignee_id,
        "order": order,
        "auto_reminder": auto_reminder,
        "auto_parse_labels": auto_parse_labels,
        "duration": duration,
        "duration_unit": duration_unit,
        "deadline_date": deadline_date,
        "deadline_lang": deadline_lang,
    }

    response = await todoist_client.create_task(**args_list)
    logging.info(response)

    return response


@mcp.tool()
async def update_task(
    task_id: str,
    content: str = None,
    description: str = None,
    labels: List[str] = None,
    priority: int = None,
    due_string: str = None,
    due_lang: str = "en",
    due_date: str = None,
    due_datetime: str = None,
    assignee_id: str = None,
    day_order: int = None,
    collapsed: bool = None,
    duration: int = None,
    duration_unit: str = None,
    deadline_date: str = None,
    deadline_lang: str = "en",
):
    kwargs_list = {
        "content": content,
        "description": description,
        "labels": labels,
        "priority": priority,
        "due_string": due_string,
        "due_lang": due_lang,
        "due_date": due_date,
        "due_datetime": due_datetime,
        "assignee_id": assignee_id,
        "day_order": day_order,
        "collapsed": collapsed,
        "duration": duration,
        "duration_unit": duration_unit,
        "deadline_date": deadline_date,
        "deadline_lang": deadline_lang,
    }
    response = await todoist_client.update_task(task_id, **kwargs_list)
    logging.info(response)
    return response


@mcp.tool()
async def complete_task(task_id: str):
    response = await todoist_client.complete_task(task_id)
    logging.info(response)
    return response


@mcp.tool()
async def delete_task(task_id: str):
    response = await todoist_client.delete_task(task_id)
    logging.info(response)
    return response


@mcp.tool()
async def reopen_task(task_id: str):
    response = await todoist_client.reopen_task(task_id)
    logging.info(response)
    return response


@mcp.tool()
async def get_active_projects():
    projects = await todoist_client.get_active_projects()
    logging.info(projects)
    return projects


@mcp.tool()
async def add_project(
    name: str,
    description: Optional[str] = None,
    parent_id: Optional[str] = None,
    color: Optional[str] = None,
    is_favorite: Optional[bool] = None,
    view_style: Optional[str] = None,
):
    response = await todoist_client.add_project(
        name=name,
        description=description,
        parent_id=parent_id,
        color=color,
        is_favorite=is_favorite,
        view_style=view_style,
    )
    logging.info(response)
    return response


@mcp.tool()
async def delete_project(project_id: str):
    response = await todoist_client.delete_project(project_id)
    logging.info(response)
    return response


@mcp.tool()
async def update_project(project_id: str):
    response = await todoist_client.update_project(project_id)
    logging.info(response)
    return response


@mcp.tool()
async def get_sections(project_id: str):
    sections = await todoist_client.get_sections(project_id)
    logging.info(sections)
    return sections


@mcp.tool()
async def add_section(project_id: str, name: str, order: Optional[int] = None):
    response = await todoist_client.add_section(
        project_id=project_id, name=name, order=order
    )
    logging.info(response)
    return response


@mcp.tool()
async def update_section(section_id: str, name: str):
    response = await todoist_client.update_section(section_id=section_id, name=name)
    logging.info(response)
    return response


@mcp.tool()
async def delete_section(section_id: str):
    response = await todoist_client.delete_section(section_id)
    logging.info(response)
    return response


@mcp.tool()
async def get_labels():
    labels = await todoist_client.get_labels()
    logging.info(labels)
    return labels


@mcp.tool()
async def add_label(
    name: str,
    color: Optional[str] = None,
    item_order: Optional[int] = None,
    is_favorite: Optional[bool] = False,
):
    response = await todoist_client.add_label(
        name=name, color=color, item_order=item_order, is_favorite=is_favorite
    )
    logging.info(response)
    return response


@mcp.tool()
async def update_label(
    label_id: str,
    name: Optional[str] = None,
    color: Optional[str] = None,
    item_order: Optional[int] = None,
    is_favorite: Optional[bool] = False,
):
    response = await todoist_client.update_label(
        label_id=label_id,
        name=name,
        color=color,
        item_order=item_order,
        is_favorite=is_favorite,
    )
    logging.info(response)
    return response


@mcp.tool()
async def delete_label(label_id: str):
    response = await todoist_client.delete_label(label_id)
    logging.info(response)
    return response


def main():
    mcp.run()


if __name__ == "__main__":
    main()
