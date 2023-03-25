import requests

response = requests.get('http://127.0.0.1:8000/api/snippets')
print(response.json())

payload = {
    "title":"title",
    "code":"code"
}
response = requests.post('http://127.0.0.1:8000/api/snippets', json=payload)
print(response.content)