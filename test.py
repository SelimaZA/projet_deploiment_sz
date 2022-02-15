import requests

ENDPOINT = "http://127.0.0.1:5002/predict"# j'ai mon endpoint avec ma route predict 


# This a simple example of input
input_simple = {
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
}

response = requests.post(ENDPOINT, json=input_simple)

print(response,response.json())#je vais imprimer la réponse et la réponse json 
