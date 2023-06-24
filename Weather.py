import requests
city = input("Enter your city: ");
apiKey= '5dd12427f0de3aebe2071602757e9961'
url = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&mode=json&appid=5dd12427f0de3aebe2071602757e9961";
response = requests.get(url);
data = response.json();
print(data)
for dt in data['list']:
    for forecast in dt['weather']:
        print("Weather forecast for "+ city,"at time "+dt['dt_txt'], ":", forecast['description']);
