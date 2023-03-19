# Build Sprint 3: Machine Learning Model

To begin work on this ticket, make sure you have:
- Finished getting locally setup.
- Completed the onboarding in your course.
- Finished Build Sprint 1 and 2.

## Objective

Machine Learning Model
- Notebook exploration
- Machine Learning interface class
- Model serialization (save and open)
- API model integration

To see what your final output should be, navigate to `/model` on the [deployed site](https://bandersnatch.herokuapp.com/).

## Relevant Files

Access `app/machine.py`, where you will add your code for this ticket. 

Stuck? Post in `labs-ds` or open a support ticket in the Hub!

## Deliverables
Submit the following in your course:

- Link to your forked repo with the added code
- Link to a Loom video answering the prompt in the `Submit Your Deliverables` Assignment in your course

## Guidance

### A. Notebook Model Training & Tuning
- [x] Create a notebook for model testing and tuning
- [x] Train and tune at least 3 models using the data generated in an earlier Sprint
- [x] Measure the accuracy of the models and report info about your best model 
- [x] Write a paragraph or two about your best model (see below)

The Gaussian Process Classifier was the best model with an
accuracy score of 0.965, while the Random Forest Classifier
and the Decision Tree Classifier had accuracy scores of
0.925 and 0.900, respectively.

A random forest classifier uses multiple decision trees for
prediction. It builds decision trees and combines their predictions
to make a final decision. Each decision tree in the forest is built on
a random subset of the training data, and at each node, a random subset
of features is considered.

A decision tree classifier builds a tree structure from the training
data. The tree is made up of nodes that represent a decision based on
the input features, making more nodes until a final decision is made.
A Gaussian process classifier is a probabilistic model that represents
a distribution over functions. Instead of predicting a single output
value, Gaussian processes predict a distribution of possible output
values. GPCs use a covariance function to measure the similarity
between input points and make predictions. They are useful in
situations involving limited training data, as they can provide more
informative predictions than other classifiers.

### B. Machine Learning Interface Class
- Starter File: `app/machine`
- Suggested ML Library: Scikit-learn

- [ ] Does the __init__ function properly initialize the machine learning model and store it as an attribute?
- [ ] Does the class properly handle and store the target and feature data when initializing the model?
- [ ] Does the __call__ function take in a DataFrame of feature data and return a prediction and the probability of the prediction?

#### Example Machine Learning Interface
```python
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, pred_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        return prediction

```

### C. Model Serialization
- [ ] Does `save()` properly save the machine learning model to the specified filepath using joblib?
- [ ] Does `open()` properly load a saved machine learning model from the specified filepath using joblib?

### D. API Model Integration
- [x] Does `info()` return a string with the name of the base model and the timestamp of when it was initialized?
