'''
Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.
'''

# Import your libraries
import pandas as pd

# Start writing code
db_employee.head()

merged_df = pd.merge(db_employee, db_dept, left_on='department_id', right_on='id', how='inner')
filtered_df = merged_df[merged_df['department'].isin(['marketing', 'engineering'])]
filtered_df = filtered_df.groupby('department')['salary'].max()
absolute_difference = abs(filtered_df['engineering'] - filtered_df['marketing'])
