import json
import os

def get_default_dir(json_file_path="cache\config.json"):
    # Check if the JSON file exists
    if os.path.exists(json_file_path):
        # Load the existing JSON data
        with open(json_file_path, "r") as file:
            data = json.load(file)
        return data.get("default_dir", None)
    else:
        return None  # JSON file doesn't exist or "default_dir" key not found

def update_default_dir(default_dir, json_file_path="cache\config.json"):
    # Check if the JSON file exists
    if os.path.exists(json_file_path):
        # Load the existing JSON data
        with open(json_file_path, "r") as file:
            data = json.load(file)
        data["default_dir"] = default_dir
    else:
        # If the JSON file doesn't exist, create a new one with the "default_dir" parameter
        data = {
            "default_dir": default_dir
        }
    
    # Save the updated JSON data back to the file
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)
        
def clear_default_dir(json_file_path="cache\config.json"):
    if os.path.exists(json_file_path):
        # Load the existing JSON data
        with open(json_file_path, "r") as file:
            data = json.load(file)
        data["default_dir"] = "null"
    else:
        data = {
            "default_dir": "null"
        }
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)