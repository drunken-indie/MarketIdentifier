import APIScript
import ModifyData

def calcRank(data):
	brands = []
	countFiveStarListings = 0
	countGoodListings = 0
	countBadListingsWithSales = 0
	countBadListings = 0
	
	#Set up variables for rating
	for i in range(0, len(data)):
		brands = addBrand(brands, data[i]['brand'])
		
		if float(data[i]['rating']) == 5:
			countFiveStarListings += 1
		
		if float(data[i]['rating']) >= 4 and float(data[i]['reviews']) >= 500:
			countGoodListings += 1
		
		if float(data[i]['rating']) <= 100 and float(data[i]['sales']) >= 300:
			countBadListingsWithSales += 1
		
		if float(data[i]['rating']) <= 100 and float(data[i]['rating']) <= 5 and float(data[i]['sales']) <= 300:
			countBadListings += 1
		
	#Calculate rating
	if checkMonopoly(brands):						#If 3 or more results are the same brand = 4/4 #Monopoly Type Market
		return 4
	elif countFiveStarListings >= 10:				#If 10 or more listings have a 5 star rating = 4/4 #No room For differentiation/Too competitive
		return 4
	elif countGoodListings >= 5: 					#If 5 or more listings have a review count of 500 AND average rating is > 4 = 4/4 #Established market/Too competitive
		return 4
	elif countBadListingsWithSales == len(data):	#If < 5 star AND sales > 300 = 1/4
		return 1
	elif countBadListings == len(data):				#If < 5 star rating AND review count < 100 AND sales < 300  = 3/4 # Not enough demand/Low ROI
		return 3
	else:
		return 2

	
	
def addBrand(brands, entry):
	dict = {}

	if len(brands) == 0:
		dict['brandName'] = entry
		dict['count'] = 1
		brands += [dict]
	else:
		found = False
		for i in range(0, len(brands)):
			if brands[i]['brandName'] == entry:
				brands[i]['count'] = brands[i]['count'] + 1
				found = True
				
		if found == False:		
			dict['brandName'] = entry
			dict['count'] = 1
			brands = brands + [dict]
	
	return brands

def checkMonopoly(brands):
	
	for brand in brands:
		if brand['count'] >= 3:
			return True
	
	return False
	
if __name__ == "__main__":
	print("////////////////  MIRANK main function start  ////////////////")
	#EBAY TEST
	#data = APIScript.queryEbayData('drone', 40)
	#print(calcRank(data))
	
	#WALMART TEST
	#data = APIScript.queryWalmartData('drone', 1)
	#data = ModifyData.reduceWalmart(data)
	
	#AMAZON TEST
	data = APIScript.queryAmazonData('drone', 10)
	
	for i in data[0]:
		print(i)
		print(data[0][i])
		
	