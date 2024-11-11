import folium
import numpy as np
import pandas as pd

lat_start = 29.84303
lat_end = 29.31152
lon_start = -95.78293
lon_end = -94.84634

lat_step_km = 1  
lon_step_km = 1 

lat_deg_to_km = 111.32
lon_deg_to_km = 85.0 

lat_step_deg = lat_step_km / lat_deg_to_km
lon_step_deg = lon_step_km / lon_deg_to_km

latitudes = np.arange(lat_start, lat_end, -lat_step_deg) 
longitudes = np.arange(lon_start, lon_end, lon_step_deg)

m = folium.Map(location=[lat_start, lon_start], zoom_start=12)

data = []
counter = 1  

for lat in latitudes:
    for lon in longitudes:
        north = round(lat, 6)
        south = round(lat - lat_step_deg, 6)
        east = round(lon + lon_step_deg, 6)
        west = round(lon, 6)
        
        folium.Rectangle(bounds=[[south, west], [north, east]],
                         color='blue', weight=2, fill=True, fill_opacity=0.2).add_to(m)
        
        # Kutu numarasını ekleyen işaretçi
        folium.Marker(
            location=[north, west],
            icon=folium.DivIcon(html=f'<div style="font-size: 10pt; color: black">{counter}</div>')
        ).add_to(m)
        
        # Data listesine koordinatları ekleme
        data.append([west, south, east, north])
        
        counter += 1

m.save('map.html') 

with open('fields.txt', 'w') as txt_file:
    for row in data:
        txt_file.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")

df = pd.DataFrame(data, columns=['West', 'South', 'East', 'North'])
df.to_excel('fields.xlsx', index=False)

print("Success!")
