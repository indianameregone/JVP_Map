from multiprocessing.connection import Client
import folium
from googlemaps import Client

ciudad = input('ingrese un lugar: ')

cliente  = Client(key='AIzaSyAexzNtMhvA2Smena8RnyLftNvcHRzK2zM')
resultado = cliente.geocode(ciudad)[0]
lat = cliente.geocode(ciudad)[0]['geometry']['location']['lat']
lon = cliente.geocode(ciudad)[0]['geometry']['location']['lng']

print(lat)
print(lon)