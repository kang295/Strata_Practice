'''
Find matching hosts and guests pairs in a way that they are both of the same gender and nationality.
Output the host id and the guest id of matched pair.
'''

# Import your libraries
import pandas as pd

# Start writing code
airbnb_hosts.head()
merged_df = pd.merge(airbnb_hosts, airbnb_guests, on=['nationality', 'gender'], how='left')
result = merged_df[['host_id', 'guest_id']].drop_duplicates()
