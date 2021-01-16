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
    map.add_child(folium.CircleMarker(location=[lt, ln], radius = 6,popup=str(el),
                                      icon=folium.Icon(color=color_producer(el)),color = 'grey', fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))
map.add_child(fg)
map.save("Map.html")