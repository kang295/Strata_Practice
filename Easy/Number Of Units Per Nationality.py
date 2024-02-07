'''
Find the number of apartments per nationality that are owned by people under 30 years old.
Output the nationality along with the number of apartments.
Sort records by the apartments count in descending order.
'''

# Import your libraries
import pandas as pd

# Start writing code
merged = pd.merge(airbnb_units, airbnb_hosts, on="host_id")
merged = merged[(merged['age'] < 30) & (merged['unit_type'] == "Apartment")]
merged.groupby('nationality')['unit_id'].nunique().reset_index(name="apartment_count").sort_values('apartment_count')
