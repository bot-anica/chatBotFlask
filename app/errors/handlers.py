from flask import render_template

from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    # To make sure that failed database sessions don't interfere with database accesses triggered by the template,
    # I issue a session rollback
    db.session.rollback()
    return render_template('errors/500.html'), 500
