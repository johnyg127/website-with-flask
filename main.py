from flask import Flask

server = Flask(__name__)


@server.route('/')
def first_web_page():
    return '<h1>Welcome to the tennis website that you just made!</h1><br/><br/><img src="https://photoresources.wtatennis.com/photo-resources/2019/08/15/dbb59626-9254-4426-915e-57397b6d6635/tennis-origins-e1444901660593.jpg?width=1200&height=630" width="500"></img>'

if __name__ == '__main__':
    server.run(debug=True, port=8000, host='0.0.0.0')