import os
from dotenv import load_dotenv

def load_env():
    """
    Load environment variables from a .env file into os.environ.
    """
    load_dotenv()  # does not override existing vars by default :contentReference[oaicite:3]{index=3}
    return {
        "OPENWEATHER_API_KEY": os.getenv("OPENWEATHER_API_KEY"),
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
    }
