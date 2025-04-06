import hashlib
from datetime import datetime


def hash_id(id_tg_user: int, created_at: float) -> str:
    """
    Hash id for task model from id_tg_user and created_at
    """
    hash_object = hashlib.sha256()
    hash_object.update(f"{id_tg_user}{created_at}".encode())
    hex_dig = hash_object.hexdigest()

    return hex_dig
