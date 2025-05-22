from ast import List
from typing import Optional
from todoist_api_python.api_async import TodoistAPIAsync
import os

from todoist_api_python.models import Task

from models import TasksOutput


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
            TasksOutput(id=task.id, content=task.content,
                        due_date=task.created_at.strftime("%Y-%m-%d %H:%M:%S"))
            for task_batch in raw_task_batches
            for task in task_batch
        ]
        return all_tasks
