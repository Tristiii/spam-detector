from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent

def get_model() -> Path:
    return get_project_root() / 'model' / 'model.pkl'

def get_data() -> Path:
    return get_project_root() / 'data' / 'SMSSpamCollection.txt'