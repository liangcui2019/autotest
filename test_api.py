import flask
import json
from flask import request

server = flask.Flask(__name__)


@server.route('/login', methods=['get', 'post'])
def login():
    username = request.values.get('name')
    pwd = request.values.get('pwd')
    if username and pwd:
        if username == 'xiaoming' and pwd == '111':
            resu = {'code': 200, 'message': 'login successfully'}
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'code': -1, 'message': 'username or password wrong'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': 'parameter can not be empty'}
        return json.dumps(resu, ensure_ascii=False)

if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')
