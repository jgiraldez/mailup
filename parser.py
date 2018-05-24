import json
import csv
import os

KEYS = ['user_id','product_id']

for files in os.walk("."):  
    for filename in files:
        for i in filename:
            if i.endswith(".json"):
                print(i)
                with open('order-vtex.json') as json_data:
                    order_parsed = json.load(json_data)
                    products_data = order_parsed['items']
                    user_data = order_parsed['clientProfileData']
                            
                with open('vtex-orders.csv','w') as dataFile:
                    newFileWriter = csv.writer(dataFile)
                    newFileWriter.writerow(KEYS)
                    for item in products_data:
                        productId = (products_data[0]['productId'])
                        userId = (user_data["userProfileId"])
                        print(productId)
                        print(userId)
                        newFileWriter.writerow([userId,productId])
                print('-------')