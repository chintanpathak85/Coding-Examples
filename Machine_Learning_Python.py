
###########################################
#Written By - Chintan Pathak
#Summary - This program tries to find answer to as why employee are leaving the company. 
#The input file is csv file HR_Data.csv. 
#First step after upload is parsing, sorting & grouping to find out why best & most experienced employee are leaving the company. 
#Later, I built and tested predictive model to forecast employee leaving the company and conclude which model is better
#Note: Change the path to actual path to store output files
###########################################


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split

#IMPORTING DATA(PUT YOUR OWN PATH)
hrData = pd.read_csv("path/HR_Data_python.csv")
hrData = hrData.rename(columns = {'sales':'department'})

# In order to explore why employee are leaving. I tried to find mean column value with groupby 'left' column

print hrData.groupby('left').mean()

# INITIAL OBSERVATIONS
#The average satisfaction level of employees who stayed with the company is higher than that of the employees who left.
#The average monthly work hours of employees who left the company is more than that of the employees who stayed.
#The employees who had workplace accidents are less likely to leave than that of the employee who did not have workplace accidents.
#The employees who were promoted in the last five years are less likely to leave than those who did not get a promotion in the last five years.


# More exploration -
# I tried to search fields which are not numerics i.e. - Department & Salary

print hrData.groupby('department').mean()
print hrData.groupby('salary').mean()


# RESULT
# Group By Department - I observe that more employees left in 'accounting' & 'HR' compared to other departments with job satisfaction lowest
# Group By salary - I observed that the employee with lowest salary tend to leave company more compare to higher salary employee


# BAR CHART TO INVESTIGATE WHY EMPLOYEE ARE LEAVING

# Department Vs Left column
pd.crosstab(hrData.department,hrData.left).plot(kind='bar')
plt.title('Turnover Frequency for Department')
plt.xlabel('Department')
plt.ylabel('Frequency of Turnover')
plt.savefig('department_bar_chart')

# Salary Vs Left column
table=pd.crosstab(hrData.salary, hrData.left)
table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of Salary Level vs Turnover')
plt.xlabel('Salary Level')
plt.ylabel('Proportion of Employees')
plt.savefig('path/salary_bar_chart')


# CONCLUSION FROM ABOVE ANALYSIS-
# Looking at the above analysis - the proportion of the employee turnover depends a great deal on their salary level; hence, salary level can be a good predictor in predicting why many employee are leaving the company.


#See dimension of data
#hrData.shape
#print hrData


#VISUALIZATION OF ALL EMPLOYEE RELATIVE FIELD
hrData.hist(bins=10, figsize=(20,15))
hrData.hist()
plt.savefig("path/hrData_histogram_plots")
#plt.show()

#One can use scatter plot to display these data

#DATA PROCESSING FOR ML IMPLEMENTATION
#As we have two field which are text we need to convert unique records to columns with dummy values
cat_vars=['department','salary']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(hrData[var], prefix=var)
    hrData1=hrData.join(cat_list)
    hrData=hrData1

hrData.drop(hrData.columns[[8, 9]], axis=1, inplace=True)
#print hrData.columns.values

hrData_vars=hrData.columns.values.tolist()
y='left'
x=[i for i in hrData_vars if i not in y]


print "\n\n####### Machine Learning Models Implementation #######\n"
# APPLYING MACHINE LEARNING MODELS
# Here I used 3 Models - Linear Regression, Decision Tree Classifiers, and Random Forest Classifier to forecast

print "Applying Linear Regression.."
#Linear Regression
lm = LinearRegression()
lm = lm.fit(hrData[x],hrData.left)
#print lm.predict(hrData[x])


print "Applying Decision Tree.."
#Decision Tree Classifier
dtc = DecisionTreeClassifier()
dtc = dtc.fit(hrData[x], hrData[y])
#print dtc.predict(hrData[x])
# For prediction we can also individual values instead of hrData[x]. For example [0,1,2,3,4,,5]

print "Applying Random Forest..."
# Random Forest Classifier
rfc = RandomForestClassifier()
rfc = rfc.fit(hrData[x], hrData.left)
#print rfc.predict(hrData[x])


# ACCURACY CHECK USING RMSE MEHTOD

print "\nCheck Accuracy of Models\n"
# Now check accuracy of model using Root Mean Square Error

print "Error - Linear Regression"
mse_lm = np.mean((hrData[y] - lm.predict(hrData[x]))**2)
print mse_lm

print"Error Decision Tree"
mse_dtc = np.mean((hrData[y] - dtc.predict(hrData[x]))**2)
print mse_dtc

print "Error - Random Forest"
mse_rfe = np.mean((hrData[y] - rfc.predict(hrData[x]))**2)
print mse_rfe
print "\n"

# CROSS-VALIDATION
print "Cross-Validation Models"
#In order to cross validate data we take a subset of data and target data
cols=['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years',
      'department_RandD', 'department_hr', 'department_management', 'salary_high', 'salary_low']
a=hrData[cols]
b=hrData['left']

X_train, X_test, y_train, y_test = train_test_split(a, b, test_size=0.3, random_state=0)

# Perform cross validation for linear regression
lr = LinearRegression()
lr = lr.fit(X_train, y_train)
lr_x_pred = lr.predict(X_test)
print('\n\nCross-Validate value for  Linear Regression ', mean_squared_error(y_test,lr_x_pred))


# Perform cross validation for decision tree classifier
dt = DecisionTreeClassifier()
dt = dt.fit(X_train, y_train)
dt_x_pred = dt.predict(X_test)
print('\n\nCross-Validate value for  Decision Tree Classifier ', mean_squared_error(y_test,dt_x_pred))


# Perform cross validation for decision tree classifier
rf = RandomForestClassifier()
rf = rf.fit(X_train, y_train)
rf_x_pred = rf.predict(X_test)
print('\n\nCross-Validate value for  Random Forest Classifier ', mean_squared_error(y_test,rf_x_pred))


#Conclusion - By Cross validation we see values of to be similar to those found without using subset of data i.e obtain during error check. The values for linear regression(error checking and cross-validation) seems to be very similar showing that it could be more reliable to forecase but if you consider lowest error value than decision tree could be better to forecast












