# Renders the 1280x640 GitHub social preview cards into png/ using the constants in gen.py.
# Run: python3 gen-social.py && for f in png/social-*.svg; do inkscape "$f" --export-type=png --export-filename="${f%.svg}.png"; done
import os, tempfile

src = open("gen.py").read()
tmp = tempfile.mkdtemp(); cwd = os.getcwd(); os.chdir(tmp)
ns = {}; exec(src, ns)          # gen.py writes its SVGs on import; do that in a throwaway dir
os.chdir(cwd)
mark, wordmark, INK, CREAM, CRIMSON = ns["mark"], ns["wordmark"], ns["INK"], ns["CREAM"], ns["CRIMSON"]
FONT = "Inter, 'DejaVu Sans', sans-serif"

def card(name, tagline, stack):
    body = f'<rect width="1280" height="640" fill="{CREAM}"/>'
    body += mark(INK, CRIMSON, 140, 120, 2.6)
    body += f'<g transform="translate(430 265) scale(3.2)">{wordmark(INK, 0, 0, 44)}</g>'
    body += f'<text x="140" y="470" font-family="{FONT}" font-size="40" font-weight="500" fill="{INK}">{tagline}</text>'
    body += f'<text x="140" y="522" font-family="{FONT}" font-size="28" fill="{INK}" opacity="0.62">{stack}</text>'
    body += f'<text x="1140" y="590" font-family="{FONT}" font-size="22" fill="{CRIMSON}" text-anchor="end">github.com/madrileno-dev</text>'
    os.makedirs("png", exist_ok=True)
    open(f"png/{name}.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" width="1280" height="640">{body}</svg>\n')

card("social-backend", "AI-first Scala 3 backend template", "http4s · Skunk · cats-effect · Postgres · OpenTelemetry")
card("social-frontend", "React frontend template for the madrileno backend", "React 19 · TypeScript · Vite · TanStack Query · oRPC · shadcn/ui")
