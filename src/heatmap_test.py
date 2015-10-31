from test import *
import heatmap

# outputs the heatmap for a specific year
def crime_heatmap_year(csv_filename):
	d = csv_to_dict(csv_filename)
	ll = get_location_list(d)

	hm = heatmap.Heatmap()
	hm.heatmap(ll)
	hm.saveKML('../output/data.kml')

if __name__ == '__main__':
	csv_filename = '../data/2013_Crime_Data.csv'
	crime_heatmap_year(csv_filename)