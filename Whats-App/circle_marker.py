import folium
import pandas as pd

data = pd.read_csv(r"C:\Users\UMANG\Desktop\projects\#FUN\Map\Volcanoes.txt")

lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elev=list(data["ELEV"])

def color(a):
    if a<1000:
        return "green"
    elif a<2000:
        return "orange"
    else:
        return "red"
    

map=folium.Map(location=[22.289790,73.362439],zoom_start=6, tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="Rapchik Map")

for lt,ln,na,el in zip(lat,lon,name,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=na+" "+str(el)+"m"))
    

map.add_child(fg)
map.save(r"C:\Users\UMANG\Desktop\projects\#FUN\Map\map1.html")
