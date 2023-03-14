from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

class Machine:

    # Does the class properly handle and store the target
    # and feature data when initializing the model?

    # Does the __init__ function properly initialize the
    # machine learning model and store it as an attribute?
    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df['Rarity']
        X = df.drop(columns=['Rarity'])
        self.model = RandomForestClassifier()
        self.model.fit(X, target)
        self.timestamp = '%s' % datetime.now()

    # Does the call function take in a DataFrame of feature data and
    # return a prediction and the probability of the prediction?
    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(feature_basis)
        return prediction

    # Does `save()` properly save the machine learning model
    # to the specified filepath using joblib?
    def save(self, filepath):
        pass

    # Does `open()` properly load a saved machine learning model
    # from the specified filepath using joblib?
    @staticmethod
    def open(filepath):
        pass

    # Does `info()` return a string with the name of the base model
    # and the timestamp of when it was initialized?
    def info(self):
        return f'{self.name}, initialized {self.timestamp}'

if __name__ == '__main__':
    machine = Machine(DataFrame({'Rarity':[0], 'Health':[0]}))
    print(machine.info())