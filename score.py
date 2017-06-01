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
    """
    Get the scores and output a list of all scores and names in dictionary form
    like this [{name:name1, score:score1},{name:name2, score:score2}, ... ]
    :return: a dictionary of scores which are previously saved
    """
    with request.urlopen(url + "type=fetch") as response:
        return eval(response.read())


def post_score(score, name):
    """
    posts the score and name and returns the google script result.
    :param score: 
    :param name: 
    :return: gs result
    """
    with request.urlopen(url + "type=post&score=" + str(score) + "&name=" + name.replace(" ", "_")) as response:
        print(response.read())


# FOR TESTING PURPOSES ONLY
if __name__ == '__main__':
    post_score(40, "test name")
    print(get_scores())

##########################################################################################
# The google script associated with the spreadsheet is pasted below for further reference.
"""
function doGet(e) {
  
  if(typeof e !== 'undefined')
    var data = JSON.parse(JSON.stringify(e.parameter))
    if(data.type == 'fetch')
      return ContentService.createTextOutput(dumpData());
    if(data.type == 'post')
      addRow([data.score, data.name]) // [col1, col2, col3, col4 ...]
      return ContentService.createTextOutput("Score of " + data.score + " for " + data.name + " added to saved scores.");
    return ContentService.createTextOutput("Not a valid request.");
}
function addRow(e) {
  var sheet = SpreadsheetApp.getActiveSheet();
  sheet.appendRow(e);
}
function dumpData() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var out = []
  for (var i = 1; i < data.length; i++) {
    out.push(JSON.stringify({score: data[i][0], name: data[i][1]}));
  }
  return out
}
"""
