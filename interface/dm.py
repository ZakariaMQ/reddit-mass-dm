import httpx

from src.logger import logger
from .consts import headers

def send_dm(proxy: str, bearer: str, dm_msg: str, user_id: str) -> dict:
    url = "https://reddapi.p.rapidapi.com/api/dm"
    payload = {
        "proxy": proxy,
        "bearer": bearer,
        "dm_msg": dm_msg,
        "user_id": user_id
    }
    logger.info(f"sending DM to user ID: {user_id} with message: [{dm_msg[:30]}]...")
    return httpx.post(url, json=payload, headers=headers).json()
