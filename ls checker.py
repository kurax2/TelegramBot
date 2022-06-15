import requests # send receive website
import json # to read json pretty
import random
import time

def sendMessage(message)
    requests.get('httpsapi.telegram.orgbot5287233731AAGr37ojkHQHX1MdBtzQNqNbJg6_yz4IW8osendMessagechat_id=86897783&text={}'.format(message))


names =  [ 
	Kit , Danish , Dani , Firdaus , Eddy ,  Jerry ,  Daniel ,  Remy , Ivan , Mambo , Jason , Yongyao , Wayne , Darrell , Clifford , Lionel , Yeo , Bing , Vancence , Guanliang , Weijie , Peter , Andy , Weibin , Yu , Chesien , Javyn , Hafiz , Amish , Javier , Choon ]
empty = []
while(True)
    page = requests.get('httpsapi.telegram.orgbot5287233731AAGr37ojkHQHX1MdBtzQNqNbJg6_yz4IW8ogetUpdates')
    parsed = json.loads(page.text)
    
    try
        if(parsed['result'][-1]['message']['text'] == List)
            sendMessage(List )
            time.sleep(10)
            
            page = requests.get('httpsapi.telegram.orgbot5287233731AAGr37ojkHQHX1MdBtzQNqNbJg6_yz4IW8ogetUpdates')
            parsed = json.loads(page.text)
            time.sleep(30)
            
            try
                reply = str(parsed['result'][-1]['message']['text'])
                n = reply.split()
                empty = names
                x = len(n)
                for i in range(x)
                    if n[i] in names
                        empty.remove(n[i])
                sendMessage(, .join(empty))
                
                    
                    
            except ValueError
                        continue
        time.sleep(60)
    except IndexError
        continue