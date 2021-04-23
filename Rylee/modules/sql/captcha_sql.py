import threading
from Rylee.modules.sql import BASE, SESSION
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText

class Captcha(BASE):
    __tablename__ = "ct"
    chat_id = Column(String(14), primary_key=True)
    mode = Column(UnicodeText)
    time = Column(Integer)
    style = Column(UnicodeText)
    
    def __init__(self, chat_id, mode, time, style):
        self.chat_id = chat_id
        self.mode = mode
        self.time = time
        self.style = style
        
        
Captcha.__table__.create(checkfirst=True)

C_LOCK = threading.RLock()
CAPTCHA_CHAT = {}

def set_captcha(chat_id, style):
 with C_LOCK:
  global CAPTCHA_CHAT
  captcha = Captcha(
            chat_id,
            "on",
            0,
            style,
  )
  SESSION.add(captcha)
  SESSION.commit()
  CAPTCHA_CHAT = {
    "chat_id": chat_id,
    "mode": "on",
    "time": 0,
    "style": style,
  }
  return captcha
  
def update_style(chat_id, style)
 with C_LOCK:
  global CAPTCHA_CHAT
  captcha = SESSION.query(Captcha).get(chat_id)
  if not captcha:
        return False
  captcha.style = style
  SESSION.commit()
  CAPTCHA_CHAT[str(chat_id)]["style"] = style

def update_time(chat_id, time)
 with C_LOCK:
  global CAPTCHA_CHAT
  captcha = SESSION.query(Captcha).get(chat_id)
  if not captcha:
        return False
  captcha.time = time
  SESSION.commit()
  CAPTCHA_CHAT[str(chat_id)]["time"] = time


def update_mode(chat_id, mode)
 with C_LOCK:
  global CAPTCHA_CHAT
  captcha = SESSION.query(Captcha).get(chat_id)
  if not captcha:
        return False
  captcha.mode = mode
  SESSION.commit()
  CAPTCHA_CHAT[str(chat_id)]["mode"] = mode

def get_style(chat_id):
    get = CAPTCHA_CHAT.get(str(chat_id))
    if get is None:
        return False
    return get["style"]

def get_mode(chat_id):
    get = CAPTCHA_CHAT.get(str(chat_id))
    if get is None:
        return False
    return get["mode"]

def get_time(chat_id):
    get = CAPTCHA_CHAT.get(str(chat_id))
    if get is None:
        return False
    return get["time"]

def _load_all_captcha():
 global CAPTCHA_CHAT
 try:
  captcha = SESSION.query(Captcha).all()
  for x in captcha:
    check = CAPTCHA_CHAT.get(x.chat_id)
    if check is None:
         FEDERATION_BYFEDID[x.chat_id] = []
    FEDERATION_BYFEDID[str(x.chat)] = {
                "mode": x.mode,
                "time": x.time,
                "style": x.style,
            }
 finally:
        SESSION.close()

_load_all_captcha()
