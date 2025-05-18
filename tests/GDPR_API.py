

import http.client
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

conn = http.client.HTTPSConnection("qa-auth.agilone.com")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic dmFpYmhhdi52ZXJtYUBhY3F1aWEuY29tOlZhaWJoYXZAMzU1NA=='
}
conn.request("POST", "/authentication?action=login", payload, headers)
res = conn.getresponse()
x = res.read()
data=x.decode("utf-8")
values = json.loads(data)
# print(db['teacher_db'][0]['name'])
# for x in values:
#     token=x["access_token"]
token=values["access_token"]
endpoint = "https://qa-api6.agilone.com/v2/3/orchstatus?limit=1&since="

# headers = {"Authorization": "Bearer 3bf81688-8dbe-4d7d-91ad-c55e6c79d3ae"}
#
#headers = {"Authorization": "Bearer 77db82ac-e3f1-4c00-8417-7db299000e61"}

conn1 = http.client.HTTPSConnection("qa-configapi.agilone.com")
payload1 = ''
headers1 = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {}'.format(token)}
conn1.request("GET", "/v2/3/orchstatus?limit=100&since=", payload1, headers1)
res1 = conn1.getresponse()
x1 = res1.read()
data1=x1.decode("utf-8")
values1 = json.loads(data1)
y1=0


def run_data():
    conn1.request("POST", "/v2/3/config/workflows/DATA_ERASURE_DEFAULT?action=run", payload1, headers1)
    print("---------------------------------------")
    print("Running Data Erasure WF")
    res3 = conn1.getresponse()
    x3 = res3.read()
    data3 = x3.decode("utf-8")
    values3 = json.loads(data3)
    print(values3.get('eventId'))
    return values3

run_data()

# for x in range(0,20):
#   if(values1[x]["status"]=='RUNNING'and values1[x]["jobType"]=="WORKFLOW"):
#      print(values1[x]["workflowName"])
#      y1=y1+1
# print("\nThere are "+str(y1)+" workflows running in QA1")
# #-------------------------------
# conn2 = http.client.HTTPSConnection("qa-configapi.agilone.com")
# payload2 = ''
# headers2 = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Bearer {}'.format(token)}
# conn2.request("GET", "/v2/40/orchstatus?limit=100&since=", payload2, headers2)
# res2 = conn2.getresponse()
# x2 = res2.read()
# data2=x2.decode("utf-8")
# values2 = json.loads(data2)
# y2=0
# print("---------------------------------------")
# for y in range(0,20):
#   if(values2[y]["status"]=='RUNNING' and values2[y]["jobType"]=="WORKFLOW"):
#      print(values2[y]["workflowName"])
#      y2=y2+1
# print("There are "+str(y2)+" workflows running in QARegression")
# if y1==0 and y2==0:
#     run_data()
# else:
#     print(" Do you still want to continue? (Y/N)")
#     x=input()
#     if(x=='y'or x=='Y'):
#         run_data()
#     else:
#         print("Exiting")





#-----------------in progress-----


# for x in values1:

#   if(values1[0]["status"]=='RUNNING' and values1[0]["jobType"]=="CAMPAIGN"):
#     y=y+1
#   if(y>=10):

# values2=values1.replace(']','')




# x = res.read()
# data=x.decode("utf-8")
# values = json.loads(data)

# json_file=requests.get(endpoint, headers=headers).json()

# jsonwrite=open("data.json","w")
# jsonwrite.write(jsonString)
# jsonwrite.close

# jsonFile = open('data.json', 'r')
# values = json.load(json_file)
# print(values["id"])




