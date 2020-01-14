#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
if __name__ == "__main__":

    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    params = {
        'q': q
    }

    q = argv[1] if len(argv) > 1 else ""
    try:
        resp = requests.post(url, params).json()
        if 'id' in resp or 'name' in resp:
            print("[{}] {}".format(resp['id'], resp['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
