"""
BASE CONFIG FILE
"""

import os
from dotenv import load_dotenv

load_dotenv()

# api-web.nhle.com/ config
BASE_URL_API_WEB = os.getenv("BASE_URL_API_WEB", "https://api-web.nhle.com/")
V  = os.getenv("VERSION", "v1")

# api.nhle.com/stats/rest/ config
BASE_URL_STATS_REST = os.getenv("BASE_URL_STATS_REST", "https://api.nhle.com/stats/rest/")
LAN = os.getenv("LAN", "en")