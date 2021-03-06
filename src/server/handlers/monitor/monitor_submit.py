from flask_restful import Resource, reqparse
from server.models.monitor import MonitorModel
from server.handlers.user.users import UserModel
from flask_jwt import jwt_required


class MonitorSubmit(Resource):
    """Clase para agregar un monitor al sistema"""
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Todo monitor necesita un nombre"
    )
    parser.add_argument(
        'variable',
        type=str,
        required=True,
        help="Todo monitor observa una variable"
    )

    @jwt_required()
    def post(self,id_user):
        """Solicitud para guardar un Monitor nuevo en la base de datos"""

        req = MonitorSubmit.parser.parse_args()

        if MonitorModel.find_by_name_id(req["name"],id_user):
            return {"mensaje": "Un monitor con ese nombre ya existe"},400
        if not UserModel.find_by_id(id_user):
            return {"mensaje": "El ID de usuario no existe"},400
        
        monitor = MonitorModel(id_user,**req)
        
        try:
            monitor.save_db()
        except:
            return { "mensaje": "Un error ha ocurrido insertando este monitor"},500

        return {"mensaje": "Monitor creado exitosamente"},201


        
