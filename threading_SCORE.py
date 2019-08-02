from threading import Thread
# global variables for sta=oring scores from all websites
eBay_SCORE    = 0
walmart_SCORE = 0
amazon_SCORE  = 0
return_DATA   = ''

def Amazon_scoreEbay(search_key):
    eBay_SCORE=score.calcScore(script.queryEbayData(search_key, 40))

def Amazon_scoreWalmart(search_key):
    walmart_SCORE=score.calcScore(modify.reduceWalmart(script.queryWalmartData(search_key, 3)))

def Amazon_scoreAmazon(search_key):
    return_DATA=script.queryAmazonData(search_key, 40)
    amazon_SCORE=score.calcScore(return_data)

def eBay_scoreEbay(search_key):
    return_DATA=script.queryEbayData(search_key, 40)
    eBay_SCORE=score.calcScore(return_data)

def eBay_scoreWalmart(search_key):
    walmart_SCORE=score.calcScore(modify.reduceWalmart(script.queryWalmartData(search_key, 3)))

def eBay_scoreAmazon(search_key):
    amazon_SCORE=score.calcScore(script.queryAmazonData(search_key, 40))

def Walmart_scoreEbay(search_key):
    eBay_SCORE=score.calcScore(script.queryEbayData(search_key, 40))

def Walmart_scoreWalmart(search_key):
    return_DATA=modify.reduceWalmart(script.queryWalmartData(search_key, 3))
    walmart_SCORE=score.calcScore(return_data)

def Walmart_scoreAmazon(search_key):
    amazon_SCORE=score.calcScore(script.queryAmazonData(search_key, 40))

def search(search_key, search_from):
    return_data_list=[]
    threads = []

    if (search_from=='amazon'):
        threads.append(Thread(target=Amazon_scoreEbay, args = (search,)))
        threads.append(Thread(target=Amazon_scoreWalmart, args = (search_key,)))
        threads.append(Thread(target=Amazon_scoreAmazon, args = (search_key,)))

        # starts 3 threads 
        for thread in threads:
            thread.start()
        # joins all the three threads
        for thread in threads:
            thread.join()
        #print('amazon')

    elif (search_from=='ebay'):
        threads.append(Thread(target=eBay_scoreEbay, args = (search,)))
        threads.append(Thread(target=eBay_scoreWalmart, args = (search_key,)))
        threads.append(Thread(target=eBay_scoreAmazon, args = (search_key,)))

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        #print('ebay')
    elif (search_from=='walmart'):
        threads.append(Thread(target=Walmart_scoreEbay, args = (search,)))
        threads.append(Thread(target=Walmart_scoreWalmart, args = (search_key,)))
        threads.append(Thread(target=Walmart_scoreAmazon, args = (search_key,)))

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        #print('walmart')
    return_data_list.append(return_DATA)
    return_data_list.append(str(amazon_SCORE))
    return_data_list.append(str(eBay_SCORE))
    return_data_list.append(str(walmart_SCORE))
    return (return_data_list)
