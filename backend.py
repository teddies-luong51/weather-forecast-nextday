import requests

APIkey = "1e27dd0f7cfa0b6410f45737ef86ea91"


def get_data(place, days=None):
    url = "https://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&appid={APIkey}"
    respond = requests.get(url)
    data = respond.json()
    times = days * 8
    filter_data = data['list'][0:times]
    return filter_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", days=1, kind="Sky"))

