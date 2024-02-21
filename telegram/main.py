import json
import os

def main(context):
    data = context.req.body_raw
    context.log(data)
    bot = context.req.query.get("bot")
    os.system(f"curl https://api.telegram.org/bot{bot}/sendMessage?text=```json {data}```&chat_id=5665225938&parse_mode=markdown")
    return context.res.send(data)