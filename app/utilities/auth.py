import jwt
from fastapi import HTTPException,Security,status
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"])
    secret = 'MY_SECRET'

    def encode_token(self,user_id):
        payload = {
            'exp':datetime.now(timezone.utc)+timedelta(days=0,minutes=10),
            'iat':datetime.now(timezone.utc),
            'sub':user_id
        }
        print(datetime.now())
        return jwt.encode(
            payload,self.
            secret,
            algorithm='HS256'
        )
    
    def decode_token(self,token):
        try:
            print(token,self.secret)
            payload = jwt.decode(token,self.secret,algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Signature has expired.')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid Token.')
            
    def auth_wraper(self,auth:HTTPAuthorizationCredentials=Security(security)):
        return self.decode_token(auth.credentials)
    