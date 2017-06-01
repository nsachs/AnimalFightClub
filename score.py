"""
Library for scoring with JJ

The scoring data is saved in a google spreadsheet here:
https://docs.google.com/spreadsheets/d/1SpQrJLBYssPFdoVdB7jft9e4WzW1g14X2Wj3yLVX_gw/edit

Username: animalfightclubscorekeeper@gmail.com
Password: dperiodisthebest

"""
identifier = 'AKfycbydbjC47B3VQQSz_YyaKYMGKr_J11EgsL5upH3A1oPQvSRKncvP'
url = 'https://script.google.com/macros/s/' + identifier + '/exec?'

from urllib import request


def get_scores():
    with request.urlopen(url + "type=fetch") as response:
        print(response.read())


def post_score(score):
    with request.urlopen(url + "type=post&score=" + str(score)) as response:
        print(response.read())


if __name__ == '__main__':
    post_score(40)
    get_scores()
