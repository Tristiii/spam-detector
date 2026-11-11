from utils import get_model
from joblib import load

def predict_text(text: str) -> str:
    model = load(get_model())
    result = model.predict([text])[0]

    match result:
        case 'spam':
            return 'Result: this message is SPAM.'
        case _:
            return 'Result: this message is NOT spam.'