#!/usr/bin/python3
'''script script to read my status
'''
if __name__ == "__main__":

    from urllib import request, parse
    from sys import argv

    '''url del servicio http'''
    url = 'https://intranet.hbtn.io/status'

    '''parametros de la consulta'''
    params = {
        'email': argv[2]
    }

    '''consulta con parametros'''
    consulta = parse.urlencode(params)

    '''creacion de la solicitud'''
    u = request.urlopen('{}?{}'.format(url, consulta))

    '''lectura de la respuesta'''
    respuesta = u.read()

    '''imprimir la respuesta en formato legible'''
    print(respuesta.decode('utf-8'))
