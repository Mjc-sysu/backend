import random
import time
import json

# Generate 50 sample documents
sample_data = []
LA_latitude_range = (34.05, 34.33)  # Latitude range for Los Angeles
LA_longitude_range = (-118.57, -118.16)  # Longitude range for Los Angeles
source_choices = ['X', 'user report', 'facebook']
start_time = time.mktime(time.strptime("2024/01/01", "%Y/%m/%d"))
end_time = time.mktime(time.strptime("2024/04/18", "%Y/%m/%d"))

for i in range(10):
    for j in range(10):
        count = random.randint(1,120)
        timestamp = random.uniform(start_time, end_time)
        source = random.choice(source_choices)
        document = {
            'id': i + 1,
            'count': count,
            'date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        }
        sample_data.append(document)

# Print the sample documents
# for doc in sample_data:
#     print(doc)

with open('sample_data2.json', 'w') as f:
    json.dump(sample_data, f, indent=4)