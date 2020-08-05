from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=4E7245DA-30DE-4F78-A525-65A6776D361C")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error!!"

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and there is no pollution, so no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable, however there is some air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(100 - 150) Although general public is not likely to be affected in this AQI range," \
                                   " but people with lung disease, order adults and children are at greater risk."
            category_color = "unhealthy for sensitive groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to feel health effects, members of sensitive group may " \
                                   "feel health issues. "
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health Alert: Everyone may experience more serious health effects."
            category_color = "very unhealthy"

        return render(request, 'home.html', {
            "api": api,
            "category_description": category_description,
            "category_color": category_color,
        })
    else:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=4E7245DA-30DE-4F78-A525-65A6776D361C")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error!!"

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is considered satisfactory, and there is no pollution, so no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable, however there is some air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(100 - 150) Although general public is not likely to be affected in this AQI range," \
                                   " but people with lung disease, order adults and children are at greater risk."
            category_color = "unhealthy for sensitive groups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to feel health effects, members of sensitive group may " \
                                   "feel health issues. "
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health Alert: Everyone may experience more serious health effects."
            category_color = "very unhealthy"

        return render(request, 'home.html', {
            "api": api,
            "category_description": category_description,
            "category_color": category_color,
        })


def about(request):
    return render(request, 'about.html', {})
