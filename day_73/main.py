import pandas
import matplotlib.pyplot as plt


test_df = pandas.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

data_frame = pandas.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
print(data_frame.shape)
print(data_frame.count())

print(data_frame.groupby("TAG")[["POSTS"]].sum().sort_values(by="POSTS", ascending=False))

print(data_frame.groupby("TAG")[["DATE"]].count().sort_values(by="DATE", ascending=False))

type(data_frame.DATE[1])

data_frame.DATE = pandas.to_datetime(data_frame.DATE)

reshaped_data_frame = data_frame.pivot(index="DATE", columns="TAG", values="POSTS").fillna(0.0)

print(reshaped_data_frame.shape)
print(reshaped_data_frame.columns)
print(reshaped_data_frame.count())
print(reshaped_data_frame.isna().values.any())

print(reshaped_data_frame.head())
print(reshaped_data_frame.tail())

plt.plot(reshaped_data_frame.java)
plt.show()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.plot(reshaped_data_frame.index, reshaped_data_frame.java)
plt.show()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date",  fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_data_frame.index, reshaped_data_frame.java)
plt.show()

plt.figure(figsize=(14, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.plot(reshaped_data_frame.index, reshaped_data_frame.java)
plt.plot(reshaped_data_frame.index, reshaped_data_frame.python)
plt.show()

plt.figure(figsize=(14, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.xlabel("Date", fontsize=14)
for column in reshaped_data_frame.columns:
  plt.plot(reshaped_data_frame[column], linewidth=3, label=reshaped_data_frame[column].name)

plt.legend(fontsize=16)
plt.show()

roll_data_frame = reshaped_data_frame.rolling(window=7).mean()
plt.figure(figsize=(14, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylim(0, 35000)
for column in roll_data_frame.columns:
  plt.plot(roll_data_frame[column], linewidth=3, label=roll_data_frame[column].name)

plt.legend(fontsize=16)
plt.show()

