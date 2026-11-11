import pandas as pd
from utils import get_data

def clean_text(text: str) -> str:
    text = text.lower()
    return text

def load_file() -> pd.DataFrame:
    data: list[list[str]] = []
    with open(get_data()) as f:
        for raw_line in f:
            line = raw_line.strip().split('\t', maxsplit=2)
            data.append(line)

    df = pd.DataFrame(data, columns=['target', 'data'])
    df['data'] = df['data'].apply(clean_text)
    return df