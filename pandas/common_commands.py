
#### pandas ####

# read_csv()
df = pd.read_csv("/path/to/file.csv")

df["A"].mean()
df["A"].median()
df["A"].std()

df["A"].value_counts()

# to_csv()
df.to_csv("file.csv")

# attributes
df.shape
df.columns
df.dtypes

# astype
df["A"].astype()

# isna()
df.isna()
df["A"].isna()

# isin()
df[df["A"].isin([1, 2])]

