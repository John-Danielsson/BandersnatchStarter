from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from pandas import DataFrame
from datetime import datetime
from joblib import load, dump


class Machine:

    """Initializes the Machine object and fits the ML model to the
    given data."""
    def __init__(self, df: DataFrame):
        self.name = "Gaussian Process Classifier"
        self.model = GaussianProcessClassifier(
            kernel=1.0 * RBF(1.0),
            random_state=4,
            warm_start=False,
            multi_class='one_vs_one',
            max_iter_predict=300,
            n_jobs=-1
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
