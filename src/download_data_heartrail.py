import requests
import pandas as pd


url = "https://express.heartrails.com/api/json"


### GET PREFECTURES ###
params_prefecture = {
    "method": "getPrefectures"
}

response = requests.get(url, params=params_prefecture)

data = response.json()
list_prefectures = data["response"]["prefecture"]
# print(list_prefectures)
### GET PREFECTURES ###



### GET LINES ###
params_lines = {
    "method": "getLines",
    "prefecture": "東京都"
}

response = requests.get(url, params=params_lines)

print(response.status_code)

data = response.json()
list_lines = data["response"]["line"]
# print(list_lines)
### GET LINES ###



### GET STATIONS ###
all_stations = []

for line in list_lines:
    params_stations = {
        "method": "getStations",
        "line": line
    }

    response = requests.get(url, params=params_stations)
    data = response.json()

    stations = data["response"]["station"]

    all_stations.extend(stations)
    print(f"Collected: {line}")

### GET STATIONS ###



### BUILD DF ###
df = pd.DataFrame(all_stations)
# df.drop(columns = ['prefecture'], inplace = True)
print(df.head())
print(df.shape)

df.to_csv(
    "../data/raw/tokyo_stations.csv",
    index=False)
### BUILD DF ###