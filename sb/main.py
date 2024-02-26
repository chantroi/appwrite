from seleniumbase import SB

def get_url(url):
    with SB(browser="firefox", headless=False, save_screenshot=True) as sb:
        sb.open(url)
        sb.save_screenshot("screenshot.png")

def main(ctx):
    url = ctx.req.query.get("url")
    if url:
        get_url(url)
        with open("screenshot.png", "rb") as f:
            return ctx.res.send(f.read(), 200, {'Content-Type': 'image/png'})
    else:
        return ctx.res.send("Please provide a URL in the 'url' query parameter.")