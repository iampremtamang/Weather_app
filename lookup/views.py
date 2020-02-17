from django.shortcuts import render


def home(request):
    #http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=10&API_KEY=888326FB-33F0-4CE5-9A35-E7F73C64A1A4
    import json
    import requests
    zipcode = ""
    if request.method == "POST":
        zipcode = request.POST.get("zipcode")
    api_request = []
    if zipcode:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode+"&distance=10&API_KEY=888326FB-33F0-4CE5-9A35-E7F73C64A1A4")
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=10&API_KEY=888326FB-33F0-4CE5-9A35-E7F73C64A1A4")

    try:
        global api
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    category_description = ""
    category_name = ""

    if api[0]["Category"]["Name"] == "Good":
        category_name = "good"
        category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
    elif api[0]["Category"]["Name"] == "Moderate":
        category_name = "moderate"
        category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution. "
    elif api[0]["Category"]["Name"] == "USG":
        category_name = "usg"
        category_description = "(101 - 150) Unhealthy for Sensitive Groups. Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
    elif api[0]["Category"]["Name"] == "Unhealthy":
        category_name = "unhealthy"
        category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects. "
    elif api[0]["Category"]["Name"] == "Very Unhealthy":
        category_name = "very-unhealthy"
        category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
    elif api[0]["Category"]["Name"] == "Hazardous":
        category_name = "hazardous"
        category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected. "

    context = {'api':api, 'category_description': category_description, 'category_name':category_name}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request,'about.html',context)
