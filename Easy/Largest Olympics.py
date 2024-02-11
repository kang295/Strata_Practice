'''
Find the Olympics with the highest number of athletes. The Olympics game is a combination of the year and the season, and is found in the 'games' column. 
Output the Olympics along with the corresponding number of athletes.
'''

# Import your libraries
import pandas as pd

# Start writing code
olympics_athletes_events.head()
result = olympics_athletes_events.groupby(['games'])['name'].nunique().reset_index(name='athletes_count').sort_values('athletes_count', ascending=False)
result[result['athletes_count'] == result['athletes_count'].max()]
