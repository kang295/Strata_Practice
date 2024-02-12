'''
Find songs that have ranked in the top position. Output the track name and the number of times it ranked at the top. 
Sort your records by the number of times the song was in the top position in descending order.
'''

# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.head()
shorted = spotify_worldwide_daily_song_ranking
position = shorted[shorted['position'] == 1]
position.groupby('trackname').size().reset_index(name='times_top1').sort_values('times_top1',ascending = False)
