import folium
import pandas as pd

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'


data = pd.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])



map = folium.Map(location=[2.40, 10], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="M map")
for lt, ln, el in zip(lat, lon, elev):
    map.add_child(folium.Marker(location=[lt, ln],popup=str(el), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)
map.save("Map.html")