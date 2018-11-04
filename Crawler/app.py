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
    with open('360.txt', 'r', encoding='utf-8') as f:
        # with open('resss.html', 'r', encoding='utf-8') as f:
        # logger.info(parse_google_html(f))
        parse_so_com_html(f)

# logger.info(requests.head('http://www.baidu.com/link?url=9jAA6m4WmL6oNBz5Hx-L8bq39QbfS1ZPmDdXvqiNFAu').headers['location'])
# crawl('hello')
# application.run(host='0.0.0.0')
