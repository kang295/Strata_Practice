'''
We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. 
Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.
'''

# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head(3)
result = ms_employee_salary.groupby(['id', 'first_name', 'last_name', 'department_id'])['salary'].max().reset_index().sort_values('id')
