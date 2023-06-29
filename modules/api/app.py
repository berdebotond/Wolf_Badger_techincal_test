import logging

import sqlalchemy
from flask import Flask, request, redirect, url_for
from flask.json import jsonify
from flask_dance.contrib.github import github
from flask_sqlalchemy import SQLAlchemy
from jsonschema import validate, ValidationError
from http import HTTPStatus
from sqlalchemy import exc

from modules.api.github_routes import github_blueprint
from modules.api.utils import user_schema_update, user_schema_create, check_auth
from modules.config.config import cfg
from modules.logger.logger import Logger

# init flask app
app = Flask(__name__)
app.secret_key = cfg.APP_SECRET_KEY

Logger.debug(f"client_id: {cfg.GITHUB_CLIENT_ID}")
Logger.debug(f"client_secret: {cfg.GITHUB_CLIENT_SECRET}")

# register github blueprint
app.register_blueprint(github_blueprint, url_prefix="/login")

# init db
app.config["SQLALCHEMY_DATABASE_URI"] = cfg.DB_URI
db = SQLAlchemy(app)

# possible errors messages
AUTH_ERROR = "Please login into your github first on page /login"
USER_NOT_FOUND_ERROR = "User not found"
USER_ALREADY_EXISTS_ERROR = "User already exists"

class User(db.Model):
    """
    User model for the database
    """
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True)
    location = db.Column(db.String(120))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def init_db():
    """
    Init the database
    :return:
    """
    with app.app_context():
        db.create_all()
        db.session.commit()

@app.route("/")
def login():
    """
    Login for github account using flask dance and init the db
    :return:
    """
    init_db()

    if not github.authorized:
        return redirect(url_for("github.login"))
    try:
        resp = github.get("/user")
    except Exception as e:
        #Could be duplicate data or any other issue related to db connection
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    assert resp.ok
    Logger.debug(f"resp: {resp.json()}")
    resp_data = resp.json()
    user = User(name=resp_data["name"], email=resp_data["email"], location=resp_data["location"], login=resp_data["login"])
    try:
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError as e:
        logging.warning(jsonify({"warning": str(e)}))

    return f'You are {resp_data["login"]} on GitHub', HTTPStatus.OK



@app.route('/user', methods=['POST'])
def create_user():
    """
    Create a new user if user is authenticated
    :return: User.id
    """
    if not check_auth():
        return AUTH_ERROR, HTTPStatus.UNAUTHORIZED
    data = request.get_json()
    try:
        validate(instance=data, schema=user_schema_create)
    except ValidationError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    user = User(**data)
    try:
        db.session.add(user)
        db.session.commit()
    except exc.IntegrityError as e:
        logging.warning(jsonify({"warning": str(e)}))
        return jsonify(USER_ALREADY_EXISTS_ERROR), HTTPStatus.CREATED

    return jsonify(user.id), HTTPStatus.CREATED


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    """
    Get a user by id
    :param id:
    :return: User
    """
    if not check_auth():
        return AUTH_ERROR, HTTPStatus.UNAUTHORIZED
    user = db.session.get(User, id)
    if user is None:
        return jsonify(error=USER_NOT_FOUND_ERROR), HTTPStatus.NOT_FOUND
    return jsonify(user.as_dict()), HTTPStatus.OK

@app.route('/users', methods=['GET'])
def get_users():
    """
    Get a user by id
    :return: User
    """
    if not check_auth():
        return AUTH_ERROR, HTTPStatus.UNAUTHORIZED
    users = db.session.query(User).all()
    if users is None:
        return jsonify(error=USER_NOT_FOUND_ERROR), HTTPStatus.NOT_FOUND
    return jsonify([user.as_dict() for user in users]), HTTPStatus.OK

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Update a user by id
    :param id:
    :return: User
    """
    if not check_auth():
        return jsonify(error=AUTH_ERROR), HTTPStatus.UNAUTHORIZED
    data = request.get_json()

    try:
        validate(instance=data, schema=user_schema_update)
    except ValidationError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

    user = db.session.get(User, id)
    if user is None:
        return jsonify(error=USER_NOT_FOUND_ERROR), HTTPStatus.NOT_FOUND
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.as_dict()), HTTPStatus.OK


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Delete a user by id
    :param id:
    :return:
    """
    if not check_auth():
        return AUTH_ERROR, HTTPStatus.UNAUTHORIZED
    user = db.session.get(User, id)
    if user is None:
        return jsonify(error=USER_NOT_FOUND_ERROR), HTTPStatus.NOT_FOUND
    db.session.delete(user)
    db.session.commit()
    return jsonify(success=True), HTTPStatus.NO_CONTENT


def start_app():
    app.run(host=cfg.APP_HOST, port=cfg.APP_PORT, debug=cfg.APP_DEBUG)


'''
Original way to implement quath2, but since I found a library in flask_dance that does it for me, I will use that instead
as it mentioned "- The amount of code written (less is more)"


authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    """Step 1: User Authorization.
    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    github = OAuth2Session(cfg.GITHUB_CLIENT_ID)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route("/login/github/authorized", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.
    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    github = OAuth2Session(cfg.GITHUB_CLIENT_ID, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=cfg.GITHUB_CLIENT_SECRET,
                               authorization_response=request.url)

    session['oauth_token'] = token
    return redirect(url_for('.profile'))

@app.route("/profile", methods=["GET"])
def profile():
    """Fetching a protected resource using an OAuth 2 token.
    """
    github = OAuth2Session(cfg.GITHUB_CLIENT_ID, token=session['oauth_token'])
    return jsonify(github.get('https://api.github.com/user').json())

'''
