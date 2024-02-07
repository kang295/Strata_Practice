'''
Find the number of rows for each review score earned by 'Hotel Arena'. 
Output the hotel name (which should be 'Hotel Arena'), review score along with the corresponding number of rows with that score for the specified hotel.
'''

# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews.head()
arena = hotel_reviews[hotel_reviews['hotel_name'] == 'Hotel Arena']
result = arena.groupby(['reviewer_score', 'hotel_name']).size().reset_index(name = "n_reviews")
