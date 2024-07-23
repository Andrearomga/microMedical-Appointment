from flask import Blueprint, jsonify as jsonIfy, request, make_response
from src.api.Infrestructure.Controllers.MedicalAppointmentsControllers.Create import CreateController
from src.api.Infrestructure.Controllers.MedicalAppointmentsControllers.ListAll import ListAllController
from src.api.Infrestructure.Controllers.MedicalAppointmentsControllers.Delete import DeleteController
from src.api.Infrestructure.MiddleWares.ProtectRoutes import token_required
from src.api.Infrestructure.Repository.MySQLMedicalAppointmentsRepository import MySQLMedicalAppointmentsRepository

repo = MySQLMedicalAppointmentsRepository()
create_controller = CreateController(repo)
list_all_controller = ListAllController(repo)
delete_controller = DeleteController(repo)

medical_appointments_routes = Blueprint('medical_appointments_route', __name__)

@medical_appointments_routes.route('/list/<int:IdBaby>', methods=['GET'])
# @token_required
def get_all(IdBaby):
    print("Obteniendo citas medicas")
    result = list_all_controller.run(IdBaby)
    if result:
        return jsonIfy(result[0])
    else:
        return jsonIfy({"value": []}), 404

@medical_appointments_routes.route('/save', methods=['POST'])
# @token_required
def create():
    return jsonIfy(create_controller.run(request)[0])

@medical_appointments_routes.route('/delete/<int:IdMedicalAppointment>', methods=['DELETE'])
# @token_required
def delete(IdMedicalAppointment):
    return jsonIfy(delete_controller.run(IdMedicalAppointment))


