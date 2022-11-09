import requests

resposta = requests.get('https://www.walissonsilva.com/')

print(resposta.status_code)
print(resposta.headers)
print(resposta.content)
