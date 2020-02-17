from django.shortcuts import render


def home(request):
    #http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=10&API_KEY=888326FB-33F0-4CE5-9A35-E7F73C64A1A4
    import json
    import requests
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=10&API_KEY=888326FB-33F0-4CE5-9A35-E7F73C64A1A4")

    try:
        global api
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    context = {'api':api}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request,'about.html',context)
