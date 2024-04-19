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

for i in range(50):
    latitude = random.uniform(LA_latitude_range[0], LA_latitude_range[1])
    longitude = random.uniform(LA_longitude_range[0], LA_longitude_range[1])
    timestamp = random.uniform(start_time, end_time)
    source = random.choice(source_choices)
    document = {
        'id': i + 1,
        'latitude': latitude,
        'longitude': longitude,
        'source': source,
        'lastUpdated': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    }
    sample_data.append(document)

# Print the sample documents
# for doc in sample_data:
#     print(doc)

with open('sample_data.json', 'w') as f:
    json.dump(sample_data, f, indent=4)