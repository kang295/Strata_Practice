'''
Find order details made by Jill and Eva.
Consider the Jill and Eva as first names of customers.
Output the order date, details and cost along with the first name.
Order records based on the customer id in ascending order.
'''

# Import your libraries
import pandas as pd

# Start writing code
customers.head()
merged_df = pd.merge(customers, orders, left_on='id', right_on='cust_id', how='inner')
only = merged_df[(merged_df['first_name'] == 'Jill') | (merged_df['first_name'] == 'Eva')]
only[['first_name','order_date', 'order_details', 'total_order_cost']]

or

merge = pd.merge(customers, orders, left_on="id", right_on='cust_id')
cust = ['Jill', 'Eva']
result = merge[merge['first_name'].isin(cust)][['first_name', 'order_date','order_details','total_order_cost']]
