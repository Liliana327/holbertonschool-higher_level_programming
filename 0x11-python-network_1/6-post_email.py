#!/usr/bin/python3
'''Response header value #1'''

if __name__ == "__main__":

    import requests
    from sys import argv

    '''parametros de la consulta'''
    params = {
        'email': argv[2]
    }

    resp = requests.post(argv[1], params)
    print(resp.text)
