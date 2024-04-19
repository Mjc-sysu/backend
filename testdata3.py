import random
import time
import json
from datetime import datetime, timedelta


# Generate 30 sample documents
sample_data = []

now = datetime.now().replace(microsecond=0)


## predict now time + 24h for 3 days
for i in range(10):
    for j in range(3):
        count = random.randint(1,50)
        timestamp = now + timedelta(days=j+1)
        document = {
            'id': i + 1,
            'count': count,
            #'date': time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp)) 
            'date': timestamp.strftime("%Y-%m-%d %H:%M:%S")

        }
        sample_data.append(document)

# Print the sample documents
# for doc in sample_data:
#     print(doc)

with open('sample_data3.json', 'w') as f:
    json.dump(sample_data, f, indent=4)