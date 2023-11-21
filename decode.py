import jwt
import datetime

token = input("Enter your jwt token:\n")

secret_key = "scurryingrats"

try:
    decoded_token = jwt.decode(token, secret_key, algorithms="HS256")

    # Check if user is admin
    if decoded_token['user-role'] != "admin":
        raise Exception('Not Admin!')

    print("Token is valid!")
    print(decoded_token)
except Exception:
    print('Token is invalid')
