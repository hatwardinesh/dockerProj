from flask import Flask


app = Flask(__name__)


@app.route('/')
def dockerWelcome():
    return "Hellow from Docker"


if __name__ == '__main__':
    app.logger.info("Track 1.1")
    app.run(host = '0.0.0.0',debug=True)    
