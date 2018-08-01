import falcon as fn
import pandas as pd
import json


df = pd.read_csv('/home/drogon/Flight(classification).csv')

print df.describe


class ObjRequestClass:
     def on_get(self, req, resp):
         content = {
             "Name" : "Ahsaan",
             "Age" : "22",
             "Country" : "Pakistan",
             "Email" : "ahsanfayyaz74@gmail.com"
         }

         resp.body = json.dumps(content)
         print "hello"

api = fn.API()
api.add_route('/test', ObjRequestClass())




