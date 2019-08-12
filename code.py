import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import Imputer,LabelEncoder
from scipy.stats import norm, skew

#### Data 1
# Load the data
df = pd.read_csv(path)
print(df.head())

# Overview of the data
df.info()
df.describe()

# Histogram showing distribution of car prices
df['price'].hist(bins=3)

# Countplot of the make column
df['make'].value_counts().plot(kind='bar')

# Jointplot showing relationship between 'horsepower' and 'price' of the car
sns.jointplot(x=df['horsepower'], y=df['price'])

# Correlation heat map
corr = df.corr()

sns.heatmap(corr, vmin=-1, vmax=1, center=0) 

# boxplot that shows the variability of each 'body-style' with respect to the 'price'
df.boxplot(column=['price'], by = 'body-style') 


#### Data 2
# Load the data
df2 = pd.read_csv(path2)
print(df2.head())

df2.info()
df2.describe() 

# Impute missing values with mean

df2 = df2.replace("?","NaN")
numeric_imp = Imputer(missing_values="NaN",strategy='mean',axis=0)
df2['normalized-losses'] = numeric_imp.fit_transform(df2[['normalized-losses']])
df2['horsepower'] = numeric_imp.fit_transform(df2[['horsepower']])
print(df2.head())

# Skewness of numeric features
numeric_feature_auto = df2._get_numeric_data().columns
for feature in numeric_feature_auto:
    if skew(df2[feature])>1:
        df2[feature] = np.sqrt(df2[feature])

# Label encode 
def LabelEncode(df2):
        columnsToEncode = list(df2.select_dtypes(include=['category','object']))
        le = LabelEncoder()
        for feature in columnsToEncode:
            try:
                df2[feature] = le.fit_transform(df[feature])
            except:
                print('Error encoding '+feature)
        return df2
df2 = LabelEncode(df2)

# New feature area by combining height and width
df2['area'] = df2['height'] * df2['width']

# Code ends here
