
##########################
#    pandas reference    #
##########################

import pandas as pd
import numpy as np

data_path="/home/sfang/windows/gitlab/stanleysfang/code_reference/example_data/"

#### read_csv ####
# parameter names: list of column names; need header=0 if names is specified
# parameter sep: delimiter; default is ','
# parameter dtype: dictionary of columns (e.g. {"Name": "category", "Sex": "category", "Ticket": "category", "Embarked": "category"})
# parameter skiprows: line numbers to skip (0-indexed) or number of lines to skip (int) at the start of file
train = pd.read_csv(
    data_path + "kaggle_titanic_train.csv",
    header=0, names=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'ParCh', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
    dtype={"Name": "category", "Sex": "category", "Ticket": "category", "Embarked": "category"}
)
test = pd.read_csv(
    data_path + "kaggle_titanic_test.csv",
    header=0, names=['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'ParCh', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
    dtype={"Name": "category", "Sex": "category", "Ticket": "category", "Embarked": "category"}
)

#### save_csv ####
# parameter index: write row names; default is True
# parameter header: write column names; default is True
# parameter mode: default is write mode 'w'; append mode is 'a'
# parameter na_rep: missing data representation; default is ''
train.loc[:, train.columns != "Survived"].to_csv(data_path + "kaggle_titanic_full.csv", index=False, mode='w')
test.to_csv(data_path + "kaggle_titanic_full.csv", index=False, header=False, mode='a')

#### attributes ####
train.shape
train.columns
train.dtypes

#### astype ####
# dtypes: int64, float64, category, bool, datetime64[ns]
train["Embarked"].astype("category")

#### statistics ####
train.describe()

train["Age"].min()
train["Age"].max()
train["Age"].mean()
train["Age"].median()
train["Age"].mode()
train["Age"].std()

#### column inspection ####
train["Embarked"].unique()
train["Embarked"].value_counts().sort_values(ascending=True) # ascending defaults to False
train["Embarked"].isna().sum()
train["Embarked"].notna().sum()
train["Embarked"].count()

#### missing value ####
mv = train.isna().sum()[train.isna().sum() != 0]
mv_list = [(mv.index[i], mv[i]) for i in range(0, mv.shape[0])]

train[train["Embarked"].notna()]
train["Age"].fillna(train["Age"].mean())

#### sort_values ####
# parameter na_position: {"first", "last"}; default is "last"
train.sort_values(by="Age", na_position="first")
train.sort_values(by=["Pclass", "Fare"], ascending=[True, False])

#### groupby ####
train[["Pclass", "Fare"]].groupby(["Pclass"]).mean()

#### isin ####
train[train["Ticket"].isin(["347082", "CA. 2343"])].sort_values(by=["Ticket", "Age"], ascending=[True, False])

#### cap ####
upper_cap = np.percentile(train["Fare"], 95)
train.loc[train["Fare"] > upper_cap, "Fare"] = upper_cap

#### row number ####
train = train.sort_values(by=["Fare", "Age", "PassengerId"], ascending=[False, False, True])
train["Fare_Rank"] = np.arange(train.shape[0], dtype="int64")+1

#### concat ####
# parameter axis: concat along rows if 0 and columns if 1; default is 0
# parameter sort: sort along the non-concat axis; default is True is old pandas version
# parameter join: how to handle indices on other axis {"inner", "outer"}; default is "outer"
full = pd.concat([train.loc[:, train.columns != "Survived"], test], sort=False)
pd.concat([pd.DataFrame(np.arange(full.shape[0], dtype="int64")+1, columns=["row_number"]), full.reset_index(drop=True)], axis=1, sort=False) # make sure indices are reset when concat along columns
