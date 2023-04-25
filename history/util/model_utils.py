import string
import secrets

def randomId():
    alphabet = string.ascii_letters + string.digits
    id = ''.join(secrets.choice(alphabet) for i in range(126))
    print(f'id({len(id)}): {id}')
    return id

