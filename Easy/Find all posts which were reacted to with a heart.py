'''
Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.
'''

# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.head()
heart = facebook_reactions[facebook_reactions['reaction'] == 'heart']['post_id']
result = pd.merge(heart, facebook_posts, on='post_id').drop_duplicates()
