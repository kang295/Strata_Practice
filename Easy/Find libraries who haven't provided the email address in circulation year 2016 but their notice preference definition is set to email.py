'''
Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email.
Output the library code.
'''

# Import your libraries
import pandas as pd

# Start writing code
library_usage.head()
filtered = library_usage[(library_usage['notice_preference_definition'] == 'email') & (library_usage['provided_email_address'] == False) & (library_usage['circulation_active_year'] == 2016)]
filtered[['home_library_code']].drop_duplicates()
