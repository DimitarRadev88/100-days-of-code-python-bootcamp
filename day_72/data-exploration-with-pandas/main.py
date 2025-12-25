import pandas

pandas.options.display.float_format = "{:,.2f}".format

data_frame = pandas.read_csv("salaries_by_college_major.csv")

print(data_frame.head())

print(data_frame.shape)

print(data_frame.columns)

data_frame.isna()

data_frame.tail()

clean_data_frame = data_frame.dropna()

print(clean_data_frame.tail())

highest_starting_median_salary_loc = clean_data_frame["Starting Median Salary"].idxmax()
print(clean_data_frame["Undergraduate Major"].loc[highest_starting_median_salary_loc])

print(clean_data_frame["Undergraduate Major"].loc[clean_data_frame["Mid-Career Median Salary"].idxmax()])

print(clean_data_frame["Undergraduate Major"].loc[clean_data_frame["Starting Median Salary"].idxmin()])

print(clean_data_frame.loc[clean_data_frame["Mid-Career Median Salary"].idxmin()])

spread_col = clean_data_frame["Mid-Career 90th Percentile Salary"].subtract(clean_data_frame["Mid-Career 10th Percentile Salary"])
clean_data_frame.insert(1, "Spread", spread_col)
low_risk = clean_data_frame.sort_values("Spread")
low_risk[["Undergraduate Major", "Spread"]].head()

highest_potential = clean_data_frame[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].sort_values("Mid-Career 90th Percentile Salary", ascending=False).head()
print(highest_potential)

highest_risk = clean_data_frame[["Undergraduate Major", "Spread"]].sort_values("Spread", ascending=False).head()
print(highest_risk)

clean_data_frame.groupby("Group").count()

clean_data_frame.drop("Undergraduate Major", axis=1).groupby("Group").mean()