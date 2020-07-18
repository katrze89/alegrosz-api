from flask import Flask


def create_app():
    alegrosz = Flask(__name__)
    alegrosz.config['SECRET_KEY'] = b'\x1b<\x91(l\x10\xe4DiL\x03\xa7/\xf4\xe9\x95'
    from alegrosz.views import main_bp

    alegrosz.register_blueprint(main_bp)

    return alegrosz


app = create_app()
