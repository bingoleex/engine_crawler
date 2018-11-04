import logzero
from logzero import logger
from flask import Flask, jsonify, render_template
from flask import request

application = Flask(__name__)

@application.route('/result')
def get_result():
    logger.info(request.args['keywords'])
    crawl(request.args['keywords'])
    res = parse_google_html(open('response.txt', 'r', encoding='utf-8'))
    logger.info(res)
    return render_template('result.html', result=res)


@application.route('/')
def show_entries():
    return render_template('index.html')
    
if __name__ == '__main__':
    application.run(debug=True)
