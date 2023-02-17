import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23348340"))
    API_HASH = os.environ.get("API_HASH", "1853e42ab1110b3d9cc62edfbe71e328")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6153156984:AAHm33bx3-kxVrnc7_YNePTLeo0r8EztCSw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOG8Bu3It-M490sOdrSh36K8-lT-VJELnn7OSBQ4mnuZutzP_nL2CwNq8XuWXcozkJOz259eWgtQwWOEqDbrHQqhWbMmc3CZzQ5IWV9-TSKUO6UuTIWOqC2krtvkUysVj_jj9o6wIi5g51XiCemoIZXjoA0RgsrRkXYgJkBj-NawoVJbhgGQfJx6qo2bDXEgz6U_DFAyI8FjrWSODaaZE8i8ijToX-lJJOLFEmXrroPCyTpDdl6l1ohqrICOl0Qs6tNHx_XDIM-_Pj53L4E0izKcP4c7S4j8DqEsgfWR74hkCaSBAPd7vAbTtwz83CB2RPrEyZ9q3MOVRcv8ixGBLxVUBeEE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MSMusicxBot")
    SUPPORT = os.environ.get("SUPPORT", "MSMusicxOfficial") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "MandSOfficial") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/7b183b3c528043786b47c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/7b183b3c528043786b47c.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5291970038")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
