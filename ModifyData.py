#!/usr/bin/env python3
import json
import APIScript as api
def reduceEbay(data):
	newDict = {}
	setDict(data, newDict, 'title', 'name', ' ')
	setDict(data, newDict, 'price', 'price', '0.00')
	setDict(data, newDict, 'primaryProductReviewRating', 'rating', '0')
	setDict(data, newDict, 'primaryProductReviewRating', 'reviews', '0')
	setDict(data, newDict, 'estimatedAvailabilities', 'stock', 'N/A')
	setDict(data, newDict, 'estimatedAvailabilities', 'sales', '0')
	setDict(data, newDict, 'brand', 'brand', ' ')

	newDict['price'] = newDict['price']['value']
	###fixed when default value is inserted in setDict, it will not produce an error
	if ('averageRating' in newDict['rating']):
		newDict['rating'] = newDict['rating']['averageRating']
	
	if ('reviewCount' in newDict['reviews']):
		newDict['reviews'] = newDict['reviews']['reviewCount']
	
	if ('availabilityThreshold' in newDict['stock'][0]):
		newDict['stock'] = "> "+str(newDict['stock'][0]['availabilityThreshold'])
	elif ('estimatedAvailabilityStatus' in newDict['stock'][0]):
		newDict['stock'] = newDict['stock'][0]['estimatedAvailabilityStatus']
	
	if ('estimatedSoldQuantity' in newDict['sales'][0]):
		newDict['sales'] = newDict['sales'][0]['estimatedSoldQuantity']
	
	newDict['price'] = float(newDict['price'])
	newDict['rating'] = float(newDict['rating'])
	newDict['reviews'] = float(newDict['reviews'])
	
	data = newDict
	return data
	
def reduceAmazon():
	print("reduceAmazon function")

def reduceWalmart(data):	
	#set new key names and default values
	for i in range(0, len(data)):
		newDict = {}
		setDict(data[i], newDict, 'name', 'name', ' ')
		setDict(data[i], newDict, 'salePrice', 'price', '0.00')
		setDict(data[i], newDict, 'customerRating', 'rating', '0')
		setDict(data[i], newDict, 'numReviews', 'reviews', '0')
		setDict(data[i], newDict, 'stock', 'stock', '0.00')
		setDict(data[i], newDict, 'brandName', 'brand', ' ')
		
		newDict['price'] = float(newDict['price'])
		newDict['rating'] = float(newDict['rating'])
		newDict['reviews'] = float(newDict['reviews'])
		
		data[i] = newDict
	return data
	
def setDict(oldDict, newDict, oldKey, newKey, defaultValue):
		if oldKey in oldDict:
			newDict[newKey] = oldDict[oldKey]
		else:
			newDict[newKey] = defaultValue

def testPrint(data):
	for i in range(0,len(data)):
		print(i, data[i]['name'])
	#for keys in data[0]:
	#	print(keys)
		
def createEstimatedSalesData():
	print("createEstimatedSalesData function")


if __name__ == "__main__":
	'''
	#test with raw walmart data
	f=open("walmart_raw.txt", "r")
	if f.mode == 'r':
		contents = f.read()
	data = json.loads(contents)
	data = data['items']
	
	data = reduceWalmart(data)
	print(data)
	'''
	data = reduceEbay(api.queryEbayData('drone', 20))

	