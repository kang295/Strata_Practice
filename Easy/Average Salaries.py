'''
Compare each employee's salary with the average salary of the corresponding department.
Output the department, first name, and salary of employees along with the average salary of that department.
'''

# Import your libraries
import pandas as pd

# Start writing code
employee.head()
df = employee.groupby('department')['salary'].mean().reset_index(name='avg_salary')
merged = pd.merge(employee, df, on='department', how='left')
merged[['department', 'first_name', 'salary', 'avg_salary']]
