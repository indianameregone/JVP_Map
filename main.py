import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import numpy as np
import pandas as pd
from vega_datasets import data as vds


#Coordenadas del mapa a localizar
lat     = -32.37092699233746  
lon     = -59.93105965747769

mapa    = folium.Map(location=[lat,lon],zoom_start=16) #zoom 13 da la perspectiva del mapa desde el aire

#Capas de mapa
folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Cartodb Positron').add_to(mapa)
folium.TileLayer('Cartodb dark_matter').add_to(mapa)

caños = folium.FeatureGroup(name='caños')
clientes = folium.FeatureGroup(name='clientes')
caños.add_to(mapa)
clientes.add_to(mapa)

folium.LayerControl().add_to(mapa)

folium.ClickForMarker

#con pandas leo el mapa
caños_map   = pd.read_excel('Modelo de datos.xlsx',sheet_name='caños')
cli_map     = pd.read_excel('Modelo de datos.xlsx',sheet_name='cliente')
for index,row in caños_map.iterrows():
    folium.PolyLine([(row['LatI'],row['LonI']),(row['LatF'],row['LonF'])],fill=True,color='green',weight=3,popup="Red de caños").add_to(caños)

for index,row in cli_map.iterrows():
    folium.Marker([row['Lat'],row['Lon']],popup=row['Num_Cli'],tooltip=f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Clientes del Mapa</title>
        </head>
        <body>
            <table border = '3' cellpadding ='5' cellspacing = '5'>
                <tr>
                <tr>
                    <th style='text-align:center;background-color:#ccccff'>Codigo</th>
                    <th style='text-align:center;background-color:#ccccff'>Nombre</th>
                    <th style='text-align:center;background-color:#ccccff'>Direccion</th>
                    <th style='text-align:center;background-color:#ccccff'>Numero</th>
                    <th style='text-align:center;background-color:#ccccff'>Telefono</th>
                    <th style='text-align:center;background-color:#ccccff'>Mail</th>
                </tr>
                <td style='text-align:center'>{row['Num_Cli']}</td>
                <td style='text-align:center'>{row['Titular']}</td>
                <td style='text-align:center'>{row['Direccion']}</td>
                <td style='text-align:center'>{row['Numero']}</td>
                <td style='text-align:center'>{row['Telefono']}</td>
                <td style='text-align:center'>{row['Mail']}</td>
                </tr>
            </table>
        </body>
    </html>
    """).add_to(clientes)

draw = plugins.Draw(export=True)
draw.add_to(mapa)
geoJson = pd.read_json('data.geojson')
newClient_lat = geoJson["features"][0]["geometry"]["coordinates"][0]
newClient_lon=  geoJson["features"][0]["geometry"]["coordinates"][1]

print(cli_map)

#se guarda en un archivo .html que sobreescribimos segun modificaciones
mapa.save('mimapa.html')




