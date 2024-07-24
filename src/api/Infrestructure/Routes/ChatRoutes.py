from flask import Blueprint, jsonify as jsonIfy, request
from src.api.Infrestructure.Controllers.chat.Create import CreateController
from src.api.Infrestructure.Controllers.chat.ListAll import ListAllController
from src.api.Infrestructure.MiddleWares.ProtectRoutes import token_required

from src.api.Infrestructure.Repository.MySQLChatRepository import MySQLChatRepository

repo = MySQLChatRepository()
create_controller = CreateController(repo)
list_all_controller = ListAllController(repo)
# delete_controller = DeleteController(repo)

chat_route = Blueprint('chat_route', __name__)

@chat_route.route('/list', methods=['GET'])
# @token_required
def get_all():    
    return jsonIfy(list_all_controller.run())

@chat_route.route('/save', methods=['POST'])
# @token_required
def create_chat():
    return jsonIfy(create_controller.run(request)[0])

# @medical_appointments_routes.route('/delete/<int:IdMedicalAppointment>', methods=['DELETE'])
# @token_required
# def delete(IdMedicalAppointment):
#     return jsonIfy(delete_controller.run(IdMedicalAppointment))


