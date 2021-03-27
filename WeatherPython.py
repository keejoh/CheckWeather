import requests
#creates a array to store city's temperatures
temparray = []
#creates a pointer for city
city = ""
#executes the following code until city == exit
while city != "exit":
	#asks user for a city
	city = input("Enter a city in the United States to get the five day forecast;\n enter exit to end program and see all your forecasts: ")
	#adds the city to the array
	temparray.append(city)
	#does the following operations if city==exit
	if city == "exit":
		temparray.pop()
		weatherfile = open("weather.txt", "w+")
		tempstring=str(temparray)
		weatherfile.write(tempstring)
		print(temparray)
	#does the following operations if city!=exit
	else:
		#sets the url for your api request given the input
		url = 'https://api.openweathermap.org/data/2.5/forecast?q={},us&APPID=40773ebab300f9d63ae6a22df3e39dd0&format=json&units=imperial'.format(city)
		res = requests.get(url)
		data = res.json()
		i = 0
		#if input is invalid prints error message. 
		if data['message']=='city not found':
			print("This is not a valid location")
			temparray.pop()
		else:	
			print("The five day forecast for " + city + " in fahrenheit is. ")
			#iterates over the json api response to get only a five day forecast
			while i <40:
				temperature = data['list'][i]['main']['temp']
				temparray.append(temperature)	
				print (temperature)
				i=i+8



