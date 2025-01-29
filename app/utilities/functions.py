import bcrypt
from app.database import models


def encrypt_password(password):
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(
        password=encoded_password,
        salt=salt
    )
    return hash_password


def check_credentials(email_id,password,db):
    emailids_in_db = db.query(models.Users.email_id).all()
    existing_emailids = []
    for email in emailids_in_db:
        existing_emailids.append(email[0])
    if email_id in existing_emailids:
        password_from_db = db.query(models.Users).filter(
            models.Users.email_id==email_id
        ).first()
        verified = bcrypt.checkpw(password.encode('utf-8'),password_from_db.password)
        if verified:
            return "Login Successful."
        else :
            return f"Password does not match. Login Failed."
    else:
        return f"{email_id} is not registered."
