import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/ff414a1bcfcba32481e4d4e8db578e55872a2ca1/titanic.csv", sep='\t')

# print(df[["Survived", "Age", "SibSp", "Fare"]].describe())
# print(df[df["Survived"] > 0][["Survived", "Age", "SibSp", "Fare"]].describe())


# print(df[["Died"] = df["Survived"].apply(lambda x: x*2))

# df["Age"].plot("hist")
# plt.show()

# df[df["Survived"] > 0].to_json("test.json")

# print(df.dropna().count())

# print(df.fillna(value=df.mean))

# print(df["Embarked"].unigue())