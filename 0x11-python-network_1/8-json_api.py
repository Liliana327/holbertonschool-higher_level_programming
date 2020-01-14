#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
if __name__ == "__main__":

    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    data = {
        'q': q
    }

    q = ""
    if len(argv) == 2:
        q = argv[1]

    try:
        resp = requests.post(url, data).json()

        if resp:
            print('[{}] {}'.format(resp.get('id'), resp.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
