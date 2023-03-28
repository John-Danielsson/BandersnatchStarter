from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame
from datetime import datetime
from joblib import load, dump


class Machine:

    """Initializes the machine learning model, fits it to the
    given data, and stores the model as an attribute."""
    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        self.model = RandomForestClassifier(
            n_estimators=350,
            max_depth=19,
            min_samples_split=5,
            min_samples_leaf=1,
            max_features='sqrt',
            bootstrap=True,
            random_state=4
        )
        features = df[["Level", "Health", "Energy", "Sanity"]]
        target = df['Rarity']
        self.model.fit(features, target)
        self.timestamp = '%s' % datetime.now()

    """Returns a prediction value and the confidence for that prediction value."""
    def __call__(self, prediction_features: DataFrame):
        prediction, *_ = self.model.predict(prediction_features)
        probability, *_ = self.model.predict_proba(prediction_features)
        return prediction, max(probability)

    """Saves the machine learning model to the specified filepath."""
    def save(self, filepath: str) -> None:
        dump(value=self, filename=filepath)

    """Loads a saved machine learning model from the given filepath."""
    @staticmethod
    def open(filepath: str) -> "Machine":
        return load(filepath)

    """Returns a string with the name of the model and a timestamp showing
    when the model was initialized."""
    def info(self):
        return f'{self.name}, initialized {self.timestamp}'
