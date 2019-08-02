#!/usr/bin/env python3

# Import module support
import requests
import json
from urllib.request import urlopen
import ModifyData
import numpy as np
from multiprocessing import Process, Manager, Value

def queryAmazonData(item, amount):
	accesskey = '3rrafvvsoe7ps85k5hk86pdqils2kjipsthi10fsdfuh0sol16dr2vbgqta13fif'



	return_list =[];
	manager = Manager()
	return_item_count_man = manager.Value('i', 0)
	return_list_man = manager.list(return_list)


	page = 0
	perPage = 100
	

	while True:


		####get 100 asins
		request_type = 'query'
		#####"current_NEW_lte": Integer,
		#####"current_NEW_gte": Integer,
		#####"current_USED_lte": Integer,
		#####"current_USED_gte": Integer,
		#####"current_SALES_lte": Integer,
		#####"current_SALES_gte": Integer,
		#####"current_RATING_lte": Integer,
		#####"current_RATING_gte": Integer,
		temp = {
        	"title": item,
        	"productType": [
        	    0
        	],
        	"perPage": perPage,
        	"page": page
    	}

		temp_json = json.dumps(temp)

		payloadProductFinder = {
			'key' : accesskey,
			'domain' : '6',
			'selection' : temp_json
		}
		#print('https://api.keepa.com/%s/?' % request_type, payloadProductFinder)

		#final data will be stored here because we need to call 20 asins per search
		final_data = []
		start_index = 0
		end_index = 20

		r =  requests.get('https://api.keepa.com/%s/?' % request_type, payloadProductFinder)
		data = r.json()
		asinList = data['asinList']
		#print(str(asinList))
		#print(type(asinList))
		#print()

		


		payloadProductRequest1 = {
			'key' : accesskey,
			'domain' : '6',
			'asin' : ','.join(asinList[0:20]),
			'rating' : '1',
			'offers' : '20'
		}
		p1 = Process(target = getAmazonItemDetails, args=(return_list_man,return_item_count_man, payloadProductRequest1))

		payloadProductRequest2 = {
			'key' : accesskey,
			'domain' : '6',
			'asin' : ','.join(asinList[20:40]),
			'rating' : '1',
			'offers' : '20'
		}
		p2 = Process(target = getAmazonItemDetails, args=(return_list_man,return_item_count_man, payloadProductRequest2))

		payloadProductRequest3 = {
			'key' : accesskey,
			'domain' : '6',
			'asin' : ','.join(asinList[40:60]),
			'rating' : '1',
			'offers' : '20'
		}
		p3 = Process(target = getAmazonItemDetails, args=(return_list_man,return_item_count_man, payloadProductRequest3))

		payloadProductRequest4 = {
			'key' : accesskey,
			'domain' : '6',
			'asin' : ','.join(asinList[60:80]),
			'rating' : '1',
			'offers' : '20'
		}
		p4 = Process(target = getAmazonItemDetails, args=(return_list_man,return_item_count_man, payloadProductRequest4))

		payloadProductRequest5 = {
			'key' : accesskey,
			'domain' : '6',
			'asin' : ','.join(asinList[80:100]),
			'rating' : '1',
			'offers' : '20'
		}
		p5 = Process(target = getAmazonItemDetails, args=(return_list_man,return_item_count_man, payloadProductRequest5))

		p1.start()
		p2.start()
		p3.start()
		p4.start()
		p5.start()
		
			
		p1.join()
		p2.join()
		p3.join()
		p4.join()
		p5.join()
		

		if (return_item_count_man.value >= amount):
			return_list = return_list_man[0:amount]
			break
		page += 1
		

	
	return(return_list)

def getAmazonItemDetails(return_list_man, return_item_count_man, payloadProductRequest):
	request_type = 'product'
	#print('https://api.keepa.com/%s/?' % request_type, payloadProductRequest)
	r =  requests.get('https://api.keepa.com/%s/?' % request_type, payloadProductRequest)
	final_data = (r.json()['products'])

	for product in final_data:
			#title  OK
			title = product['title']
			#print('title : ' + title) 
	
			#price OK
			if (type(product['offers']) == list):
				if 'offerCSV' in product['offers'][0]:
					price = product['offers'][0]['offerCSV'][-2]
			else:
				priceArray = product['csv'][1]
				#if priceArray is type [data, price]
				if (priceArray[-2] > 1000000):
					price = priceArray[-1]
				else:
					price = priceArray[-2]
			#print('price is : '+ str(price))
	
			#rating
			list_rating = (product['csv'][16])
			#rating same as reviews
			if list_rating is not None:
				rating = list_rating[-1]
			else:
				rating = 'nan'
			#print('rating is : ' + str(rating))
	
			#reviews
			list_review = (product['csv'][17])
			if list_review is not None:
				reviews_num = list_review[-1]
			else:
				reviews_num = 0
			#count of number of reviews in [data, # of reviews, date, # of reviews] in ascenting # of reviews
	
			#stock
			stock = 0
			list_offers = product['offers']
			if list_offers is not None:
				for individual_offer in list_offers:
					if 'stockCSV' in individual_offer:
						stock += individual_offer['stockCSV'][-1]
						
			brand = " "
			if 'brand' in product:
				brand = product['brand']
	
			#append the data to the dictionary
			if not (stock == 0 or price < 0 or price > 1000000):
				#make it to dollar.cent
				price = price/100
				return_list_man.append({'name':title,'price':price,'rating':rating,'reviews':reviews_num,'stock':stock,'brand':brand})
				return_item_count_man.value += 1;


