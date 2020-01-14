#!/usr/bin/python3
'''script script to read my status
'''
if __name__ == "__main__":

    from urllib import request, error
    from sys import argv

    '''url del servicio http'''
    url = argv[1]

    resp = request.Request(url)

    try:
        with request.urlopen(resp) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
