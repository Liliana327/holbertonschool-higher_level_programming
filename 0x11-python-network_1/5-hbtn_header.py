#!/usr/bin/python3
'''Valor de encabezado de respuesta'''

if __name__ == "__main__":

    import requests
    from sys import argv

    '''url del servicio http'''
    resp = requests.get(argv[1])
    print(resp.headers.get('X-Request-Id'))
