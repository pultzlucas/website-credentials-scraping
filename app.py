from flask import Flask, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
from credentials import get_favicon_credentials, get_website_description, get_website_title

app = Flask(__name__)


@app.route('/')
def get_info():
    try:
        if len(request.args) == 0 or request.args['url'] == '':
            return jsonify({
                'error': 'The website url must be specified.'
            })

        url = str(request.args['url'])
        html = str(requests.get(url).text)
        soup = BeautifulSoup(html, 'html.parser')

        title = get_website_title(html, url)
        tags_metadata = soup.find_all('meta')
        description = str(get_website_description(tags_metadata))
        favicon_credentials = get_favicon_credentials(url)

        return jsonify({
            'status': 'success',
            'title': title,
            'description': description,
            'favicon_url': favicon_credentials['url'],
            'favicon_file_extension': favicon_credentials['file_extension']
        })

    except Exception as error:
        return jsonify({
            'status': 'error',
            'error': str(error)
        })

@app.route('/default_icon')
def get_default_favicon():
    return send_file('default_icon.png', mimetype='image/png')


if __name__ == '__main__':
    port = 8080
    host = 'localhost'
    app.run(host, port, debug=True)
