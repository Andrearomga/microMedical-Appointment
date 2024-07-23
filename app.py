from flask import Flask, make_response
from src.api.Infrestructure.Routes.MedicalAppointmentsRoutes import medical_appointments_routes
from src.api.Infrestructure.Routes.ChatRoutes import chat_route
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(medical_appointments_routes, url_prefix='/medical-appointment')
app.register_blueprint(chat_route, url_prefix='/chat')

CORS(app, resources={r"/*": {"origins": "*"}})

def no_cache(view):
    def no_cache_wrapper(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    return no_cache_wrapper

# @app.before_request
# def log_request_info():
#     print(f"Ruta invocada: {request.path}")
#     print(f"Método: {request.method}")
#     print(f"Datos: {request.data}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
