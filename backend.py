import requests

API_Key = 'dc21d83171118f58f90e40ede0e4f2c5'

def get_data(city, forecast_days=None):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_Key}"
    response = requests.get(URL)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    print(get_data(city="Tokyo"))



