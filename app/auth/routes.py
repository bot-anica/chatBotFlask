from app.auth import bp, controllers


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return controllers.login()


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return controllers.register()


@bp.route('/logout')
def logout():
    return controllers.logout()
