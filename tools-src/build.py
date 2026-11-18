"""자료 상세 페이지 생성기 — pages/*.py 의 META, BODY 로 site/guides/<slug>.html 을 만든다."""
import importlib.util, pathlib, html

ROOT = pathlib.Path(__file__).parent
OUT = ROOT.parent / "greenai" / "guides"
SITE = "https://greenai-205.pages.dev"

TPL = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#000000">
  <meta name="robots" content="noindex, nofollow">
  <title>{title} — 그린 AI Lab</title>
  <meta name="description" content="{desc}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{title} — 그린 AI Lab">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{site}/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <script src="/assets/guide.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
  <link rel="stylesheet" href="/assets/guide.css">
{extra_head}</head>
<body>
<div class="page">

  <header class="nav">
    <a class="brand" href="/archive"><i>G</i>그린 AI Lab<b>.</b></a>
    <a class="back" href="/archive">← 자료실</a>
  </header>

  <section class="hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p>{intro}</p>
{buttons}
    <div class="badges">{badges}</div>
  </section>
{toc}
{body}

  <section class="cta">
    <small>NEXT STEP</small>
    <h2>{cta_h2}</h2>
    <p>{cta_p}</p>
    <a href="/class" data-class class="btn btn-green">클래스 자세히 보기 →</a>
  </section>

  <div class="next"><a href="/archive" class="btn btn-black">← 다른 자료 보러가기</a></div>
  <p class="updated">최종 업데이트 {updated} · 출처: {source}<br>개인·업무용 자유 이용 · 재배포·판매 금지 · 인용 시 출처(그린 AI Lab) 표기 · 툴 화면과 기능은 업데이트로 달라질 수 있어요</p>

  <footer>
    <div class="f-brand">그린 AI Lab<b>.</b></div>
    © 2026 Green AI Lab · <a href="mailto:greenai.lab3@gmail.com">문의하기</a>
  </footer>
</div>
{extra_body}</body>
</html>
"""

def esc(s): return html.escape(s, quote=True)

def build(mod):
    m = mod.META
    btns = m.get("buttons", [])
    if btns:
        cls = "btns one" if len(btns) == 1 else "btns"
        b = "".join(f'<a href="{h}" class="btn {"btn-green" if i == 0 else "btn-line"}">{t}</a>' for i, (t, h) in enumerate(btns))
        buttons = f'    <div class="{cls}">{b}</div>'
    else:
        buttons = ""
    toc = ""
    if m.get("toc"):
        toc = '\n  <nav class="toc">' + "".join(f'<a href="#{a}">{t}</a>' for t, a in m["toc"]) + "</nav>"
    page = TPL.format(
        title=esc(m["title"]), desc=esc(m["desc"]), site=SITE,
        eyebrow=m["eyebrow"], h1=m["h1"], intro=m["intro"], buttons=buttons,
        badges="".join(f"<span>{x}</span>" for x in m["badges"]), toc=toc,
        body=mod.BODY, cta_h2=m["cta_h2"], cta_p=m["cta_p"], updated=m.get("updated", "2026.11.18"), source=m.get("source", "그린 AI Lab 자체 제작"),
        extra_head=getattr(mod, "HEAD", ""), extra_body=getattr(mod, "SCRIPT", ""),
    )
    (OUT / f'{m["slug"]}.html').write_text(page, encoding="utf-8")
    return m["slug"]

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for p in sorted((ROOT / "pages").glob("*.py")):
        spec = importlib.util.spec_from_file_location(p.stem, p)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        print("built", build(mod))
