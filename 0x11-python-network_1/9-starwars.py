#!/usr/bin/python3
'''
Star Wars API # 0
'''
if __name__ == "__main__":

    import requests
    from sys import argv

    '''url del servicio http'''
    url = 'https://swapi.co/api/people'

    '''parametros de la consulta'''
    params = {
        'search': argv[1]
    }

    resp = requests.get(url, params=params).json()
    print("Number of results: {}".format(resp.get('count')))
    for i in resp.get('results'):
        print(i.get('name'))
