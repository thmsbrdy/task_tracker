import json
from pathlib import Path

path = Path("tasks.json")

if not path.exists():
    with open(path, 'w') as f:
        json.dump({"task": []},f)

with open(path,'w') as f:
    json.dump([],f)


"""
with open(path, 'r') as f:
    data = json.load(f)

for i in range(4):
    description = "test" + str(i + 2)
    id = i + 2
    newTask = {"ID":id, "Description":description}
    data["task"].append(newTask)

with open(path, 'w') as f:
    json.dump(data,f)
"""