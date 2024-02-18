from .data import Note
import os
import names

notes = Note()
html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="icon"
      href="https://icon-sets.iconify.design/favicon@32.png"
      type="image/png"
    />
    <title>Take Notes</title>
    <meta property="og:title" content="Take Notes" />
    <meta name="description" content="Take notes with simplicity" />
    <meta property="og:type" content="website" />
    <meta
      name="author"
      content="https://github.com/nghiepdev/freenote.deno.dev"
    />
    <meta
      property="og:image"
      content="https://images.unsplash.com/photo-1579208581155-feeb3bbb4e60?auto=format&fit=crop&w=1170&q=80"
    />
    <script src="https://unpkg.com/reconnectingwebsocket@1.0.0/reconnecting-websocket.min.js"></script>
    <style>
      * {
        margin: 0;
        padding: 0;
      }
      textarea {
        position: fixed;
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  <body>
    <textarea
      autofocus
      autocomplete="off"
      placeholder="Task a note..."
      aria-label="Take a note"
      spellcheck="false"
    >
{}</textarea
    >
    <script>
      const textarea = document.querySelector("textarea");

textarea.addEventListener("input", async (event) => {
  const value = event.target.value;
  const formData = new FormData();
  formData.append('value', value;)
  await fetch(window.location.href, {
    method: 'POST',
    body: formData,
  });
});
    </script>
  </body>
</html>
"""

def get(ctx):
    if ctx.req.path == "/" or not ctx.req.path:
        return html.replace("{}", "")
    else:
        note_name = ctx.req.path.split('/')[1]
        try:
            note_content = notes.get_note(note_name)
        except Exception as e:
            ctx.error(e)
            note_content = ""
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
    if ctx.req.path == "/" or not ctx.req.path:
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
    if "favicon" in ctx.req.path:
        return ctx.res.redirect("https://icon-sets.iconify.design/favicon@32.png", 301)
    if ctx.req.method == "GET" and "Mozilla" in ctx.req.headers["user-agent"]:
        return ctx.res.send(get(ctx), 200, {"content-type": "text/html"})
    elif ctx.req.method == "GET":
        return ctx.res.send(raw(ctx), 200, {"content-type": "text/plain"})
    elif ctx.req.method == "POST":
        return ctx.res.redirect(post(ctx), 301)