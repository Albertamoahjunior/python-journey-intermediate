import json

new_task = {
    "Name": "Kofi",
    "due_time": "time ",
    "subtasks": {"Name":"Mike", "due_time":"date" },
}

# save_task = json.dumps(new_task)

file = open("data.json", "w")

# json.dump(new_task, file)

file.close()