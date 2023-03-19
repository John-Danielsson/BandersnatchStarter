from sklearn.ensemble import RandomForestClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.gaussian_process import GaussianProcessClassifier
# from sklearn.gaussian_process.kernels import RBF
# from sklearn.model_selection import (
#     train_test_split, RandomizedSearchCV, GridSearchCV
# )
# from scipy.stats import uniform
# import pandas as pd
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
        self.name = "Random Forest Classifier"
        self.target = df['Rarity']
        self.features = df.drop(columns=['Rarity'])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = '%s' % datetime.now()

    # Does the call function take in a DataFrame of feature data and
    # return a prediction and the probability of the prediction?
    def __call__(self, feature_basis: DataFrame):
        # prediction = self.model.predict(pred_basis)
        # prediction, *_ = self.model.predict(feature_basis)
        # print('prediction', type(prediction))
        # return prediction
        return self.model.predict(pred_basis)

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


# if __name__ == '__main__':
#     machine = Machine(DataFrame({'Rarity': [0], 'Health': [0]}))
#     print(machine.info())



# nwoiejgoi2gi42hn9c498tn2394htvnw3hg3vhovigh3wigh4iurwehgoiw3hnoit4h


# from pandas import DataFrame
# from sklearn.ensemble import RandomForestClassifier
# from joblib import dump, load
# import datetime
#
#
# class Machine:
#
#     def __init__(self, df: DataFrame):
#         self.name = "Random Forest Classifier"
#         target = df["Rarity"]
#         features = df.drop(columns=["Rarity"])
#         self.model = RandomForestClassifier()
#         self.model.fit(features, target)
#
#     def __call__(self, pred_basis: DataFrame):
#         prediction = self.model.predict(pred_basis)
#         probability = self.model.predict_proba(pred_basis)
#         return prediction
#
#     def save(self, filepath):
#         dump(self.model, filepath)
#
#     @classmethod
#     def open(cls, filepath):
#         model = load(filepath)
#         obj = cls.__new__(cls)
#         obj.model = model
#         return obj
#
#     def info(self):
#         now = datetime.datetime.now()
#         return f"Base Model: {self.name} - Initialized at {now.strftime('%Y-%m-%d %H:%M:%S')}"

