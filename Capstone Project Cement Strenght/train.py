print("Script started")

import pandas as pd 
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor 
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.tree import export_text
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

df = pd.read_csv('Concrete_Data_Yeh.csv')

df_full_train, df_test = train_test_split (df, test_size = 0.2, random_state = 42)
df_train, df_val = train_test_split (df_full_train, test_size = 0.25, random_state = 42)

df_train = df_train.reset_index(drop = True)
df_val = df_val.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)

y_train = df_train['csMPa']
y_val = df_val['csMPa']
y_test = df_test['csMPa']

del df_train['csMPa']
del df_val['csMPa']
del df_test['csMPa']

print("Training model")
# Training the model
train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)

model = XGBRegressor(booster='dart', learning_rate = 0.1, max_depth=4, n_estimators=500)



model.fit(X_train, y_train)

with open('FinalModel.bin', 'wb') as f_out:
    pickle.dump((dv, model), f_out)
    
print("The model is saved to 'FinalModel.bin'")
