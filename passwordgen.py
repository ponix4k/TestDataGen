import string
import secrets

def create_password(stringLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    password =''.join(secrets.choice(chars) for i in range(stringLength))
    print(password)
create_password(20)