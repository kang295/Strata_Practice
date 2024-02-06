'''
Find the last time each bike was in use. 
Output both the bike number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). 
Order the results by bikes that were most recently used.
'''
# Import your libraries
import pandas as pd

# Start writing code
dc_bikeshare_q1_2012.head()
df = dc_bikeshare_q1_2012
result = df.groupby('bike_number')['end_time'].max().to_frame('last_used').reset_index().sort_values(by='last_used', ascending = False)
