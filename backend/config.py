from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

# === Percorsi base ===
BASE_DIR = Path(__file__).resolve().parent
ANNOUNCEMENTS_DIR = BASE_DIR / "announcements"
FUTURE_EVENTS_FILE = BASE_DIR / "future_events.json"
MAINTENANCE_FILE = BASE_DIR / "maintenance.json"
BANNER_FILE = BASE_DIR / "banner.json"
LOG_FILE = BASE_DIR / "log.txt"

# === Parametri campus / eventi ===
CAMPUS_ID = int(os.getenv("CAMPUS_ID", "30"))
CURSUS_ID = int(os.getenv("CURSUS_ID", "21"))
EVENT_LOOKAHEAD_DAYS = int(os.getenv("EVENT_LOOKAHEAD_DAYS", "7"))

# === Banner ===
BANNER_DEFAULT_VISIBLE = os.getenv("BANNER_DEFAULT_VISIBLE", "false").lower() == "true"
BANNER_DEFAULT_TEXT = os.getenv(
    "BANNER_DEFAULT_TEXT", "🔔 Attenzione: Manutenzione programmata il 17 dicembre"
)

# === OAuth 42 ===
OAUTH_AUTHORIZE_URL = os.getenv("OAUTH_AUTHORIZE_URL", "https://api.intra.42.fr/oauth/authorize")
OAUTH_TOKEN_URL = os.getenv("OAUTH_TOKEN_URL", "https://api.intra.42.fr/oauth/token")
OAUTH_API_BASE_URL = os.getenv("OAUTH_API_BASE_URL", "https://api.intra.42.fr")
OAUTH_CLIENT_ID = os.getenv("OAUTH_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("OAUTH_CLIENT_SECRET")
OAUTH_REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI", "https://monitor.42roma.it/callback")

# === SSL e host ===
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH", "/etc/ssl/42roma.it.crt")
SSL_KEY_PATH = os.getenv("SSL_KEY_PATH", "/etc/ssl/wildcard.key")
HOST = os.getenv("FLASK_HOST", "monitor.42roma.it")
PORT = int(os.getenv("FLASK_PORT", "443"))

# === Servizi esterni ===
SITE = os.getenv("URL", "")
OFFLINE_LOCATIONS = f"{SITE}/offline"
ONLINE_LOCATIONS = f"{SITE}/online"
GET_EVENTS = f"{SITE}/get"
NAGIOS_URL = os.getenv("NAGIOS_URL")

# === Autorizzazioni ===
AUTHORIZED_USERS = os.getenv("AUTHORIZED_USERS", "ffrau").split(",")
