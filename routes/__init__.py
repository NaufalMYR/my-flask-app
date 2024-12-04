def register_routes(app):
    from .auth import auth_bp
    from .scan import scan_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(scan_bp, url_prefix='/scan')
