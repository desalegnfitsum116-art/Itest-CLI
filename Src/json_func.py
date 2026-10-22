import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "datastore.json"

def load_data():
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

