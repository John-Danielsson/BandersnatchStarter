from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from pandas import DataFrame, read_csv
from datetime import datetime
from joblib import load, dump


class Machine:

    # Does the __init__ function properly initialize the
    # machine learning model and store it as an attribute?
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
        # self.model = {
        #     "name": "Decision Tree Classifier",
        #     "model": DecisionTreeClassifier(
        #         criterion='entropy',
        #         splitter='best',
        #         min_samples_split=5,
        #         min_samples_leaf=1,
        #         max_features='sqrt',
        #         max_depth=19,
        #         random_state=4
        #     )
        # }
        # Got this warning message when running the web app:
        # The optimal value found for dimension 0 of parameter k1__constant_value is
        # close to the specified upper bound 100000.0.Increasing the bound and calling
        # fit again may find a better value.
        # self.model = {
        #     "name": "Gaussian Process Classifier",
        #     "model": GaussianProcessClassifier(
        #         kernel=1.0 * RBF(1.0),
        #         random_state=4,
        #         warm_start=False,
        #         multi_class='one_vs_one',
        #         max_iter_predict=300,
        #         n_jobs=-1
        #     )
        # }
        # Does the class properly handle and store the target
        # and feature data when initializing the model?
        # self.df = df
        features = df[["Level", "Health", "Energy", "Sanity"]]
        target = df['Rarity']
        self.model.fit(features, target)
        self.timestamp = '%s' % datetime.now()

    # Does the call function take in a DataFrame of feature data and
    # return a prediction and the probability of the prediction?
    def __call__(self, prediction_features: DataFrame):
        prediction = self.model["model"].predict(prediction_features)
        probability = max(self.model["model"].predict_proba(prediction_features))
        return prediction, probability
        # return self.model["model"].predict(prediction_features)

    # Does `save()` properly save the machine learning model
    # to the specified filepath using joblib?
    def save(self, filepath: str) -> None:
        dump(value=self, filename=filepath)

    # Does `open()` properly load a saved machine learning model
    # from the specified filepath using joblib?
    @staticmethod
    def open(filepath: str) -> "Machine":
        return load(filepath)

    # Does `info()` return a string with the name of the base model
    # and the timestamp of when it was initialized?
    def info(self):
        return f'{self.name}, initialized {self.timestamp}'

if __name__ == '__main__':
    machine = Machine(read_csv('bandersnatch_data_1.csv'))
    print(machine.info())
    machine.save('app/model.joblib')
    machine2 = machine.open('app/model.joblib')
    print(machine2.info())
