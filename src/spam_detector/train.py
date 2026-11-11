from preprocessing import load_file
from utils import get_model

from joblib import dump, load

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score

def train_model() -> float:
    df = load_file()
    X, y = df['data'], df['target']

    model = Pipeline([
        ('vect', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    Xtrain, Xtest, ytrain, ytest = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(Xtrain, ytrain)
    dump(model, get_model())

    y_model = model.predict(Xtest)
    return accuracy_score(y_model, ytest)