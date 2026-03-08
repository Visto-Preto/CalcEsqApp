from flask import Flask

from routes.portas import portas_bp
from routes.janelas import janelas_bp
from routes.extras import extras_bp
from routes.portagiro import portagiro_bp

app = Flask(__name__)

app.register_blueprint(portas_bp)
app.register_blueprint(janelas_bp)
app.register_blueprint(extras_bp)
app.register_blueprint(portagiro_bp)


@app.route("/")
def home():
    from flask import render_template
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")