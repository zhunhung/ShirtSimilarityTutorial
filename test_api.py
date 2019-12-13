import requests

local_endpoint = "http://localhost:7071/api/ShirtSim"
live_endpoint = "FUNCTION_ENDPOINT"

# Specify image to test
test_image_path = "path_to_image"
files={"file":open(test_image_path,'rb')}

# Make POST request
r = requests.post(url=local_endpoint, files=files)
print(r.text)