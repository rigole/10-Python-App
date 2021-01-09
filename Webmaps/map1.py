import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[2.40, 10], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="M map")
for lt, ln in zip(lat, lon):
    map.add_child(folium.Marker(location=[lt, ln],popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.save("Map.html")