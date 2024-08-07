import datetime
from database.json_manager import JSONManager

json_manager = JSONManager()


def create_task_version(task):
    versions = json_manager.read_json("task_versions.json")
    if task["id"] not in versions:
        versions[task["id"]] = []
    versions[task["id"]].append(
        {
            "version": len(versions[task["id"]]) + 1,
            "data": task,
            "timestamp": datetime.datetime.now().isoformat(),
        }
    )
    json_manager.write_json("task_versions.json", versions)
