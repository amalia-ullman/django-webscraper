from django.shortcuts import render
#from django import Http404
import requests
import json

def index(request1):
  with open("webscraper/templates/webscraper/out.html", 'w') as f:
    api_url = 'https://api.api-ninjas.com/v1/webscraper?url=https://www.target.com'
    response = requests.get(api_url, headers={'X-Api-Key': 'tMJ3rqBbZrT0ijHaibuDrA==Q61Gr7Kz0fn2YLO7'})
    if response.status_code == requests.codes.ok:
      res = json.loads(response.text)
      f.write(res[list(res.keys())[0]])
      return render(request1, "webscraper/out.html")
    else:
      print("Error:", response.status_code, response.text)
      return render(request1, "webscraper/index.html", {"data": response.status_code + response.text})