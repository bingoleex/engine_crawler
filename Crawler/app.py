import logzero
from logzero import logger
from flask import Flask, jsonify, render_template
from flask import request
from crawl import Crawl

application = Flask(__name__)

@application.route('/result')
def get_result():
    logger.info(request.args['keywords'])
    crawl = Crawl()
    result = crawl.crawl(request.args['keywords'])
    logger.info(result)
    return render_template('result.html', result=result)

@application.route('/')
def show_entries():
    return render_template('index.html')
    
if __name__ == '__main__':
    application.run(debug=True)
