"""
Github OAuth2.0
"""

from flask_dance.contrib.github import make_github_blueprint, github

from modules.config.config import cfg

github_blueprint = make_github_blueprint(
    client_id=cfg.GITHUB_CLIENT_ID,
    client_secret=cfg.GITHUB_CLIENT_SECRET,
)


