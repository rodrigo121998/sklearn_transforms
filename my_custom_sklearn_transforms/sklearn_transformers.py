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
        data['score_ds']=(data.HOURS_DATASCIENCE*data.AVG_SCORE_DATASCIENCE*(data.NUM_COURSES_BEGINNER_DATASCIENCE+data.NUM_COURSES_ADVANCED_DATASCIENCE))
        data['score_be']=(data.HOURS_BACKEND*data.AVG_SCORE_BACKEND*(data.NUM_COURSES_BEGINNER_BACKEND+data.NUM_COURSES_ADVANCED_BACKEND))
        data['score_fe']=(data.HOURS_FRONTEND*data.AVG_SCORE_FRONTEND*(data.NUM_COURSES_BEGINNER_FRONTEND+data.NUM_COURSES_ADVANCED_FRONTEND))
        return data
class resampling(BaseEstimator, TransformerMixin):
    def __init__(self,columns=None):
        self.columns=columns
        
    def fit(self, X, y):
        return self

    def transform(self, X,y):
        data = X.copy()
        data['OBJETIVO']=y
        sospe=data['OBJETIVO'].value_counts()['Sospechoso']
        acep=data['OBJETIVO'].value_counts()['Aceptado']
        df_majority = data[data.OBJETIVO=='Aceptado']
        df_minority = data[data.OBJETIVO=='Sospechoso']
 
        df_minority_upsampled = resample(df_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=sospe*2,    # to match majority class
                                 random_state=123) # reproducible results
        df_majority_downsampled = resample(df_majority, 
                                 replace=False,    # sample without replacement
                                 n_samples=acep//2,     # to match minority class
                                 random_state=123) # reproducible results
 
        df_new = pd.concat([df_majority_downsampled, df_minority_upsampled])
        return df_new.iloc[:,:-1].reset_index().drop(['index'],axis=1),df_new.iloc[:,-1].reset_index().drop(['index'],axis=1)
