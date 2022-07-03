import requests, json
def solve(sid, sis):

    r = sis.get(url=f'https://onnxrt.herokuapp.com/solve?sid={sid}').json()
    captxt, capsid = r['text'], r['sid']

    return captxt, capsid
