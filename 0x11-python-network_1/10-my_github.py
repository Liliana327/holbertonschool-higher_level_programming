#!/usr/bin/python3
'''Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
'''
if __name__ == "__main__":

    import requests
    from sys import argv

    '''url del servicio http'''
    url = 'https://api.github.com/user'

    '''parametros de la consulta'''
    params = {
        'username': argv[1],
        'password': argv[2]
    }

    resp = requests.get(url,  params=params)
    print(resp.json().get('id'))
