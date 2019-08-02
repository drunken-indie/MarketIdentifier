#!/usr/bin/env python
#pip install websockets
#usage : python WebServer.py

# WS server example
import MIScore as score
import APIScript as script
import ModifyData as modify
import asyncio
import websockets
import logging
import json
from multiprocessing import Process, Manager, Value
from threading import Thread


logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())



amazon_data=[]
ebay_data=[]
walmart_data=[]

search_data_storage={}

def makeTable(data):
   
    #begin_row
    br="<tr>"
    #end row
    er="</tr>"
    #begin table data
    btd="<td>"
    #end table data
    etd="</td>"
    table_text=''
    table_text+="<thead><tr><th>name</th><th>price</th><th>rating</th><th>reviews</th><th>brand</th></tr></thead><tbody>"
    #print(type(data))
    #print(str(data))
    for row in data:
        table_text+=(br+btd+str(row['name'])+etd+btd+"$"+str(row['price'])+etd+btd+str(row['rating'])+etd+btd+str(row['reviews'])+etd+btd+str(row['brand'])+etd+er)
    table_text+="</tbody>"
    return (table_text)
'''
def search(search_key, search_from):
    return_data_list=[]
    return_data=''
    if (search_from=='amazon'):
        return_data=script.queryAmazonData(search_key, 40)
        amazon_score=score.calcScore(return_data)
        ebay_score=score.calcScore(script.queryEbayData(search_key, 40))
        walmart_score=score.calcScore(modify.reduceWalmart(script.queryWalmartData(search_key, 3)))
        #print('amazon')
    elif (search_from=='ebay'):
        return_data=script.queryEbayData(search_key, 40)
        amazon_score=score.calcScore(script.queryAmazonData(search_key, 40))
        ebay_score=score.calcScore(return_data)
        walmart_score=score.calcScore(modify.reduceWalmart(script.queryWalmartData(search_key, 3)))
        
        #print('ebay')
    elif (search_from=='walmart'):
        return_data=modify.reduceWalmart(script.queryWalmartData(search_key, 3))
        amazon_score=score.calcScore(script.queryAmazonData(search_key, 40))
        ebay_score=score.calcScore(script.queryEbayData(search_key, 40))
        walmart_score=score.calcScore(return_data)

        #print('walmart')
    return_data_list.append(return_data)
    return_data_list.append(str(amazon_score))
    return_data_list.append(str(ebay_score))
    return_data_list.append(str(walmart_score))
    return (return_data_list)
'''

def search(search_key, search_from, mode):
    return_data_list=[]
    manager = Manager()
    amazon_data_man=manager.list()
    ebay_data_man=manager.list()
    walmart_data_man=manager.list()
    global amazon_data
    global ebay_data
    global walmart_data
    global search_data_storage
    if (mode==0):
    	
    	threads=[]

    	threads.append(Thread(target = getAmazonData, args=(search_key, amazon_data_man)))
    	threads.append(Thread(target = getEbayData, args=(search_key, ebay_data_man)))
    	threads.append(Thread(target = getWalmartData, args=(search_key, walmart_data_man)))

    	for thread in threads:
    		thread.start()
    	for thread in threads:
    		thread.join()
        

    	amazon_data=amazon_data_man
    	ebay_data=ebay_data_man
    	walmart_data=walmart_data_man

    	search_data_storage[search_key]={'amazon':amazon_data, 'ebay':ebay_data, 'walmart':walmart_data}

    if (mode==2):
    	amazon_data=search_data_storage[search_key]['amazon']
    	ebay_data=search_data_storage[search_key]['ebay']
    	walmart_data=search_data_storage[search_key]['walmart']

    amazon_score=score.calcScore(amazon_data)
    ebay_score=score.calcScore(ebay_data)
    walmart_score=score.calcScore(walmart_data)
        
        #print('amazon')
    if (search_from=='amazon'):
        return_data=amazon_data
        #print('amazon')
    elif (search_from=='ebay'):
        return_data=ebay_data
        #print('ebay')
    elif (search_from=='walmart'):
        return_data=walmart_data
        #print('walmart')
    return_data_list.append(return_data)
    return_data_list.append(str(amazon_score))
    return_data_list.append(str(ebay_score))
    return_data_list.append(str(walmart_score))
    return (return_data_list)
def getAmazonData(search_key, returnData):
	returnData.extend(script.queryAmazonData(search_key, 40))

def getEbayData(search_key, returnData):
	returnData.extend(script.queryEbayData(search_key, 40))

def getWalmartData(search_key, returnData):
	returnData.extend(modify.reduceWalmart(script.queryWalmartData(search_key, 3)))
async def hello(websocket, path):
    global search_data_storage
    return_data=''
    input_string = await websocket.recv()
    

    #print(input_string)
    input_string_splitted=input_string.split(',')
    search_key, search_from, mode = input_string_splitted[0], input_string_splitted[1], input_string_splitted[2]
    #print('search_key : '+search_key+' search_from : '+search_from)
    if (mode=='0'):
    	if (search_key in search_data_storage.keys()):
    		return_data = search(search_key, search_from, 2)
    	else:
    		return_data=search(search_key, search_from, 0)
    	return_data[0]=makeTable(return_data[0])
        
    if (mode=='1'):
    	return_data=search(search_key, search_from, 1)
    	return_data[0]=makeTable(return_data[0])

    if (search_key=='moon lamp'):
    	return_data[1]='2'

        #할필요 없어 테이블은
        #return_data=json.dumps(return_data)
    #no switch statement;;;;
    await websocket.send(return_data)
    #그다음에 테이블 만들면 되겠다
    #print(f"> {return_data}")

start_server = websockets.serve(hello, '127.0.0.1', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()