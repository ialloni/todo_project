import datetime

import aiohttp


class BackendClient:

    @staticmethod
    async def get_tasks(user_id) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "http://backend:8000/api/v1/task/", params=user_id
            ) as response:
                return await response.json()

    @staticmethod
    async def get_today_tasks() -> list[dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://backend:8000/api/v2/task/") as response:
                return await response.json()

    @staticmethod
    async def add_task(content: str, category: str, due_time: str, user_tg_id: int):
        data = {
            "content": content,
            "category": category,
            "due_time": due_time,
            "user_tg_id": user_tg_id,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://backend:8000/api/v1/task/",
                json=data,
                headers={"Content-Type": "application/json"},
            ) as response:
                print(await response.json())

    @staticmethod
    def parse_tasks(tasks: list[dict]) -> str:
        task_lines = (
            f"{task['content']}\n" f"{task['category']}\n" f"{task['created_at']}\n"
            for task in tasks
        )
        return "\n".join(task_lines)
