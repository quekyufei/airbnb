import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

data = pd.read_csv("processed_user_onehot.csv")  
print (data.head())
X = data.drop('country_destination', axis = 1)
y = data['country_destination']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)  


svclassifier = SVC(kernel='sigmoid')  
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)  

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))  
print(classification_report(y_test, y_pred))  
