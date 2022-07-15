from flask import Flask, render_template,request,session,redirect,url_for
from graphviz import render
import pandas as pd
import pymssql

conn    = pymssql.connect(
                'jvpdatos.database.windows.net',
                'jcverni@jvpsa.onmicrosoft.com@jvpdatos',
                'Juan11121923',
                'Laboratorio'
            )

mex_objetos = 'SELECT * FROM tbl_XYT_Mex_Camino_Optico'
obj         = pd.read_sql(mex_objetos,conn)

app = Flask(__name__)
app.secret_key = 'Hello'

def equal(lat):
    e = 0       
    li = []        
    for i in obj.iterrows(): 
        if lat == obj['Id_Inicio'][e]:
            li.append(obj['Id_Hilo'][e]) 
        e += 1        
    return li

def buff(lat):
    e = 0       
    li = []        
    for i in obj.iterrows(): 
        if lat == obj['Id_Hilo'][e]:
            li.append(obj['Id_Buffer'][e]) 
        e += 1        
    return li


@app.route('/',methods=['POST','GET'])
def inicio():    
    inicio = obj['Id_Inicio']
    return render_template('inicio.html', inicio = inicio)

@app.route('/hilo',methods=['POST','GET'])
def hilo():
    hilo = obj['Id_Hilo']
    inicio = request.form['inicio']
    if 'inicio' in session:
        session['inicio'] = inicio
        inicio = inicio
        hilo = equal(inicio)
        return render_template('hilo.html',inicio = inicio,hilo = hilo)

@app.route('/buffer',methods=['POST','GET'])
def buffer():    
    hilo = request.form['hilo']      
    session['hilo'] = hilo
    inicio = session['inicio']
    hilo = hilo 
    buffer = buff(hilo)     
    if 'hilo' in session:
        print(session['inicio'])  
        print(session['hilo']) 
        print(buffer)             
        return render_template('buffer.html',buffer = buffer, hilo = hilo, inicio = inicio)



if __name__ == '__main__':
    app.run(debug=True)
