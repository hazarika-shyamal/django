import requests
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout


# the index() will handle all the app's logic


def index(request):
    # Check if user is logged in
    if not request.session.get('logged_in'):
        return redirect('login')

    # if there are no errors the code inside try will execute
    try:
        # checking if the method is POST
        if request.method == 'POST':
            API_KEY = '425a56346a4331f5158025241128efe6'
            # getting the city name from the form input
            city_name = request.POST.get('city')
            # the url for current weather, takes city_name and API_KEY
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
            # converting the request response to json
            response = requests.get(url).json()
            # getting the current time
            current_time = datetime.now()
            # formatting the time using directives, it will take this format Day, Month Date Year, Current Time
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            # bundling the weather information in one dictionary
            city_weather_update = {
                'city': city_name,
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                'country_code': response['sys']['country'],
                'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                'time': formatted_time
            }
        # if the request method is GET empty the dictionary
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'weatherupdates/home.html', context)
    # if there is an error the 404 page will be rendered
    # the except will catch all the errors
    except:
        return render(request, 'weatherupdates/404.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' and password == 'a':
            # hardcoded authentication successful
            request.session['logged_in'] = True
            return redirect('home')
        else:
            # authentication failed
            messages.error(request, 'Invalid username or password')
            return render(request, 'weatherupdates/login.html')
    else:
        return render(request, 'weatherupdates/login.html')


# def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' and password == 'a':
            # hardcoded authentication successful
            return redirect('home')
        else:
            # authentication failed
            return render(request, 'weatherupdates/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'weatherupdates/login.html')


def logout_view(request):
    logout(request)
    # other logout logic, such as redirecting to the login page
    return redirect('home')
