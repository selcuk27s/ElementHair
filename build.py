"""Erzeugt aus index.html (Vorschau) die Live-Version in website/ – mit vollständigem <head>,
lokal gehosteten Schriften, robots.txt und sitemap.xml. Aufruf: python3 build.py"""
import re, datetime, pathlib
ROOT = pathlib.Path(__file__).parent
src = (ROOT / "index.html").read_text(encoding="utf-8")
head, body = src.split("</style>", 1)
head += "</style>"
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
head = re.sub(r'<!-- Hinweis für die Live-Website.*?-->\n', "", head)
head = re.sub(r'<link rel="preconnect"[^>]*>\n', "", head)
fonts = ""
for fam, file, w, st in [("Inter","inter-latin-300-normal",300,"normal"),("Inter","inter-latin-400-normal",400,"normal"),("Inter","inter-latin-500-normal",500,"normal"),
                         ("Playfair Display","playfair-display-latin-400-normal",400,"normal"),("Playfair Display","playfair-display-latin-500-normal",500,"normal"),
                         ("Playfair Display","playfair-display-latin-400-italic",400,"italic"),("Playfair Display","playfair-display-latin-500-italic",500,"italic")]:
    fonts += f'@font-face{{font-family:"{fam}";font-style:{st};font-weight:{w};font-display:swap;src:url(fonts/{file}.woff2) format("woff2")}}\n'
head = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>\n',
              '<link rel="preload" href="fonts/playfair-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
              '<link rel="preload" href="fonts/inter-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>\n<style>\n' + fonts +
              'body{margin:0}img{max-width:100%}[hidden]{display:none!important}\n</style>\n', head)
out = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + "\n</head>\n<body>" + body + "\n</body>\n</html>\n")
web = ROOT / "website"; web.mkdir(exist_ok=True)
(web / "index.html").write_text(out, encoding="utf-8")
(web / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://elementhair-sonthofen.de/sitemap.xml\n", encoding="utf-8")
today = datetime.date.today().isoformat()
(web / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://elementhair-sonthofen.de/</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>
</urlset>
''', encoding="utf-8")
import shutil
shutil.copytree(ROOT / "bilder", web / "bilder", dirs_exist_ok=True)
shutil.copy(ROOT / "og-image.jpg", web / "og-image.jpg")
shutil.copy(ROOT / "llms.txt", web / "llms.txt")
print("website/ erstellt:", len(out) // 1024, "KB")
