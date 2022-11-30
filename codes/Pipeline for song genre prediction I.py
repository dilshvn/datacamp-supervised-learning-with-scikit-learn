# Import modules
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


# Instantiate an imputer
imputer = SimpleImputer()

# Instantiate a knn model
knn = KNeighborsClassifier(3)

# Build steps for the pipeline
steps = [("imputer", imputer), 
         ("knn", knn)]