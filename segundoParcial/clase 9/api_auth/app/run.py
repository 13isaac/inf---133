from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.animal_controller import animal_bp
from controllers.user_controller import user_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

#JWTManager es una instancia que se usa para manejar la autenticacion basada en tokens JWT, proporciona funcionalidades para la creacion, verficacion y gestion de tokens JWT
#get_swaggerui_blueprint se usa para configurar la integracion de Swagger UI en la aplicacion Swagger UI es una herramienta que genera una interfaz interactiva para la documentacion y prueba de API

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "tu_clave_secreta_aqui"
# Configuración de la URL de la documentación OpenAPI
# Ruta para servir Swagger UI
SWAGGER_URL = "/api/docs"
# Ruta de tu archivo OpenAPI/Swagger
API_URL = "/static/swagger.json"


# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Zoológico API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

# Inicializa la extensión JWTManager
jwt = JWTManager(app)

# Registra los blueprints de animales y usuarios en la aplicación
app.register_blueprint(animal_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
