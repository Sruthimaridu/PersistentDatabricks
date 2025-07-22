import pandas as pd
s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)

# ------------------ 2. DATAFRAME ------------------
data = {
    "Name": ["sruthi", "surya", "deepu"],
    "Age": [22, 25, 30],
    "Department": ["IT", "HR", "Finance"]
}
df1 = pd.DataFrame(data)
print(df1)

'''# ------------------ 3. READING FILES ------------------
df = pd.read_csv('data.csv')
print("Data from CSV:\n", df)

df.to_excel('output.xlsx', index=False)
print("Saved to output.xlsx")

df_excel = pd.read_excel('output.xlsx')
print("Data from Excel:\n", df_excel)

# ------------------ 4. DATA EXPLORATION ------------------

print("First 2 rows:\n", df.head(2))
print("Last 2 rows:\n", df.tail(2))
print("Summary Info:")
df.info()
print("\nStatistics Summary:\n", df.describe())

# ------------------ 5. INDEXING & FILTERING ------------------

print("Access Salary column:\n", df['Salary'])
print("Rows where Department is IT:\n", df[df['Department'] == 'IT'])

# ------------------ 6. MODIFYING DATA ------------------

df['Bonus'] = df['Salary'] * 0.10
print("After Adding Bonus Column:\n", df)

df.loc[df['Name'] == 'Sruthi', 'Salary'] = 52000
print("After Updating Sruthi's Salary:\n", df)

df = df.drop(columns=['Bonus'])
print("After Dropping Bonus Column:\n", df)

# ------------------ 7. SORTING & GROUPING ------------------

print("Sorted by Salary:\n", df.sort_values('Salary', ascending=False))

print("\nGrouped by Department:\n", df.groupby('Department')['Salary'].mean())

# ------------------ 8. EXPORTING DATA ------------------

df.to_csv('updated_data.csv', index=False)
print("Saved updated data to updated_data.csv")'''
