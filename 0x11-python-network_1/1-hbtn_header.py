#!/usr/bin/python3
'''Valor de encabezado de respuesta'''

if __name__ == "__main__":

    from urllib import request
    from sys import argv

    '''url del servicio http'''
    resp = request.Request(argv[1])
    with request.urlopen(resp) as response:
        print(response.headers.get('X-Request-Id'))
