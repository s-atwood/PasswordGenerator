from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache
from dotenv import load_dotenv
from pathlib import Path
from .passphrase.generate_passphrase import generate_passphrase
from .random_api.random_indices import get_random_indices
from .word_loader.load_words import load_words_from_json
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
FILE_PATH = Path('english_corpus.json')


def create_app(test_config=None):
    cache = Cache(config={'CACHE_TYPE': 'simple'})
    app = Flask(__name__, instance_relative_config=True)
    cache.init_app(app)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        CACHE_DEFAULT_TIMEOUT = 60 * 15,
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # laod the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET'])
    @cache.cached(timeout=1)
    def home():
        words = load_words_from_json(FILE_PATH)
        random_indices = get_random_indices(API_KEY, 5, 0, len(words)-1)
        passphrase = generate_passphrase(words, random_indices)
        return jsonify({'Your passphrase': passphrase})
        # x = {"members": ["member1", "member2"]}
        # y = {"something", "somethingelse"}
        # return jsonify(x)
    
    return app
    