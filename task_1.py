import csv
import pandas as pd
import requests, os
import datetime
# for this task I have to do..
# 1. at first I have check its pick time, is it in between 6 AM to less than 12 PM
# 2. secondly I have to groupby with source station name, code
# 3. thirdly I have to count rows for count trips
# 4. forthly I have to return top 5 data

# if it is from database I have to this query..
# " select source_station_name, source_station_code, count(source_station_name) AS trips from bicycle_trips where picup_time >= 6 Am and pickup_time < 12 PM group by source_station_name, source_station_code order by trips desc limit 5"

file_url = 'https://press.radiocut.fm/bicycle-travels-jan-2018.csv'
filename = 'bicycle-travels-jan-2018.csv'
def download_and_processing_file(url, filename):
	# check if file already exists
	if not os.path.isfile(filename):
		print('downloading file..')
		response = requests.get(url)
		# check if the response i ok (200)
		if response.status_code == 200:
			# open file and write the content
			with open(filename, 'wb') as file:
				for chunk in response:
					file.write(chunk)
	else:
		print('file exists..')

	print('Top five source stations: ')
	
	df = pd.read_csv(filename)
	group_data = df.groupby('source_station_name')
	# print(group_data)
	for source_station_name, source_station_name_df in group_data:

	# data_dict = data.to_dict()

	# for val in data_dict.items(): 
	# 	print(val)

	# for source_station_name, source_station_code in data.groupby(['source_station_name','source_station_code']):
	# 	print('source station name : ')
	# 	print(source_station_name)


download_and_processing_file(file_url,filename)