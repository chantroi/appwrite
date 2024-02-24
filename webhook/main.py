import json
import requests
from types import SimpleNamespace

def main(ctx):
    value = ctx.req.body_raw
    obj = json.loads(value, object_hook=lambda d: SimpleNamespace(**d))
    ctx.log(obj)
    jobj = json.loads(value)
    bot_token = ctx.req.query.get("bot")
    chat = ctx.req.query.get("chat")
    bot_api = "https://api.telegram.org/bot" + bot_token
    data = dict(chat_id=chat, text=f"```json\n{jobj}```")
    r = requests.post(bot_api + "/sendMessage", json=data)
    return ctx.res.json(r.json())