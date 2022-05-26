import requests, ast
def solve(sid):
    r = requests.get(f'https://onnxrt.herokuapp.com/solve?sid={sid}')
    resp = dict(ast.literal_eval(r.text))
    captxt, capsid = resp['text'], resp['sid']
    return captxt
