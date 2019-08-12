# --------------
# Code starts here
import pandas as pd
import seaborn as sns
#### Data 1
# Load the data

# # df = pd.read_csv(path)
# # print(df.head())
# # # Overview of the data
# # df.info()
# # df.describe()

# # # Histogram showing distribution of car prices
# # df['price'].hist(bins=3)

# # # Countplot of the make column
# # df['make'].value_counts().plot(kind='bar')

# # # Jointplot showing relationship between 'horsepower' and 'price' of the car
# # sns.jointplot(x=df['horsepower'], y=df['price'])

# # Correlation heat map
# corr = df.corr()

# sns.heatmap(corr, vmin=-1, vmax=1, center=0) 

# # boxplot that shows the variability of each 'body-style' with respect to the 'price'
# df.boxplot(column=['price'], by = 'body-style') 

#### Data 2
# Load the data
df2 = pd.read_csv(path2)

print(df2.head())
df2.info()
df2.describe() 
# Impute missing values with mean


# Skewness of numeric features



# Label encode 



# Code ends here


