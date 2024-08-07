from core import sync, cache, security, versioning
from database.json_manager import JSONManager
from utils.google_sheets import GoogleSheets


class TaskService:
    def __init__(self):
        self.json_manager = JSONManager()
        self.sheets = GoogleSheets()

    def update_task(self, task_id, updates):
        local_task = self.json_manager.get_task_metadata(task_id)
        cloud_task = self.sheets.get_task(task_id)

        sync.sync_task(local_task, cloud_task)

        updated_task = {**local_task, **updates}
        versioning.create_task_version(updated_task)

        encrypted_task, key = security.encrypt_data(str(updated_task))
        # Store the encrypted task and key securely

        cache.update_cache(f"task_{task_id}", updated_task)

        self.json_manager.update_task_metadata(task_id, updated_task)
        self.sheets.update_task(task_id, updated_task)
