for client in Storage.domain(["hub", "client-(\d+)"]):

for task in Storage.domain(["hub", "client-001", "task-(\d+)"]):
    task.get("module")
    task.get("name")
    task.get("params")
    task.get("schedule")
