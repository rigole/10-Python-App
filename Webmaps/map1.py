import folium
map = folium.Map(location=[2.40, 10], zoom_start=6, tiles="Mapbox Bright")
for coordinates in [[4.0548443, 9.7294843],[5.0548443,11.7294843]]:
    map.add_child(folium.Marker(location=coordinates,popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.save("Map.html")