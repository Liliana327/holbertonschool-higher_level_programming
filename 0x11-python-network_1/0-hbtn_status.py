#!/usr/bin/python3
'''script script to read my status
'''
from urllib import request

'''url del servicio http'''
url = 'https://intranet.hbtn.io/status'

with request.urlopen(url) as response:
    html_body = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html_body)))
    print('\t- content: {}'.format(html_body))
    print('\t- utf8 content: {}'.format(html_body.decode('utf -8')))
