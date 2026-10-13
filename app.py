from flask import Flask
from models.database import crear_base
from controllers.comision_controller import comision_bp

app = Flask(__name__)
app.register_blueprint(comision_bp)
crear_base()

if __name__ == "__main__":
    app.run(debug=True)
