from flask import Flask, render_template, request, url_for
from flask_babel import Babel
import datetime
import json
import os


app = Flask(__name__, static_url_path='/static')
babel = Babel(app)


app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['LANGUAGES'] = ['en', 'ru']  # List of supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language


def get_locale():
    # Get language from URL parameter or default to 'en'
    lang = request.args.get('lang', 'en')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    with open('media.json', 'r', encoding='utf-8') as json_file:
        media = json.load(json_file)

    photo_folder = os.path.join(app.static_folder, 'images', 'photos')
    photo_files = [filename for filename in os.listdir(photo_folder) if filename.endswith(('.jpg', '.png', '.JPG'))]
    photo_urls = [url_for('static', filename=os.path.join('images', 'photos', filename)).replace('%5C', '/') for filename in photo_files]
    current_year = datetime.datetime.now().year
    user_language = get_locale()
    print(photo_urls)
    return render_template('index.html',
                           media=media,
                           photos=photo_urls,
                           current_year=current_year,
                           user_language=user_language)


if __name__ == '__main__':
    app.run(debug=True)
