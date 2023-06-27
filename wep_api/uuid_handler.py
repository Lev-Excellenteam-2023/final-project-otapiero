
import uuid



def generate_uid():
    """
    Generate a unique identifier (UID) using UUID version 4 and store it in memory.
    """
    uid = str(uuid.uuid4())
    return uid


def is_valid_uid( uid ):
    """
    Check if a given string is a valid UUID and if it is already taken.
    """
    if not isinstance(uid, str):
        return False

    try:
        uuid_obj = uuid.UUID(uid)
        return True
    except ValueError:
        return False
