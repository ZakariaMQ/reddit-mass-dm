from src.utils import CONF

headers = {
    "x-rapidapi-key": CONF["REDDAPI"]["API"],
    "x-rapidapi-host": "reddapi.p.rapidapi.com",
    "Content-Type": "application/json"
}
