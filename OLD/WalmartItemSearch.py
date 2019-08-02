from urllib.request import urlopen
import json 

# def walmart_search(query):
def walmart_search(query_this_item, API_KEY):
	url ='http://api.walmartlabs.com/v1/search?query='+ query_this_item + '&format=json&apiKey=' + API_KEY
	json_obj = urlopen(url)
	data =  json.load(json_obj)
	with open('WalmartData.txt', 'w') as outfile:
		json.dump(data, outfile)

def main():
	API_KEY = "qufjxk28t4su7mr8sgxhpd7n"
	## As Example
	item = "socks"
	walmart_search(item, API_KEY)
main()
