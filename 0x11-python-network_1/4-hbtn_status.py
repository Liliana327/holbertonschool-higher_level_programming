#!/usr/bin/python3
'''Python script that fetches https://intranet.hbtn.io/status'''

import requests

if __name__ == "__main__":

    '''url del servicio http'''
    url = 'https://intranet.hbtn.io/status'

    resp = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
