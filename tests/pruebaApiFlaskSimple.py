#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     28/04/2022
# Copyright:   (c) LENOVO 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask,request,jsonify,\
 render_template,session
#import wikipedia
#import pymysql
#import requests
#import json
#import sqlite3
aplicacion=Flask(__name__)
#aplicacion.secret_key='miPalabraSecreta'
@aplicacion.route('/')
def bienvenida():
    #session['estaLogueado']='NO'
    return 'Bienvenido a la pagina'

@aplicacion.route('/miercoles')
def elMiercoles():
    return 'tercer dia habil de la semana'

@aplicacion.route('/python')
def muestraPython():
    return 'es un lenguaje de programacion'

@aplicacion.route('/numeros')
def muestraNumeros():
    diccionario={'1':{'español':'uno','ingles':'one'},
    '2':{'español':'dos','ingles':'two'},
    '3':{'español':'tres','ingles':'three'},
    '4':{'español':'cuatro','ingles':'four'}}
    numeroRecibido=request.args.get('elNumero')
    aplicacion.logger.info(f'numero recibido {numeroRecibido}')
    if numeroRecibido==None:
        respuesta=diccionario
    elif str(numeroRecibido) in diccionario.keys():
        respuesta=diccionario[str(numeroRecibido)]
    else:
        respuesta={'error':'numero no hallado'}
    return respuesta

@aplicacion.route('/numeros2')
def muestraNumeros2():
    diccionario={'1':{'español':'uno','ingles':'one'},
    '2':{'español':'dos','ingles':'two'},
    '3':{'español':'tres','ingles':'three'},
    '4':{'español':'cuatro','ingles':'four'}}
    numeroRecibido=request.args.get('elNumero')
    aplicacion.logger.info(f'numero recibido {numeroRecibido}')
    if numeroRecibido==None:
        respuesta=diccionario
    elif str(numeroRecibido) in diccionario.keys():
        respuesta=diccionario[str(numeroRecibido)]
    else:
        respuesta={'error':'numero no hallado'}

    return  jsonify(respuesta)



if __name__ == '__main__':
    aplicacion.run(host='0.0.0.0',port='8010',
    debug=True )
