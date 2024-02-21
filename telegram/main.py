import json
import requests

def main(context):
    data = context.req.body_raw
    context.log(data)
    bot = context.req.query.get("bot")
    res = requests.get(f"https://api.telegram.org/bot{bot}/sendMessage", params={"text": f"```json {data}```", "chat_id": 5665225938, "parse_mode": "markdown"})
    context.log(res.text)
    return context.res.send(data)