import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("train.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())


# -----------------------------
# Data Cleaning
# -----------------------------

# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin column (too many missing values)
df = df.drop(columns=['Cabin'])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# -----------------------------
# Exploratory Data Analysis
# -----------------------------

# 3.1 Survival Distribution
plt.figure()
df['Survived'].value_counts().plot(kind='bar')
plt.title("Survival Distribution")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()


# 3.2 Survival by Gender
plt.figure()
pd.crosstab(df['Sex'], df['Survived']).plot(kind='bar')
plt.title("Survival by Gender")
plt.ylabel("Count")
plt.show()


# 3.3 Age Distribution
plt.figure()
plt.hist(df['Age'], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# 3.4 Survival by Passenger Class
plt.figure()
pd.crosstab(df['Pclass'], df['Survived']).plot(kind='bar')
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.show()


# 3.5 Fare Distribution
plt.figure()
plt.hist(df['Fare'], bins=20)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()


# 3.6 Correlation Analysis
print("\nCorrelation Matrix:")
print(df[['Age', 'Fare', 'Pclass', 'Survived']].corr())


print("\nEDA Completed Successfully.")
