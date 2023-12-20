import requests ## to use the POST method we use a library named requests

url = 'http://localhost:9696/predict'

sample = {"cement": 251.8,
 "slag": 0.0,
 "flyash": 99.9,
 "water": 146.1,
 "superplasticizer": 12.4,
 "coarseaggregate": 1006.0,
 "fineaggregate": 899.8,
 "age": 100.0}

response = requests.post(url, json=sample).json() ## post the student information in json format
print(response)