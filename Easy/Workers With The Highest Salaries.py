'''
You have been asked to find the job titles of the highest-paid employees.
Your output should include the highest-paid title or multiple titles with the same salary.
'''

import pandas as pd
import numpy as np

worker.head()

output = worker[worker['salary'] == worker['salary'].max()]
result = pd.merge(output, title, left_on='worker_id', right_on='worker_ref_id', how='inner')
