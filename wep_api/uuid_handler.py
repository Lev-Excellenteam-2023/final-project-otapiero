
import uuid

generated_uuids = []


def generate_uid():
    """
    Generate a unique identifier (UID) using UUID version 4 and store it in memory.
    """
    uid = str(uuid.uuid4())
    generated_uuids.append(uid)
    return uid


def is_valid_uid( uid ):
    """
    Check if a given string is a valid UUID and if it is already taken.
    """
    if not isinstance(uid, str):
        return False

    try:
        uuid_obj = uuid.UUID(uid)
        if uid in generated_uuids:
            return True
        return False
    except ValueError:
        return False
