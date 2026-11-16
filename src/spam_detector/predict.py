from utils import get_model
from joblib import load

def predict_text(text: str) -> bool:
    model = load(get_model())
    result = model.predict([text])[0]

    match result:
        case 'spam':
            return True
        case _:
            return False