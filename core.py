import logging
import os
import json

from dotenv import load_dotenv

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
STAT_FILE = 'statistics.json'


def load_stats():
    if not os.path.exists(STAT_FILE) or os.path.getsize(STAT_FILE) == 0:
        with open(STAT_FILE, 'w', encoding='utf-8') as file:
            json.dump({}, file)
            return {}
    else:
        with open(STAT_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)

def save_stats(stats):
    with open(STAT_FILE, 'w', encoding='utf-8') as file:
        json.dump(stats, file, indent=4)

def msg_count(user_id, username):
    stats = load_stats()

    if user_id not in stats:
        stats[user_id] = {"username": username, "messages_count": 0}
        save_stats(stats)
        return None
    else:
        stats[user_id]['messages_count'] += 1
        save_stats(stats)
        return stats[user_id]['messages_count']




