import time 
from typing import Dict 

import jwt 
from decouple import config 

JWT_SECRET = config("edd85cfad0ebf288263854d4279d0d22f717fd4a35b45c6f85af45c40ed50611") 
JWT_ALGORITHM = config("algorithm")

# Helper function for returning generated tokens
def token_response(token: str) -> dict:
    return {
        "access_token": token
    }