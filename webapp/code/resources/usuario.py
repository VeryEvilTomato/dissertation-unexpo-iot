from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

class Usuario(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'usuario',
        type=str,
        required=True,
        help="El campo 'Usuario' no puede dejarse en blanco"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="El campo 'Contraseña' no puede dejarse en blanco"
    )

    def post(self):
        """Solicitud post para registrar usuarios"""
        datos = Usuario.parser.parse_args()

        if UsuarioModel.encontrar_por_usuario(datos['usuario']):
            return {"Mensaje": "El usuario ya existe"}, 400
        
        usuario = UsuarioModel(**datos)
        usuario.guardar_db()
        
        return {"Mensaje": "Usuario creado exitosamente"}, 201