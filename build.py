"""Generate the SVG panels of the profile README. Run: python build.py"""
import html
import pathlib

G, GD, GF, SAGE, INK, AMB = "#39ff7a", "#2bbf5c", "#1c7a3c", "#5f8d68", "#eafff1", "#ffd24a"
MONO = "'JetBrains Mono','IBM Plex Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',Menlo,monospace"
W = 1200

ART = """███╗   ███╗ █████╗  ██████╗  ██████╗ ███╗   ███╗██╗███╗   ██╗
████╗ ████║██╔══██╗██╔════╝ ██╔═══██╗████╗ ████║██║████╗  ██║
██╔████╔██║███████║██║  ███╗██║   ██║██╔████╔██║██║██╔██╗ ██║
██║╚██╔╝██║██╔══██║██║   ██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝""".split("\n")

AVATAR = """▄▄▄▄▄▄▄▄▄▄▄
█ ▄▄▄ ▄▄▄ █
█ █ █ █ █ █
█ █▄█ █▄█ █
█         █
█  ▀▀▀▀▀  █
█▄▄▄▄▄▄▄▄▄█
  ▀▀   ▀▀""".split("\n")

NEOFETCH = [
    ("OS", "Human (agentic build)"),
    ("Host", "Cad&Lan, building automation"),
    ("Role", "Agentic programmer"),
    ("Shell", "Claude Code, PowerShell, Git Bash"),
    ("Stack", "Python, TypeScript, Next.js, PostgreSQL"),
    ("Focus", "agents that ship code with tests and CI"),
    ("Status", "shipping at Cad&Lan"),
]

STACK = [("agents + CI", 90), ("Python", 85), ("TypeScript", 80), ("GitHub Actions", 80),
         ("Next.js / React", 75), ("PostgreSQL", 70), ("Ableton Live", 60)]


def frame(h, title, body, extra_style=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{html.escape(title)}">
<style>
  text {{ font-family: {MONO}; }}
  .ui {{ font-size: 15px; fill: {G}; }} .dim {{ font-size: 13px; fill: {SAGE}; }}
  .cur {{ fill: {G}; animation: blink 1.1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
  {extra_style}
</style>
<defs>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" y="3" fill="#000" fill-opacity=".45"/></pattern>
  <radialGradient id="wash1" cx="1" cy="0" r="0.9"><stop offset="0" stop-color="{G}" stop-opacity=".10"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient>
  <filter id="glow" x="-5%" y="-20%" width="110%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="{W}" height="{h}" fill="#000000"/><rect width="{W}" height="{h}" fill="url(#wash1)"/>
<rect x="24" y="24" width="{W-48}" height="{h-48}" rx="8" fill="#050805" stroke="#1f4d1f" stroke-width="1.5" filter="url(#glow)"/>
{body}
<rect x="24" y="24" width="{W-48}" height="{h-48}" rx="8" fill="url(#scan)"/>
</svg>'''


def header():
    H = 430

    def lines(cls):
        return "\n".join(
            f'<text class="{cls}" style="animation-delay:{0.25+i*0.18:.2f}s" x="70" y="{138+i*32}" xml:space="preserve">{html.escape(l)}</text>'
            for i, l in enumerate(ART))

    tag = "agentic programmer · software built with AI agents, tests and CI"
    style = f'''
  .l {{ font-size: 26px; fill: {INK}; opacity: 0; animation: reveal .01s steps(1) forwards; }} .l.g {{ fill: {G}; }}
  .gl {{ animation: glitch 7s infinite; }} .tag {{ font-size: 18px; fill: {G}; }}
  .amb {{ fill: {AMB}; animation: blink 1.1s steps(1) infinite; }} .sweep {{ animation: sweep 6s linear infinite; }}
  .typed {{ transform-origin: {W-70}px 0; animation: typing 2.2s steps(64) 1.6s reverse both; }}
  @keyframes reveal {{ to {{ opacity: 1; }} }}
  @keyframes sweep {{ from {{ transform: translateY(-40px); }} to {{ transform: translateY({H}px); }} }}
  @keyframes typing {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
  @keyframes glitch {{ 0%,86%,100% {{ transform: translate(0,0); opacity:0; }} 87% {{ transform: translate(-4px,1px); opacity:.8; }} 89% {{ transform: translate(3px,-1px); opacity:.8; }} 91% {{ transform: translate(-2px,0); opacity:.6; }} 93% {{ transform: translate(0,0); opacity:0; }} }}'''
    body = f'''<defs><linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{G}" stop-opacity="0"/><stop offset=".5" stop-color="{G}" stop-opacity=".12"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></linearGradient></defs>
<rect x="24" y="24" width="{W-48}" height="34" rx="8" fill="#070b07"/><line x1="24" y1="58" x2="{W-24}" y2="58" stroke="#143614"/>
<circle cx="48" cy="41" r="6" fill="#ff5f56"/><circle cx="68" cy="41" r="6" fill="#ffbd2e"/><circle cx="88" cy="41" r="6" fill="#27c93f"/>
<text class="dim" x="110" y="46"><tspan fill="{INK}">magomin</tspan>@github: ~/dev</text>
<circle class="amb" cx="{W-250}" cy="41" r="4"/><text class="dim" x="{W-238}" y="46" fill="{AMB}">shipping at Cad&amp;Lan</text>
<text class="ui" x="70" y="88" xml:space="preserve"><tspan fill="{SAGE}">magomin~/dev $</tspan> whoami --full</text>
<g class="gl" filter="url(#glow)">{lines("l g")}</g>
<g filter="url(#glow)">{lines("l")}</g>
<text class="tag" x="70" y="362" xml:space="preserve" filter="url(#glow)"><tspan fill="{SAGE}">&gt;</tspan> {html.escape(tag)}</text>
<rect class="typed" x="70" y="344" width="{W-140}" height="26" fill="#050805"/>
<text class="dim" x="70" y="392" xml:space="preserve">[x] Cad&amp;Lan   [x] re-track   [x] matdomi.vercel.app</text>
<rect class="cur" x="783" y="348" width="10" height="18"/>
<rect class="sweep" x="24" width="{W-48}" height="40" fill="url(#bar)"/>'''
    return frame(H, "MAGOMIN, Matthieu Dominguez, agentic programmer", body, style)


def neofetch():
    H = 300
    body_lines = AVATAR[:-1]
    av = "\n".join(
        f'<text x="70" y="{112+i*20}" font-size="17" fill="{G}" xml:space="preserve">{html.escape(l)}</text>'
        for i, l in enumerate(body_lines))
    fy = 112 + len(body_lines) * 20
    feet = (f'<g class="lf"><text x="70" y="{fy}" font-size="17" fill="{G}" xml:space="preserve">  ▀▀</text></g>'
            f'<g class="rf"><text x="70" y="{fy}" font-size="17" fill="{G}" xml:space="preserve">       ▀▀</text></g>')
    kv = "\n".join(
        f'<text x="340" y="{112+i*22}" font-size="15" xml:space="preserve"><tspan fill="{G}">{k:<8}</tspan><tspan fill="{AMB if k == "Status" else SAGE}">{html.escape(v)}</tspan></text>'
        for i, (k, v) in enumerate(NEOFETCH))
    sw = "".join(
        f'<rect x="{340+i*30}" y="{112+len(NEOFETCH)*22+2}" width="24" height="12" fill="{c}"/>'
        for i, c in enumerate(["#050805", "#ff5f56", G, AMB, "#5cf6ff", GD, GF, INK]))
    # idle sway: weight shifts from one foot to the other, figure stays in place
    style = '''
  .bob, .lf, .rf { transform-box: fill-box; transform-origin: 50% 100%; }
  .bob { animation: sway 1.6s ease-in-out infinite; }
  .lf { animation: lift 1.6s ease-in-out infinite; }
  .rf { animation: lift 1.6s ease-in-out -.8s infinite; }
  @keyframes sway { 0%,100% { transform: translateX(-4px) rotate(-2.5deg); } 50% { transform: translateX(4px) rotate(2.5deg); } }
  @keyframes lift { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-3px); } }'''
    body = f'''<text class="ui" x="70" y="64" xml:space="preserve"><tspan fill="{SAGE}">magomin~/dev $</tspan> neofetch</text>
<g filter="url(#glow)"><g class="bob">{av}</g>{feet}</g>
<text x="70" y="{fy+26}" class="dim">magomin@dev</text>
<text x="340" y="88" font-size="15" fill="{INK}" filter="url(#glow)">magomin@github</text><line x1="340" y1="94" x2="760" y2="94" stroke="{GF}"/>
{kv}{sw}'''
    return frame(H, "neofetch: identity card of Matthieu Dominguez", body, style)


def stack():
    H = 110 + len(STACK) * 30 + 30
    rows = ""
    for i, (name, pct) in enumerate(STACK):
        y = 110 + i * 30
        rows += f'''<text x="70" y="{y+4}" font-size="15" fill="{SAGE}">{html.escape(name)}</text>
<rect x="260" y="{y-6}" width="760" height="10" rx="2" fill="#000" stroke="#143614"/>
<rect x="261" y="{y-5}" width="{758*pct/100:.0f}" height="8" rx="2" fill="{G}" filter="url(#glow)"/>
<text x="1090" y="{y+4}" font-size="15" fill="{INK}" text-anchor="end">{pct}%</text>
'''
    body = f'''<text class="ui" x="70" y="64" xml:space="preserve"><tspan fill="{SAGE}">magomin~/dev $</tspan> cat stack.txt | sort -r</text>
<text class="dim" x="70" y="86">self-assessed, honest</text>
{rows}'''
    return frame(H, "stack.txt: self-assessed proficiency bars", body)


PROJECTS = [
    ("re-track/", "Learn Ableton Live by rebuilding real songs. AI reverse-engineers a track into a lesson verified against your live set.  -> github.com/Magomin/re-track", ["python", "ableton", "early development"], "open source"),
]


def projects():
    row_h = 78
    H = 100 + len(PROJECTS) * row_h + 20
    rows = ""
    for i, (name, desc, tags, flag) in enumerate(PROJECTS):
        y = 100 + i * row_h
        rows += f'<rect x="56" y="{y}" width="{W-112}" height="{row_h-10}" rx="4" fill="#070b07" stroke="#143614"/>\n'
        rows += f'<text x="72" y="{y+24}" font-size="15" fill="{G}" filter="url(#glow)">{html.escape(name)}</text>\n'
        rows += f'<text x="{W-72}" y="{y+24}" font-size="13" fill="{GF}" text-anchor="end">-rwxr-xr-x</text>\n'
        rows += f'<text x="72" y="{y+44}" font-size="13" fill="{SAGE}">{html.escape(desc)}</text>\n'
        x = 72
        for t, col in [(t, GD) for t in tags] + [(flag, AMB)]:
            w = 16 + len(t) * 8
            rows += f'<rect x="{x}" y="{y+52}" width="{w}" height="14" rx="3" fill="none" stroke="{col}" stroke-opacity=".7"/>'
            rows += f'<text x="{x+8}" y="{y+63}" font-size="11" fill="{col}">{html.escape(t)}</text>\n'
            x += w + 8
    body = f'''<text class="ui" x="70" y="64" xml:space="preserve"><tspan fill="{SAGE}">magomin~/dev $</tspan> ls -la ~/projects</text>
<text class="dim" x="70" y="86">&gt; the open-source one I am building properly // drwxr-xr-x</text>
{rows}'''
    return frame(H, "ls -la ~/projects: selected work", body)


def prompt_panel(title, cmd, lines, cursor=False):
    """Panel with a prompt line and dim text lines; lines may carry (text, color) tuples."""
    H = 110 + len(lines) * 22 + (20 if cursor else 0)
    body = f'''<text class="ui" x="70" y="64" xml:space="preserve"><tspan fill="{SAGE}">magomin~/dev $</tspan> {html.escape(cmd)}</text>
'''
    y = 96
    for ln in lines:
        text, color = ln if isinstance(ln, tuple) else (ln, SAGE)
        body += f'<text x="70" y="{y}" font-size="15" fill="{color}" xml:space="preserve">{html.escape(text)}</text>\n'
        y += 22
    if cursor:
        body += f'<rect class="cur" x="70" y="{y-8}" width="9" height="16"/>'
    return frame(H, title, body)


def whoami():
    return prompt_panel("whoami: Matthieu Dominguez, agentic programmer", "whoami --full", [
        ("Matthieu Dominguez. Agentic programmer: I build software by directing AI agents,", INK),
        ("with tests and CI as the judge. At Cad&Lan I bring that way of working to a", INK),
        ("building-automation engineering team and ship the internal tools it needs.", INK),
        ("Before that, two years in growth and product at an AI recruiting startup.", INK),
        "",
        ("[x] Cad&Lan, Spain    [x] shipping since 2024    [x] every PR runs its tests", G),
    ])


def contact():
    return prompt_panel("contact: links below", "./contact", [
        ("-> linkedin   linkedin.com/in/matt-domi", G),
        ("-> web        matdomi.vercel.app", G),
        ("-> github     github.com/Magomin", G),
    ])


def footer():
    return prompt_panel("footer", 'echo "(c) 2026 Matthieu Dominguez, built with agents, shipped through CI"', [
        ("(c) 2026 Matthieu Dominguez, built with agents, shipped through CI", SAGE),
    ], cursor=True)


def pill(label):
    """Clickable link pill: wrapped in <a> by the README, since SVG inside <img> cannot link."""
    w = 40 + len(label) * 9
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="32" viewBox="0 0 {w} 32" role="img" aria-label="{html.escape(label)}">
<rect x="1" y="1" width="{w-2}" height="30" rx="4" fill="#050805" stroke="#1f4d1f"/>
<text x="14" y="21" font-family="{MONO}" font-size="14" fill="{G}" xml:space="preserve">-&gt; {html.escape(label)}</text>
</svg>'''


PILLS = ["linkedin", "web", "re-track"]


if __name__ == "__main__":
    import xml.dom.minidom
    for name, fn in (("header", header), ("whoami", whoami), ("neofetch", neofetch), ("stack", stack), ("projects", projects), ("contact", contact), ("footer", footer)):
        svg = fn()
        xml.dom.minidom.parseString(svg.encode())
        pathlib.Path("assets", f"{name}.svg").write_text(svg, encoding="utf-8")
        print("wrote", name)
    for label in PILLS:
        pathlib.Path("assets", f"pill-{label.replace(' ', '-')}.svg").write_text(pill(label), encoding="utf-8")
