import requests
import json

# Make a GET request to the weather API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# Save the JSON response to a file
with open('weather.json', 'w') as f:
    output_json = json.dumps(result.json(), indent=4, sort_keys=True)
    f.write(output_json)

result_dict = json.loads(result.text) #parse the json string into a dict object

# print the temperature of each location
for location in result_dict["temperature"]["data"]:
    print(location["place"], location["value"])