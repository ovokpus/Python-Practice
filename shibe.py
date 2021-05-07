# First thing we'll do is import the requests library
import requests

# Define a variable with the URL of the API
api_url = "http://shibe.online/api/shibes"

params = {
    "count": 5
}


# Call the root of the api with GET, store the answer in a response variable
# This call will return a list of URLs that represent dog pictures
api_response = requests.get(api_url, params=params)

# # Get the status code for the response. Should be 200 OK
# # Which means everything worked as expected
print(f"Shibe API Response Status Code is: {api_response.status_code}")

# Get the result as JSON
json_data = api_response.json()

# Print it. We should see a list with one image URL.
print("Here is a list of URLs for dog pictures:")
for url in json_data:
    print(f"\t {url}")
