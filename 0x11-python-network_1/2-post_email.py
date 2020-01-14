#!/usr/bin/python3
'''script script to read my status
'''
if __name__ == "__main__":

    from urllib import request, parse
    from sys import argv

    '''url del servicio http'''
    url = argv[1]

    '''parametros de la consulta'''
    params = {
        'email': argv[2]
    }

    '''consulta con parametros'''
    consulta = parse.urlencode(params)

    u = consulta.encode('ascii')

    resp = request.Request(url, consulta)

    with request.urlopen(resp) as response:
        print(response.read().decode('utf-8'))
