from flask import request, jsonify
from src.api.Infrestructure.MiddleWares.functionJWT import validate_token

def token_required(f):
    def wrapper(*args, **kwargs):
        print("validando token")
        token = request.headers.get('token')
        print("token",token)
        if not token:
            return jsonify({"Message": "Acceso denegado", "status": 403})
        try:
            data = validate_token(token)
            print(data)
            # print(data)
            if(not not data): 
                return jsonify({"Message": "Acceso denegado", "status": 403})
            else: 
                pass
        except Exception as e:
            return jsonify({"Message": "Acceso denegado", "status": 403,data:str(e)})
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper
