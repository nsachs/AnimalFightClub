"""
Library for scoring with JJ
"""
url = 'https://script.google.com/macros/s/AKfycbzAHgTwxYYtFoMwzyXovL_IUbt62R4hBeoew1wUY4tU/exec?'

from urllib import request


def get_scores():
    with request.urlopen(url + "type=fetch") as response:
        print(response.read())


if __name__ == '__main__':
    get_scores()