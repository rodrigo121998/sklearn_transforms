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
    def __init__(self,  columna_nueva,columna1,columna2,columna3,columna4):
        self.columna_nueva = columna_nueva
        self.columna1=columna1
        self.columna2=columna2
        self.columna3=columna3
        self.columna4=columna4
        
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data[self.columna_nueva]=data[self.columna1]*data[self.columna2]*(data[self.columna3]+data[self.columna4])
        return data

