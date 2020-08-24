from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
class Scorecolumn(BaseEstimator, TransformerMixin):
    def __init__(self,columns=None):
        self.columns=columns
        
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data["score_ds"]=data["HOURS_DATASCIENCE"]*data["AVG_SCORE_DATASCIENCE"]*(data["NUM_COURSES_BEGINNER_DATASCIENCE"]+data["NUM_COURSES_ADVANCED_DATASCIENCE"])
        data["score_be"]=data["HOURS_BACKEND"]*data["AVG_SCORE_BACKEND"]*(data["NUM_COURSES_BEGINNER_BACKEND"]+data["NUM_COURSES_ADVANCED_BACKEND"])
        data["score_fe"]=data["HOURS_FRONTEND"]*data["AVG_SCORE_FRONTEND"]*(data["NUM_COURSES_BEGINNER_FRONTEND"]+data["NUM_COURSES_ADVANCED_FRONTEND"])
        return data

