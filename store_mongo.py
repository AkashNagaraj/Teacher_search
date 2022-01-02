import pymongo
import json, ast, regex


def main_mongo():
   # initialize mongodb client
   myclient = pymongo.MongoClient("mongodb://localhost:27017/")
   data_base = myclient["mydatabase"]
   collection = data_base["content"]

   # read data to post in mongoodb collection
   data_list = open('data/output.txt','r').read()
   data_list = ast.literal_eval(data_list)['complete_data']
   
   # insert document
   # collection.insert_many(data_list) 
 
   # query for specific substring
   sub_string = " Re "
   query = {'content':{regex:sub_string}} 
   result = collection.find(query)
   print(result)
   
