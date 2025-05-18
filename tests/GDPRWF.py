

import http.client
import json
import requests
import ssl
from datetime import datetime
import time


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



def check_status():
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    params = {
        "limit": "3",
        "since": timestamp
    }
    # conn1.request("GET", "/v2/3/orchstatus?limit=3&since={{$timestamp}}", headers1, params)
    response = requests.get("https://qa-api6.agilone.com/v2/3/orchstatus?", params=params,headers=headers1)

    # res4 = conn1.getresponse()
    # x4 = res4.read()
    # data4 = x4.decode("utf-8")
    # values4 = json.loads(data4)
    json_data = response.json()
    latest_entry = None
    latest_entry_status = None

    # Iterate through each entry in the JSON response
    for entry in json_data:
        if entry['workflowName'] == 'DATA_ERASURE_DEFAULT':
            # Check if this entry has the latest timestamp
            if latest_entry is None or datetime.strptime(entry['started'], '%m-%d-%Y %H:%M:%S') > datetime.strptime(
                    latest_entry['started'], '%m-%d-%Y %H:%M:%S'):
                latest_entry = entry

    # If a latest entry with 'DATA_ERASURE_DEFAULT' workflowName is found
    if latest_entry:
        latest_entry_status = latest_entry['status']
        print("Latest status of DATA_ERASURE_DEFAULT:", latest_entry_status)
    else:
        print("No entry with workflowName 'DATA_ERASURE_DEFAULT' found in the response")


while True:
    # Get the latest status
    status = check_status()

    # Check if the status is 'COMPLETED'
    if status == 'SUCCEEDED':
        print("Workflow status is COMPLETED. Exiting loop.")
        break

    # Wait for 60 seconds before pinging the URL again
    time.sleep(60)

check_status()




