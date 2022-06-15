import requests # send receive website
import json # to read json pretty
import random
import time

def sendMessage(message):
    requests.get('https://api.telegram.org/bot5287233731:AAGr37ojkHQHX1MdBtzQNqNbJg6_yz4IW8o/sendMessage?chat_id=86897783&text={}'.format(message))

names =  [ 
	"Kit" , "Danish" , "Dani" , "Firdaus" , "Eddy" ,  "Jerry" ,  "Daniel" ,  "Remy" , "Ivan" , "Mambo" , "Jason" , "Yong Yao" , "Wayne" , "Darrell" , "Clifford" , "Lionel" , "Yeo Ee" , "Bing Heng" , "Vancence" , "Guan Liang" , "Wei Jie" , "Peter" , "Andy" , "Wei Bin" , "Yu Xuan" , "Chesien" , "Javyn" , "Hafiz" , "Amish" , "Javier" , "Choon Yong" ]
txt=str()
while(True):
    page = requests.get('https://api.telegram.org/bot5287233731:AAGr37ojkHQHX1MdBtzQNqNbJg6_yz4IW8o/getUpdates')
    parsed = json.loads(page.text)
    
    try:
        if(parsed['result'][-1]['message']['text'] == "Help"):
            sendMessage("How many: ")
            time.sleep(10)
            
            page = requests.get('https://api.telegram.org/bot5287233731:AAGr37ojkHQHX1MdBtzQNqNbJg6_yz4IW8o/getUpdates')
            parsed = json.loads(page.text)
            
            try:
                n = int(parsed['result'][-1]['message']['text'])
                random.shuffle(names)
                
                #print(names)
                for i in range(0,n):
                    txt=txt+str(names[i]+("\n"))
                    time.sleep(1)
                    
                sendMessage("Plz do the stores, thank you.\n\n"+txt) 
                
            except ValueError:
                continue
        
        txt=""
        time.sleep(60)
        
    except IndexError:
        continue
