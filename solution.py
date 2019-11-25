import pandas as pd

df = pd.read_csv("election_data.csv")

# print(df)

total_num_votes = df['Voter ID'].shape
print(total_num_votes)

count_df = df.groupby("Candidate").count()
# print(count_df)
print(count_df['Voter ID'])