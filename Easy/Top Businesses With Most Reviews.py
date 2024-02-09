'''
Find the top 5 businesses with most reviews. Assume that each row has a unique business_id such that the total reviews for each business is listed on each row. 
Output the business name along with the total number of reviews and order your results by the total reviews in descending order.
'''

# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()
filtered = yelp_business['review_count'].sort_values(ascending = False).head(5)

joined = pd.merge(yelp_business, filtered, on='review_count')
joined[['name', 'review_count']].sort_values(by = 'review_count', ascending=False)
