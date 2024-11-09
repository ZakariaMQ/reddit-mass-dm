from concurrent.futures import ThreadPoolExecutor
import random

from src.utils import get_data, AccountCycler, CONF
from interface.user_info import get_id
from interface.dm import send_dm
from src.logger import logger

proxies = get_data("proxies.txt")
messages = get_data("msgs.txt")
usernames = get_data("usernames.txt")
accounts_pool = AccountCycler(
   get_data("accounts.txt")
   )
max_workers = int(CONF["THREADS"]["NUMBER"])


def dms(username: str):
    try:
        user_id = get_id(username)
        if not user_id:
            logger.warning(f"Failed to get ID for username: [{username}]")
            return
        r = send_dm(
            proxy=random.choice(proxies),
            bearer=accounts_pool.get_next_account(),
            dm_msg=random.choice(messages),
            user_id=user_id
        )
        if r.get("success"):
            logger.info(f"Successfully DMed user: [{username}]")
        else:
            logger.warning(f"Failed to DM user: [{username}], Reason: [{r.get('reddit_response')}]")
    
    except Exception as e:
        logger.error(f"An error occurred while DMing user [{username}]: {e}")

def main():
   with ThreadPoolExecutor(max_workers=max_workers) as executor:
       executor.map(dms, usernames)

if __name__ == "__main__":
    main()