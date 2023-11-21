import datetime
import jwt

iat = datetime.datetime.utcnow()
exp = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

payload = {
    "sub": "123456789",
    "iss": "example-app",
    "iat": iat,
    "exp": exp,
    "user-role": "admin"
}

secret_key = "scurryingrats"

token = jwt.encode(payload, secret_key, algorithm="HS256")

print(token)