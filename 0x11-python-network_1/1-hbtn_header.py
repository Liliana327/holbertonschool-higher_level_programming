#!/usr/bin/python3
'''Valor de encabezado de respuesta'''

from urllib import request
import sys

'''url del servicio http'''
with request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
