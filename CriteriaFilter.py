#!/usr/bin/env python3

import json

#def filterData(data, ratingLow, ratingHigh, priceLow, priceHigh, numReviewsLow, numReviewHigh, numSaleslow, numSalesHigh):
def filterData(data, ratingLow, ratingHigh):
	#rating
	quickSort(data, 'rating', 0, len(data)-1)
	cutoffLow = binarySearchLow(data, 'rating', ratingLow)
	cutoffHigh = binarySearchHigh(data, 'rating', ratingHigh)	
	data = data[cutoffLow+1:cutoffHigh]
	
	return data
	
def quickSort(data, key, first, last):
	if first<last:
		splitpoint = partition(data, key, first, last)
		quickSort(data, key, first, splitpoint-1)
		quickSort(data, key, splitpoint+1, last)


def partition(data, key, first, last):
	pivotvalue = data[first][key]
	
	leftmark = first+1
	rightmark = last
	
	done = False
	while not done:
		while leftmark <= rightmark and data[leftmark][key] <= pivotvalue:
			leftmark = leftmark + 1
			
		while leftmark <= rightmark and pivotvalue <= data[rightmark][key]:
			rightmark = rightmark -1
			
		if leftmark > rightmark:
			done = True
		else:
			temp = data[leftmark]
			data[leftmark] = data[rightmark]
			data[rightmark] = temp
			
	temp = data[first]
	data[first] = data[rightmark]
	data[rightmark] = temp
	
	return rightmark
	
	
def binarySearchLow(data, key, value):
	if data[0][key] >= value:
		return -1
	
	low = 0
	high = len(data) - 1
	
	while low <= high:
		mid = low + (high - low)//2
		
		if data[mid][key] >= value:
			high = mid - 1
		else:
			low = mid + 1
	
	return low - 1
	
def binarySearchHigh(data, key, value):
	last = len(data) - 1
	
	if data[last][key] <= value:
		return last + 1
		
	
	low = 0
	high = len(data) - 1
	
	while low <= high:
		mid = low + (high - low)//2
		
		if data[mid][key] <= value:
			low = mid + 1
		else:
			high = mid - 1
	
	return high + 1
				
def reduceRows(data):
	print("reduceRows function")
	
	
def testPrint(data):
	for i in range(0, len(data)):
		print(i, data[i]['name'], data[i]['price'], data[i]['rating'], data[i]['reviews'], data[i]['stock'])

if __name__ == "__main__":
	f=open("walmart_reduced.txt", "r")
	if f.mode == 'r':
		contents = f.read()
	data = json.loads(contents)	
	data = data['data']
	
	data = filterData(data, "4.0" , "5.0")
	testPrint(data)