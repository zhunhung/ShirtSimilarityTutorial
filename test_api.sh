# Test Local
curl -i -X POST -k http://localhost:7071/api/ShirtSim -F "file=@{path_to_image}"
# Test Live Azure Function
# curl -i -X POST -k FUNCTION_URL_HERE -F "file=@{path_to_image}"