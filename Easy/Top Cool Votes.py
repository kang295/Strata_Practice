'''
Find the review_text that received the highest number of  'cool' votes.
Output the business name along with the review text with the highest numbef of 'cool' votes.
'''

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_reviews
result = df[df['cool'] == df['cool'].max()][['business_name', 'review_text']]