def queryWeatherData(location, unitType):
	url = 'http://api.openweathermap.org/data/2.5/weather'
	appID = '43644e4e8baf019c3a323353f3b594ee'
	modeType = 'json'
	payload = {
		'q' : location,
		'mode' : modeType,
		'units' : unitType,
		'appid' : appID
	}
		
	r = requests.get(url, params=payload)
	return r.json()
	
##########5.23
def queryEbayData(item, amount):
	global data
	url = 'https://api.ebay.com/buy/browse/v1/item_summary/search'
	appAccessToken = getEbayAuth()
	headers = {
		'Authorization' : 'Bearer ' + appAccessToken
	}
	##for filtering, you can use 'filter' : 'price:[10 .. 50]'
	##filter=returnsAccepted:true ????
	payload = {
		'q' : item,
		'limit' : amount
	}
	
	r = requests.get(url, headers=headers, params=payload)
	data = r.json()['itemSummaries']
	######Manager to declare variable that will be shared among all processors
	manager = Manager()

	#d with type list, euqal to data 
	d = manager.list(data)
	

	#10 processors;;;
	jobs_per_proc = len(d)//10

	#declaring processes
	start_index = 0
	end_index = jobs_per_proc
	#p1
	p1 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p2 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p3 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p4 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p5 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p6 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p7 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p8 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	p9 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))
	start_index+=jobs_per_proc
	end_index+=jobs_per_proc
	#if there are items that are not covered
	if (end_index != len(d)):
		end_index = len(d)
	p10 = Process(target = getEbayItemDetails, args=(appAccessToken, d, start_index, end_index))

	#starting process
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p6.start()
	p7.start()
	p8.start()
	p9.start()
	p10.start()

	#joining process
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	p7.join()
	p8.join()
	p9.join()
	p10.join()
	#data = pool.apply(getEbayItemDetails, args=(appAccessToken, data))

	#set data to the data that was shared among processors
	data = d

	
	
	return data
	
def getEbayAuth():
	url = 'https://api.ebay.com/identity/v1/oauth2/token'
	b64_encoded_oath_cred = 'Umlja2VzaE0tTWFya2V0SWQtUFJELTQzOTNjYWI3ZC1lNWE2ZmZkZjpQUkQtMzkzY2FiN2Q4MWY0LTkzMjktNGEyNS05Y2RhLTFhNGY='
	headers = {
		'Content-Type' : 'application/x-www-form-urlencoded',
		'Authorization' : 'Basic ' + b64_encoded_oath_cred
	}
	payload = {
		'grant_type' : 'client_credentials',
		'scope' : 'https://api.ebay.com/oauth/api_scope'
	}
	
	r = requests.post(url, headers=headers, data=payload)
	return r.json()['access_token']

def getEbayItemDetails(appAccessToken, d, start_index, end_index):	
	#headers needs to be declared once
	headers = {
		'Authorization' : 'Bearer ' + appAccessToken
	}
	
	#for i in range start_index to end_index
	for i in range (start_index, end_index):
		url = 'https://api.ebay.com/buy/browse/v1/item/' + d[i]['itemId']
		r = requests.get(url, headers=headers)
		data = r.json()
		data = ModifyData.reduceEbay(data)
		
		#modify the array that is shared along processors
		d[i] = data

	
	
#return value has estimatedAvailableQuantity, estimatedSoldQuantity, topRatedBuyingExperience
def queryWalmartData(query_this_item, numPages):
	API_KEY = "qufjxk28t4su7mr8sgxhpd7n"
	data = []
	temp_keyword=''
	#breaking spaces
	a = query_this_item.split(' ')
	for i in a:
		temp_keyword+=i
		temp_keyword+='%20'

	query_this_item = temp_keyword
	for page in range(1,numPages+1):
		url = 'http://api.walmartlabs.com/v1/search?query='+ query_this_item + '&format=json&start=' + str(page) + '&responseGroup=full' + '&apiKey=' + API_KEY
		json_obj = urlopen(url)
		response =  json.load(json_obj)
		data += response['items']
 
		
	#	checkItemID = data[key]['itemId']
	#		queryWalmartReviews(data, key, checkItemID, API_KEY)
	#	except:
	#		data[key]['numReviews'] = 0

	return data
	
def queryWalmartReviews(data, key, itemID, API_KEY):
	myurl = 'http://api.walmartlabs.com/v1/reviews/'+ str(itemID) + '?format=json&apiKey=' + API_KEY
	myjson_obj = urlopen(myurl)
	mydata =  json.load(myjson_obj)
	checkID = mydata['itemId']

	if checkID == itemID:
		data[key]['numReviews'] = mydata['reviewStatistics']['totalReviewCount']
	

if __name__ == "__main__":	
	
	#print(queryWeatherData("Hamilton,CA", "metric"))
	
	#ebayData = queryAmazonData('drone', 40)
	#print(ebayData)
	data = queryWalmartData('socks',3)
	ebayData = ModifyData.reduceWalmart(data)
	print(ebayData)
	
	#data = queryWalmartData('socks',2)
	#print(len(data))

	#data = queryAmazonData("drone", 2)
	#print(data)
	
	#print("FIN")
	