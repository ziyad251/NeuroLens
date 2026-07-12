from typing import Tuple
from pymongo import MongoClient

from backend.config import get_settings

_client: MongoClient | None = None

def get_mongo() -> Tuple[MongoClient, object]:
    """
    Returns (client, db). Uses a simple module-level cached client.
    """
    global _client
    settings = get_settings()

    if _client is None:
        _client = MongoClient(settings.MONGODB_URI)

    db = _client[settings.MONGODB_DB]
    return _client, db
