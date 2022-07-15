import folium
import pandas as pd
import pymssql


conn    = pymssql.connect(
                'jvpdatos.database.windows.net',
                'jcverni@jvpsa.onmicrosoft.com@jvpdatos',
                'Juan11121923',
                'Laboratorio'
            )
cursor  = conn.cursor()


mex_objetos = 'SELECT lat,lon FROM tbl_XYT_Mex_Objetos'
mex_tramos  = 'SELECT Lati,Loni,Latf,Lonf FROM xytMexAutoCableTramos'
mex_cierre  = 'SELECT Lat,Lon FROM xytMexAutoCierre'
mex_empalme = 'SELECT Lat,Lon FROM xytMexAutoEmpalme'
mex_hilo    = 'SELECT Lat,Lon FROM xytMexAutoHilo'
mex_sitio   = 'SELECT Lat,Lon FROM xytMexAutoSitio'
mex_tubo    = 'SELECT Lat,Lon FROM xytMexAutoTubo'

latlon  = pd.read_sql(mex_tramos,conn)
obj     = pd.read_sql(mex_objetos,conn)
close   = pd.read_sql(mex_cierre,conn) 
emp     = pd.read_sql(mex_empalme,conn) 
dread   = pd.read_sql(mex_hilo,conn) 
site    = pd.read_sql(mex_sitio,conn) 
pipe    = pd.read_sql(mex_tubo,conn) 

#Coordenadas del mapa a localizar
lat     = 19.429708131780036 
lon     = -99.13942199005166

mapa    = folium.Map(location=[lat,lon],zoom_start=10) #zoom 13 da la perspectiva del mapa desde el aire

#Capas de mapa
folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Cartodb Positron').add_to(mapa)
folium.TileLayer('Cartodb dark_matter').add_to(mapa)

cable    = folium.FeatureGroup(name='cable')
objetos = folium.FeatureGroup(name='objeto')
cierre  = folium.FeatureGroup(name='cierre') 
empalme = folium.FeatureGroup(name='empalme')
hilo    = folium.FeatureGroup(name='hilo')
sitio   = folium.FeatureGroup(name='sitio')
tubo    = folium.FeatureGroup(name='tubo')

cable.add_to(mapa)
objetos.add_to(mapa)
cierre.add_to(mapa)
empalme.add_to(mapa)
hilo.add_to(mapa)
sitio.add_to(mapa)
tubo.add_to(mapa)


folium.LayerControl().add_to(mapa)

i = 0
lati = latlon['Lati']
loni = latlon['Loni']
latf = latlon['Latf']
lonf = latlon['Lonf']

for e in lati:
    try: 
        latI = float(lati[i])    
        lonI = float(loni[i])
        latF = float(latf[i])
        lonF = float(lonf[i])
        
        folium.PolyLine([(latI,lonI),(latF,lonF)],fill=True,color='red',weight=3).add_to(cable)
    except:
        pass
    i +=1

def parts(object,color,capa):
    lati = object['Lat']
    loni = object['Lon']
    i = 0
    for e in lati:
        try: 
            latI = float(lati[i])    
            lonI = float(loni[i])
                    
            folium.Circle(location=[latI,lonI],radius=100, fill= True,color=color).add_to(capa)
        except:
            pass
        i += 1

def partes(object,color,capa):
    lati = object['lat']
    loni = object['lon']
    j = 0
    for e in lati:
        try: 
            latI = float(lati[j])    
            lonI = float(loni[j])
                    
            folium.Circle(location=[latI,lonI],radius=100, fill= True,color=color).add_to(capa)
        except:
            pass
        j += 1

partes(obj,'green',objetos)
parts(close,'blue',cierre)
parts(emp,'pink',empalme)
parts(dread,'yellow',hilo)
parts(site,'grey',sitio)
parts(pipe,'black',tubo)

#se guarda en un archivo .html que sobreescribimos segun modificaciones
mapa.save('mimapa.html')