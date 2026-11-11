import pandas as pd
from utils import get_project_root

ROOT = get_project_root()

def load_file() -> pd.DataFrame:

    data: list[list[str]] = []
    with open(ROOT / 'data' / 'SMSSpamCollection.txt') as f:
        for raw_line in f:
            line = raw_line.strip().split('\t', maxsplit=2)
            data.append(line)

    return pd.DataFrame(data, columns=['target', 'data'])