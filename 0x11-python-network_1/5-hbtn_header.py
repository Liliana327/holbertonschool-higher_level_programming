#!/usr/bin/python3
'''Valor de encabezado de respuesta'''

if __name__ == "__main__":

    import requests
    from sys import argv

    '''url del servicio http'''
    url = 'https://intranet.hbtn.io/status'

    resp = requests.get(url)
    print(resp.headers.get('X-Request-Id'))
