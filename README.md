# Digit-Recognizer
Kaggle project using MNIST dataset

####Steps:
1. Install kaggle package to be able to use kaggle API.
- Download the credentials file (kaggle.json) from kaggle.com -> My Account -> Create API Token.
- Store the file at ~/.kaggle/kaggle.json

2. Download dataset using api commands
- `kaggle competitions download -c digit-recognizer`

3. Build a framework to spot check algoriths
- There are four parts to the framework that we need to develop; they are:
    1. Load Dataset - return X, y elements
    2. Define Models - create a dict of models
    3. Evaluate Models - Build a pipeline (to transform data prior to feeding it to the model)
    4. Summarize Results - as. 
    
####References:
1. Framework - https://machinelearningmastery.com/spot-check-machine-learning-algorithms-in-python/
2. Guidance - https://www.slideshare.net/0xdata/design-patterns-for-machine-learning-in-production
