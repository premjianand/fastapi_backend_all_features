import json

def get_config(file_name):
    try:
        with open(f"/etc/secrets/{file_name}", "r") as file:
            return json.load(file)  # Load JSON as a dictionary
    except (FileNotFoundError, json.JSONDecodeError):
        raise Exception("config error, check secrets.")

file_name = "secret1"
config = get_config(file_name)

