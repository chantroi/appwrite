import json
import requests
from types import SimpleNamespace

def main(context):
    data = context.req.body
    data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    context.log(data)
    bot = context.req.query.get("bot")
    res = requests.get(f"https://api.telegram.org/bot{bot}/sendMessage", params={"text": f"```json\n{data}```", "chat_id": data.message.chat.id, "parse_mode": "markdown"})
    context.log(res.text)
    return context.res.send(data)