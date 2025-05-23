from typing import List, Optional
from requests import HTTPError
from todoist_api_python.api_async import TodoistAPIAsync
import os
from todoist_api_python.models import (
    Label as RawLabel,
    Section as RawSection,
    Task as RawTask,
    Project as RawProject,
)

from models import Task, Project, Section, Label


class TodoistClient:
    def __init__(self, api_token: Optional[str] = None):
        self.api_token = api_token or os.getenv("TODOIST_API_TOKEN")
        if not self.api_token:
            raise ValueError("TODOIST_API_TOKEN is not set and is required.")

        self.todoist_client = TodoistAPIAsync(token=self.api_token)

    async def get_tasks(
        self,
        project_id: Optional[str] = None,
        section_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        label: Optional[str] = None,
        ids: Optional[List[str]] = None,
        limit: Optional[int] = None,
    ):
        tasks_iter = await self.todoist_client.get_tasks(
            project_id=project_id,
            section_id=section_id,
            parent_id=parent_id,
            label=label,
            ids=ids,
            limit=limit,
        )
        raw_task_batches: List[List[RawTask]] = [task async for task in tasks_iter]

        all_tasks = [
            Task(
                id=task.id,
                content=task.content,
                created_at=task.created_at,
                updated_at=task.updated_at,
                completed_at=task.completed_at,
                url=task.url,
                project_id=task.project_id,
                section_id=task.section_id,
                parent_id=task.parent_id,
                duration=task.duration,
                labels=task.labels,
                due=task.due.__dict__ if task.due else None,
                meta=task.meta.__dict__ if task.meta else None,
                creator_id=task.creator_id,
            )
            for task_batch in raw_task_batches
            for task in task_batch
        ]
        return all_tasks

    async def create_task(self, **kwargs):
        try:
            task = await self.todoist_client.add_task(**kwargs)
            return {"message": "Task created successfully", "task": task}
        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def update_task(self, task_id: str, **kwargs):
        try:
            task = await self.todoist_client.update_task(task_id, **kwargs)
            return {"message": "Task updated successfully", "task": task}
        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def complete_task(self, task_id: str):
        try:
            task = await self.todoist_client.complete_task(task_id)
            return {"message": "Task completed successfully", "task": task}
        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def delete_task(self, task_id: str):
        try:
            task = await self.todoist_client.delete_task(task_id)
            if task:
                return {"message": "Task deleted successfully", "task": task}
            else:
                return {"error": "Something went wrong while deleting the task."}
        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def reopen_task(self, task_id: str):
        try:
            task = await self.todoist_client.uncomplete_task(task_id)
            return {"message": "Task reopened successfully", "task": task}
        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def get_active_projects(self):
        projects_iter = await self.todoist_client.get_projects()
        raw_project_batches: List[List[RawProject]] = [
            project async for project in projects_iter
        ]

        all_projects = [
            Project(
                id=project.id,
                name=project.name,
                description=project.description,
                is_favorite=project.is_favorite,
                is_archived=project.is_archived,
                created_at=project.created_at,
                updated_at=project.updated_at,
            )
            for project_batch in raw_project_batches
            for project in project_batch
        ]
        return all_projects

    async def add_project(
        self,
        name: str,
        description: Optional[str] = None,
        parent_id: Optional[str] = None,
        color: Optional[str] = None,
        is_favorite: Optional[bool] = None,
        view_style: Optional[str] = None,
    ):
        try:
            project = await self.todoist_client.add_project(
                name=name,
                description=description,
                parent_id=parent_id,
                color=color,
                is_favorite=is_favorite,
                view_style=view_style,
            )
            return {"message": "Project added successfully", "project": project}
        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def delete_project(self, project_id: str):
        try:
            response = await self.todoist_client.delete_project(project_id)
            if response:
                return {"message": "Project deleted successfully"}
            else:
                return {"error": "Something went wrong while deleting the project."}

        except HTTPError as e:
            return {"error": str(e)}

    async def update_project(self, project_id: str, **kwargs):
        try:
            project = await self.todoist_client.update_project(project_id, **kwargs)
            return {"message": "Project updated successfully", "project": project}
        except HTTPError as e:
            return {"error": str(e)}

    async def get_sections(self, project_id: str):
        try:
            sections_iter = await self.todoist_client.get_sections(project_id)
            raw_section_batches: List[List[RawSection]] = [
                section async for section in sections_iter
            ]

            all_sections = [
                Section(
                    id=section.id,
                    name=section.name,
                    project_id=section.project_id,
                    order=section.order,
                )
                for section_batch in raw_section_batches
                for section in section_batch
            ]

            return all_sections

        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def add_section(
        self, project_id: str, name: str, order: Optional[int] = None
    ):
        try:
            section = await self.todoist_client.add_section(
                project_id=project_id, name=name, order=order
            )
            return {"message": "Section added successfully", "section": section}
        except HTTPError as e:
            return {"error": str(e)}

    async def update_section(self, section_id: str, name: str):
        try:
            section = await self.todoist_client.update_section(
                section_id=section_id, name=name
            )
            return {"message": "Section updated successfully", "section": section}
        except HTTPError as e:
            return {"error": str(e)}

    async def delete_section(self, section_id: str):
        try:
            response = await self.todoist_client.delete_section(section_id=section_id)
            if response:
                return {"message": "Section deleted successfully"}
            else:
                return {"error": "Something went wrong while deleting the section."}
        except HTTPError as e:
            return {"error": str(e)}

    async def get_labels(self):
        try:
            labels_iter = await self.todoist_client.get_labels()
            raw_label_batches: List[List[RawLabel]] = [
                label async for label in labels_iter
            ]

            all_labels = [
                Label(
                    id=label.id,
                    name=label.name,
                    color=label.color,
                    order=label.order,
                    is_favorite=label.is_favorite,
                )
                for label_batch in raw_label_batches
                for label in label_batch
            ]

            return all_labels

        except (HTTPError, TypeError) as e:
            return {"error": str(e)}

    async def add_label(
        self,
        name: str,
        color: Optional[str] = None,
        item_order: Optional[int] = None,
        is_favorite: Optional[bool] = False,
    ):
        try:
            label = await self.todoist_client.add_label(
                name=name,
                color=color,
                item_order=item_order,
                is_favorite=is_favorite,
            )
            return {"message": "Label added successfully", "label": label}
        except HTTPError as e:
            return {"error": str(e)}

    async def update_label(
        self,
        label_id: str,
        name: str,
        color: Optional[str] = None,
        item_order: Optional[int] = None,
        is_favorite: Optional[bool] = False,
    ):
        try:
            label = await self.todoist_client.update_label(
                label_id=label_id,
                name=name,
                color=color,
                item_order=item_order,
                is_favorite=is_favorite,
            )
            return {"message": "Label updated successfully", "label": label}
        except HTTPError as e:
            return {"error": str(e)}

    async def delete_label(self, label_id: str):
        try:
            response = await self.todoist_client.delete_label(label_id=label_id)
            if response:
                return {"message": "Label deleted successfully"}
            else:
                return {"error": "Something went wrong while deleting the label."}
        except HTTPError as e:
            return {"error": str(e)}
