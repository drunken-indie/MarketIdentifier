import APIScript
import ModifyData

def calcScore(data):
	if 'sales' in data:
		return calcScoreEbay(data)
	else:
		return calcScoreAmazonWalmart(data)

def calcScoreAmazonWalmart(data):
	brands = []
	
	HighRating = 0
	HighReview = 0
	
	TotalPrice = 0
	TotalRating = 0
	TotalReviews = 0
	
	NumItems = len(data)
	Monopoly = False
	AvgPrice = 0
	AvgRating = 0
	AvgReviews = 0
	
	for i in range(0, len(data)):

		brands = addBrand(brands, data[i]['brand'], data[i]['rating'])
	
		TotalPrice += data[i]['price']
		TotalRating += data[i]['rating']
		TotalReviews += data[i]['reviews']
		
		if data[i]['rating'] >= 5.0:
			HighRating += 1
		
		if data[i]['reviews'] >= 500:
			HighReview += 1
		
		
	for brand in brands:
		if brand['count'] >= 3:
			Monopoly = True
	
	AvgPrice = TotalPrice / NumItems
	AvgRating = TotalRating / NumItems
	AvgReviews = TotalReviews / NumItems
	
	if AvgPrice < 10:
		return 4
	elif HighRating >= 5:
		return 4
	elif HighReview >= 5 and AvgRating > 4.0:
		return 4
	elif Monopoly == 5:
		return 4
	elif AvgPrice > 25 and AvgRating < 4.0:
		return 3
	elif AvgRating < 5.0 and AvgReviews < 100:
		return 2
	elif AvgPrice < 25 and AvgReviews < 100:
		return 1
	else:
		return 2
	
def calcScoreEbay(data):
	brands = []
	
	HighReview = 0
	HighRating = 0
	
	TotalSales = 0
	TotalRating = 0
	TotalReviews = 0
	
	NumItems = len(data)
	BrandRepetition = 0
	Monopoly = False
	AvgSales = 0
	AvgRating = 0
	AvgReviews = 0
	
	#Setup Variables
	for i in range(0, len(data)):

		brands = addBrand(brands, data[i]['brand'], data[i]['rating'])
		
		if data[i]['reviews'] >= 300:
			HighReview += 1
		
		if data[i]['rating'] >= 4.5:
			HighRating += 1
		
		TotalSales += data[i]['sales']
		TotalRating += data[i]['rating']
		TotalReviews += data[i]['reviews']
			
	for brand in brands:
		if brand['count'] >= 3:
			Monopoly = True
		elif brand['count'] >= 2:
			BrandRepetition += 1
	
	AvgSales = TotalSales / NumItems
	AvgRating = TotalRating / NumItems
	AvgReviews = TotalReviews / NumItems
	
	#Calculate Score
	if HighReview > 3:
		return 4
	elif HighRating > 3:
		return 4
	elif AvgSales > 500 and AvgRating > 4.5:
		return 4
	elif AvgSales > 500 and AvgReviews > 100:
		return 4
	elif Monopoly:
		return 4
	elif AvgRating < 5.0 and BrandRepetition < 5:
		return 3
	elif AvgReviews < 100 and AvgRating < 4.5:
		return 2
	elif AvgSales > 200 and AvgRating < 5.0:
		return 1
	elif AvgSales > 200 and AvgReviews < 100:
		return 1
	elif AvgSales > 200 and BrandRepetition < 3:
		return 1
	else:
		return 2
	
	
def addBrand(brands, entry, rating):
	dict = {}

	if len(brands) == 0:
		dict['brandName'] = entry
		dict['count'] = 1
		dict['rating'] = [rating]
		brands += [dict]
		return brands
	else:
		found = False
		for i in range(0, len(brands)):
			if brands[i]['brandName'] == entry:
				brands[i]['count'] = brands[i]['count'] + 1
				brands[i]['rating'].append(rating)
				return brands

	dict['brandName'] = entry
	dict['count'] = 1
	dict['rating']= [rating]
	brands = brands + [dict]
	return brands	
	
if __name__ == "__main__":
	pass
	#EBAY TEST
	data = APIScript.queryEbayData('LED Lights', 40)
	
	#WALMART TEST
	#data = APIScript.queryWalmartData('drone', 2)
	#data = ModifyData.reduceWalmart(data)
	
	#AMAZON TEST
	#data = APIScript.queryAmazonData('drone', 10)
	
	for item in data:
		print(item)
	
	print(calcScore(data))

	
	'''
	#TEST DATA
	data = []
	data.append({'name':'Name A','price':100,'rating':3,'reviews':100,'brand':'Brand A'})
	data.append({'name':'Name B','price':100,'rating':3,'reviews':100,'brand':'Brand A'})
	data.append({'name':'Name C','price':100,'rating':3,'reviews':100,'brand':'Brand A'})
	data.append({'name':'Name D','price':100,'rating':5,'reviews':100,'brand':'Brand D'})	
	data.append({'name':'Name E','price':100,'rating':5,'reviews':100,'brand':'Brand E'})
	data.append({'name':'Name F','price':100,'rating':5,'reviews':100,'brand':'Brand F'})
	data.append({'name':'Name G','price':100,'rating':5,'reviews':100,'brand':'Brand G'})
	data.append({'name':'Name H','price':100,'rating':5,'reviews':100,'brand':'Brand H'})
	data.append({'name':'Name I','price':100,'rating':5,'reviews':100,'brand':'Brand I'})
	data.append({'name':'Name J','price':100,'rating':5,'reviews':100,'brand':'Brand J'})
	data.append({'name':'Name K','price':100,'rating':5,'reviews':100,'brand':'Brand K'})
	data.append({'name':'Name L','price':100,'rating':5,'reviews':100,'brand':'Brand L'})
	data.append({'name':'Name M','price':100,'rating':5,'reviews':100,'brand':'Brand M'})
	
	print("////////////////////////////////")

	print(calcScore(data))
	'''
	
	
	