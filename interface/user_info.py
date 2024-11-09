import httpx

from src.logger import logger
from .consts import headers

def get_id(username: str):
    url = "https://reddapi.p.rapidapi.com/api/user_info"
    params = {"username": username}
    logger.info(f"getting user ID for username: {username}")
    
    try:
        r = httpx.get(url, headers=headers, params=params)
        if r.status_code == 200:
            user_id = r.json().get("data", {}).get("id", "")
            if user_id:
                logger.info(f"Successfully got user ID for username: {username}")
            else:
                logger.warning(f"No user ID found for username: {username}")
            return user_id
        else:
            logger.error(f"Failed to get user ID for username: {username}, HTTP Status: {r.status_code}")
            return ""
        
    except httpx.RequestError as e:
        logger.error(f"An error occurred while fetching user ID for username: {username}, Error: {e}")
        return ""
