from django.shortcuts import render
import requests
import json

#z8XHdIAuHFWPMkuzxyudeQ==a031jYoRcQ06oUZP z8XHdIAuHFWPMkuzxyudeQ==BrnOx7miUt1C2hSF
def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'z8XHdIAuHFWPMkuzxyudeQ==BrnOx7miUt1C2hSF'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html',{'api': api['items']})
    else:
        return render(request, 'home.html',{'query':'Enter a valid query'})
