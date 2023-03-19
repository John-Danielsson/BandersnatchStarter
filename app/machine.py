# from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from pandas import DataFrame
from datetime import datetime
from joblib import load, dump


class Machine:

    # TO DO: download data as a .csv, use in colab for testing

    # Does the class properly handle and store the target
    # and feature data when initializing the model?

    # Does the __init__ function properly initialize the
    # machine learning model and store it as an attribute?
    def __init__(self, df: DataFrame):
        # self.name = "Random Forest Classifier"
        # self.name = "Decision Tree Classifier"
        self.name = "Gaussian Process Classifier"
        # self.model = RandomForestClassifier(
        #     n_estimators=350,
        #     max_depth=19,
        #     min_samples_split=5,
        #     min_samples_leaf=1,
        #     max_features='sqrt',
        #     bootstrap=True,
        #     random_state=random_state
        # )
        # self.model = DecisionTreeClassifier(
        #     criterion='entropy',
        #     splitter='best',
        #     min_samples_split=5,
        #     min_samples_leaf=1,
        #     max_features='sqrt',
        #     max_depth=19,
        #     random_state=random_state
        # )
        self.model = GaussianProcessClassifier(
            kernel=1.0 * RBF(1.0),
            random_state=random_state,
            warm_start=False,
            multi_class='one_vs_one',
            max_iter_predict=300,
            n_jobs=-1
        )
        features = df.drop(columns=['Rarity'])
        target = df['Rarity']
        self.model.fit(features, target)
        self.timestamp = '%s' % datetime.now()

    # Does the call function take in a DataFrame of feature data and
    # return a prediction and the probability of the prediction?
    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        return prediction

    # Does `save()` properly save the machine learning model
    # to the specified filepath using joblib?
    def save(self, filepath: str) -> None:
        dump(value=self.model, filename=filepath)

    # Does `open()` properly load a saved machine learning model
    # from the specified filepath using joblib?
    @staticmethod
    def open(filepath):
        model = load(filepath)
        obj = cls.__new__(cls)
        obj.model = model
        return obj

    # Does `info()` return a string with the name of the base model
    # and the timestamp of when it was initialized?
    def info(self):
        return f'{self.name}, initialized {self.timestamp}'

if __name__ == '__main__':
    machine = Machine(DataFrame({'Rarity': [0], 'Health': [0]}))
    print(machine.info())
