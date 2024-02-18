from .data import Note
import os
import names

notes = Note()
html_path = os.path.realpath(__file__).replace("main.py", "index.html")

def get(ctx):
    with open(html_path, "r") as f:
        html = f.read()
    if ctx.req.path == "/":
        note_content = ""
    else:
        note_name = ctx.req.path.split('/')[1]
        note_content = notes.get_note(note_name)
    return html.format(note_content)
       
def raw(ctx):
    if ctx.req.path ==  "/":
        return ""
    else:
        note_name = ctx.req.path.split('/')[1]
        return notes.get_note(note_name)
    
def post(ctx):
    data = ctx.req.body_raw
    url = ctx.req.url
    if not url.endswith("/"):
        url = url + "/"
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    if ctx.req.path == "/":
        note_name = names.get_first_name(gender='female').lower()
        notes.add_note(note_name, data)
        return url + note_name
    else:
        note_name = ctx.req.path.split('/')[1]
        try:
            notes.add_note(note_name, data)
        except Exception as e:
            ctx.error(e)
            notes.update_note(note_name, data)
        return url
    

def main(ctx):
    if ctx.req.method == "GET" and "Mozilla" in ctx.req.headers["user-agent"]:
        return ctx.res.send(get(ctx), 200, {"content-type": "text/html"})
    elif ctx.req.method == "GET":
        return ctx.res.send(raw(ctx), 200, {"content-type": "text/plain"})
    elif ctx.req.method == "POST":
        return ctx.res.redirect(post(ctx), 301)