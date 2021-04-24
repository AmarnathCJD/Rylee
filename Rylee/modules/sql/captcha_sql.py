import threading
from Rylee.modules.sql import BASE, SESSION
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText, Numeric

class Captcha(BASE):
    __tablename__ = "csa"
    chat_id = Column(Numeric, primary_key=True)
    mode = Column(Boolean)
    time = Column(Integer)
    style = Column(UnicodeText)

    def __init__(self, chat_id, mode=True, time=0, style="button"):
        self.chat_id = chat_id
        self.mode = mode
        self.time = time
        self.style = style

    def __repr__(self):
        return "{}".format(self.chat_id)

Captcha.__table__.create(checkfirst=True)

C_LOCK = threading.RLock()
CAPTCHA_CHAT = {}

def set_captcha(chat_id, style):
 with C_LOCK:
  global CAPTCHA_CHAT
  curr = SESSION.query(Captcha).get(chat_id)
  if not curr:
      curr = Captcha(chat_id, True, 0, style)
  else:
      curr.mode = True
      curr.time = 0
      curr.style = style
  SESSION.add(curr)
  SESSION.commit()
  CAPTCHA_CHAT[str(chat_id)] = {
            "mode": True,
            "time": 0,
            "style": style
        }
  
def set_style(chat_id, style):
 with C_LOCK:
   global CAPTCHA_CHAT
   curr = SESSION.query(Captcha).get(chat_id)
   if not curr:
        return False
   curr.style = style
   SESSION.add(curr)
   SESSION.commit()

def set_mode(chat_id, mode):
 with C_LOCK:
   global CAPTCHA_CHAT
   curr = SESSION.query(Captcha).get(chat_id)
   if not curr:
        return False
   curr.mode = mode
   SESSION.add(curr)
   SESSION.commit()

def set_time(chat_id, time):
 with C_LOCK:
   global CAPTCHA_CHAT
   curr = SESSION.query(Captcha).get(chat_id)
   if not curr:
        return False
   curr.time = time
   SESSION.add(curr)
   SESSION.commit()

def __load_all_chats():
 global CAPTCHA_CHAT
 captcha = SESSION.query(Captcha).all()
 for x in feds:
            check = CAPTCHA_CHAT[x.chat_id]
            if check is None:
                CAPTCHA_CHAT[str(x.chat_id)] = []
            CAPTCHA_CHAT[str(chat_id)] = {
                "mode": x.mode,
                "time": x.time,
                "style": x.style,
        }

__load_all_chats()
