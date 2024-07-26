import requests

def validate_token(token: str):
    
    print(token)
    
    url = "http://autentication:7000/user/validate/token"    
    payload = {
        "token": token,
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:        
        data = response.json()        
        return data["value"]    
    else:
        print(f"Error en la petición: {response.status_code}")
        return False

