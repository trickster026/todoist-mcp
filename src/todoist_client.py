from typing import List, Optional
from todoist_api_python.api_async import TodoistAPIAsync
import os
from todoist_api_python.models import Task, Project

from models import TasksOutput, ProjectsOutput


class TodoistClient:
    def __init__(self, api_token: Optional[str] = None):
        self.api_token = api_token or os.getenv("TODOIST_API_TOKEN")
        if not self.api_token:
            raise ValueError("TODOIST_API_TOKEN is not set and is required.")

        self.todoist_client = TodoistAPIAsync(token=self.api_token)

    async def get_tasks(self, project_id: Optional[str] = None):
        tasks_iter = await self.todoist_client.get_tasks(project_id=project_id)
        raw_task_batches: List[List[Task]] = [task async for task in tasks_iter]

        all_tasks = [
            TasksOutput(
                id=task.id,
                content=task.content,
                due_date=task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            )
            for task_batch in raw_task_batches
            for task in task_batch
        ]
        return all_tasks

    async def get_active_projects(self):
        projects_iter = await self.todoist_client.get_projects()
        raw_project_batches: List[List[Project]] = [
            project async for project in projects_iter
        ]

        all_projects = [
            ProjectsOutput(
                id=project.id,
                name=project.name,
                description=project.description,
                is_favorite=project.is_favorite,
                is_archived=project.is_archived,
                created_at=project.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                updated_at=project.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                workspace_id=project.workspace_id,
                folder_id=project.folder_id,
            )
            for project_batch in raw_project_batches
            for project in project_batch
        ]
        return all_projects
