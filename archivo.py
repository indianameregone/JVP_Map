import pandas as pd
import pymssql


conn    = pymssql.connect(
                'jvpdatos.database.windows.net',
                'jcverni@jvpsa.onmicrosoft.com@jvpdatos',
                'Juan11121923',
                'Laboratorio'
            )
cursor  = conn.cursor()
camino = 'SELECT * FROM tbl_XYT_Mex_Camino_Optico'

tbl_mex = pd.read_sql(camino,conn)


def hilo():
    hilo = input('Ingrese un hilo: ')
    e = 0
    camino =[]
    for i in tbl_mex.iterrows():
        if hilo == tbl_mex['Id_Hilo'][e]:
            hilos =tbl_mex['Id_Hilo'][e]
            buffer =tbl_mex['Id_Buffer'][e]
            cable = tbl_mex['Id_Cable'][e]
            final =tbl_mex['Id_Final'][e]
            emp = tbl_mex['Id_Empalme'][e]

            camino.append(hilos)
            camino.append(buffer)
            camino.append(cable)
            camino.append(final)
            camino.append(emp)
            print(camino)
        e += 1

def search(id):
    id = input('Ingrese un id de inicio: ')
    e = 0
    for i in tbl_mex.iterrows():
        if id == tbl_mex['Id_Inicio'][e]:
            print(tbl_mex['Id_Inicio'][e],tbl_mex['Id_Hilo'][e])
        e += 1
    print('===================')
    hilo()    
    

search(id)  
