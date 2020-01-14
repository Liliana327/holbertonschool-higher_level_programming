#!/usr/bin/python3
'''Código de error # 1 
'''
if __name__ == "__main__":

    import requests
    from sys import argv

    '''url del servicio http'''
    url = argv[1]

    resp = requests.get(url)
    if resp.error >= 400:
        print("Error code: {}".format(resp.error))
    else:
        print(resp.text)
