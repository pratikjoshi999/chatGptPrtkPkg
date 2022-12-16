

import chatgptprtk as ch
import os

api_key=os.getenv('API_KEY')
# msg="I want to learn Python, MVC, MongoDb and Azure what we will be completed soon"

ch.setApiKey(api_key)
# print(ch.sendMessage(msg))

ch.startServer()



