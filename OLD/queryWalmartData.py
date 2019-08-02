from urllib.request import urlopen
import json 

###
## SAMPLE QUERIES FOR "dryer"
## itemID = 55050217

## Reviews API call URL 
#http://api.walmartlabs.com/v1/reviews/55050217?format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n
## url = 'http://api.walmartlabs.com/v1/reviews/'+ str(itemID) + '?format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n'
##
## LookUp API Call URL
#http://api.walmartlabs.com/v1/items/55050217?format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n
## URL = 'http://api.walmartlabs.com/v1/items/' + str(itemID) +'?format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n'
##
## Search API Call URL 
#http://api.walmartlabs.com/v1/search?query=dryer&format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n
## url = 'http://api.walmartlabs.com/v1/search?query=' + search_item + '&format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n'
##
####

# price, rating, number of reviews
class WalmartQuery:
	def __init__(self):
		self.itemID = 1
		self.name = ""
		self.price = 1
		self.category = ""
		self.rating = ""
		self.numberOfReviews = 1
		self.numberOfResult = 0
		self.stock = ""

		## stores a list of dictionaries
		## e.g Sample Template => [{"]'itemID': 0000,'name': "xyz", 'salePrice':2.0,'categoryPath':"asdf",
		## 							'customerRating':'2.5','numReviews':'1.4','stock':'Available'}]
		self.relevantProductFields = [] 

	def searchUsefulFields(self):
		search_item = 'fan' ## try a different item to search 
		url = 'http://api.walmartlabs.com/v1/search?query=' + search_item + '&format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n'
		json_obj = urlopen(url)
		data =  json.load(json_obj)

		for key in data:
			# reviews is a list of dictionaries, and itemReviews is a list of every reviews 
			# in the reviews dictionary. 
			if key == "items":
				self.numberOfResult = data['numItems'] ## sets the field for number of result for our search
				for i in range(len(data[key])):
					dictTemplate = {"itemId":0, "name":"", "salePrice":0, "categoryPath":"","customerRating":"","numReviews":0,"stock":""}
					##print("The ith iteration is " + str(i))
					self.itemID = data[key][i]['itemId']
					self.userName =  data[key][i]['name']
					self.price = data[key][i]['salePrice']
					self.category =  data[key][i]['categoryPath']
					self.rating = data[key][i]['customerRating']
					#self.numberOfReviews =  data[key][i]['numReviews']
					self.stock =  data[key][i]['stock']
					dictTemplate['itemId'] = self.itemID 
					dictTemplate['name'] = self.userName
					dictTemplate['salePrice'] = self.price 
					dictTemplate['categoryPath'] = self.category
					dictTemplate['customerRating'] = self.rating
					dictTemplate['stock'] = self.stock
					self.relevantProductFields.append(dictTemplate) ## by now we should have entered a pair of 
																 ## name and itemID into the list
		for key in range(len(self.relevantProductFields)):
			checkItemID = self.relevantProductFields[key]['itemId']
			self.setNumberOfReviews(key, checkItemID)

	## now we enter the retrived data into the productNameandID variable to store them 
	def getNumberOfResults(self):
		return self.numberOfResult

	## index must be within the range of the returned result from the search query
	def getItemName(self, index):
		return self.relevantProductFields[index]['name']# item Name which will be searched for

	## this method will be used for other queries like LOOKUP API & Reviews API  
	def getID(self, index):
		return self.relevantProductFields[index]['itemId']

	## will be done using the reviews API
	def getTotalNumberOfReviews(self, index):
		return self.relevantProductFields[index]['numReviews']

	## we update the numReviews field in every dictinary of our list
	## this fucntion was made cause some reviews weren't included for certain products 
	## from the search API. So I implemented the the Reviews API to get the number of 
	## reviews for the respective field order to fill in the missing reviews for products. 
	def setNumberOfReviews(self, key, itemID):
		myurl = 'http://api.walmartlabs.com/v1/reviews/'+ str(itemID) + '?format=json&apiKey=qufjxk28t4su7mr8sgxhpd7n'
		myjson_obj = urlopen(myurl)
		mydata =  json.load(myjson_obj)
		checkID = mydata['itemId']

		if checkID == itemID:
			self.relevantProductFields[key]['numReviews'] = mydata['reviewStatistics']['totalReviewCount']

def main():

	## must call searchUsefulFields() in order to store data results
	result = WalmartQuery()
	result.searchUsefulFields()
	print("")
	print(result.relevantProductFields)
	print(result.getNumberOfResults())
	print(result.getID(2))
	print(result.getItemName(2))
	print(result.getTotalNumberOfReviews(2))
main()