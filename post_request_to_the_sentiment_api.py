import requests

url = 'http://127.0.0.1:5000/get_sentiment'
payload = {
    'text': 'Hello mister viwer , I apreciate your visite to my github repo , please leave a star in your way'
}
headers= {
    'Content-Type' : 'application/json'
}

r= requests.post(url , json = payload , headers = headers )
print(r.text)