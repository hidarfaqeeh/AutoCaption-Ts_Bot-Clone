import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "odaygholy")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 485527614 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
