# First Task is to build an ML regression model with the data
import numpy as np
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Step 1: Read the data
######Enter Code here#######################
data=None
##################################################

# Step 2: Extract (bmi and age) features as X and charges as Y
#######Enter Code here############
X=None
y=None
####################################

# Step 3: Fit a regression model using (X,y), save the model as treemodel.pkl
####Add code here
model=None
pickle.dump(model,open('treemodel.pkl','wb'))
###########################################

#Step 4: Test the model for a sample input
model1=pickle.load(open('treemodel.pkl','rb'))
x_test=np.array([[15,120]])
print(x_test)
print(model1.predict(x_test))
