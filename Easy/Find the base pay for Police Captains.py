'''
Find the base pay for Police Captains.
Output the employee name along with the corresponding base pay.
'''

# Import your libraries
import pandas as pd

# Start writing code
sf_public_salaries.head()
title = sf_public_salaries[sf_public_salaries['jobtitle'] == 'CAPTAIN III (POLICE DEPARTMENT)']
title[['employeename', 'basepay']]
