import datetime


def sync_task(local_task, cloud_task):
    if local_task["last_modified"] > cloud_task["last_modified"]:
        update_cloud_task(local_task)
    elif cloud_task["last_modified"] > local_task["last_modified"]:
        update_local_task(cloud_task)
    else:
        # Implement conflict resolution strategy
        resolve_conflict(local_task, cloud_task)


# TODO implement update_cloud_task, update_local_task, and resolve_conflict
