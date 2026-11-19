import html, pathlib, lessons
E = html.escape
OUT = pathlib.Path(__file__).parent.parent / "greenai" / "lessons"; OUT.mkdir(exist_ok=True)
CATN = {"basic":"AI 기초","prompt":"프롬프트","content":"콘텐츠 제작","ux":"UX/UI","pm":"기획·PM","build":"자동화·제작"}
SITE = "https://greenai-205.pages.dev"
def page(L, i, all_):
    steps = "".join(f'''<li><b>{E(t)}</b><br>{E(b)}{f'<div class="prompt light" style="margin-top:8px"><div class="ptitle">예시</div><button class="copy" type="button">복사</button><pre>{E(ex)}</pre></div>' if ex else ''}</li>''' for t,b,ex in L["steps"])
    concepts = "".join(f'<div class="mini"><span class="k">{E(k)}</span><p style="color:var(--ink2);font-size:14px">{E(v)}</p></div>' for k,v in L["concepts"])
    mistakes = "".join(f'<li><b>✕ {E(m)}</b><br><span style="color:var(--green-deep)">→ {E(f)}</span></li>' for m,f in L["mistakes"])
    checks = "".join(f'<li><label><input type="checkbox"><div class="t"><b>{E(c)}</b></div></label></li>' for c in L["check"])
    nxt = "".join(f'<a href="{E(u)}">{E(t)} →</a>' for t,u in L["next"])
    prev_ = all_[i-1] if i > 0 else None; next_ = all_[i+1] if i+1 < len(all_) else None
    nav = '<div class="grid2" style="margin-top:12px">' + (f'<a class="btn btn-white" href="/lessons/{prev_["slug"]}">← 이전 레슨</a>' if prev_ else '<span></span>') + (f'<a class="btn btn-black" href="/lessons/{next_["slug"]}">다음 레슨 →</a>' if next_ else '<a class="btn btn-black" href="/learn">레슨 목록 →</a>') + '</div>'
    return f'''<!DOCTYPE html>
<html lang="ko"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><meta name="theme-color" content="#000000">
<title>{E(L["t"])} — LEARNING LAB · 그린 AI Lab</title><meta name="description" content="{E(L["sum"])}">
<meta property="og:type" content="article"><meta property="og:title" content="{E(L["t"])} — 그린 AI Lab"><meta property="og:description" content="{E(L["sum"])}"><meta property="og:image" content="{SITE}/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css"><link rel="stylesheet" href="/assets/guide.css"><script src="/assets/lab.js"></script>
<style>.steps-ol li{{margin-top:12px}}.steps-ol li b{{font-size:15.5px;color:var(--ink)}}.dt-rel{{display:grid;gap:6px;margin-top:10px}}.dt-rel a{{font-size:14.5px;font-weight:700;color:var(--ink);text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 14px}}.why{{font-size:15.5px;line-height:1.75;color:var(--ink2)}}@media(min-width:768px){{.why{{font-size:17px}}}}</style>
</head><body><div class="page">
<header class="nav"><a class="brand" href="/"><i>G</i>그린 AI Lab<b>.</b></a><a class="back" href="/learn">← 레슨 목록</a></header>
<nav class="labnav" id="labnav"></nav>
<section class="hero"><p class="eyebrow">LEARNING LAB · {E(L["lv"])} {i+1:02d}</p><h1>{E(L["t"])}</h1><p>{E(L["sum"])}</p>
<div class="badges"><span>{E(L["lv"])}</span><span>{E(CATN[L["cat"]])}</span><span>약 {L["min"]}분</span><span>실습 포함</span></div></section>
<section class="block"><p class="label">WHY</p><h2>이 레슨에서 <em>얻는 것</em></h2><p class="why" style="margin-top:10px">{E(L["why"])}</p></section>
<section class="block"><p class="label">CONCEPTS</p><h2>먼저 알아둘 <em>개념</em></h2><div class="grid2">{concepts}</div></section>
<section class="block"><p class="label">STEP BY STEP</p><h2>따라 하기 <em>{len(L["steps"])}단계</em></h2><div class="card"><ol class="steps-ol">{steps}</ol></div></section>
<section class="block"><p class="label">BEFORE · AFTER</p><h2>이렇게 <em>달라져요</em></h2>
<div class="note warn"><b>✕ 전</b><br>{E(L["bad"])}</div><div class="note"><b>○ 후</b><br>{E(L["good"])}</div><div class="note gray"><b>왜 좋아졌나요?</b> {E(L["why_good"])}</div></section>
<section class="block"><p class="label">COMMON MISTAKES</p><h2>자주 하는 <em>실수</em></h2><div class="card"><ul>{mistakes}</ul></div></section>
<section class="block"><p class="label">MISSION</p><h2>오늘의 <em>실습 미션</em></h2><div class="card"><p style="margin-top:0;font-size:15.5px;color:var(--ink)"><b>🎯 {E(L["mission"])}</b></p>
<div class="prompt" style="margin-top:12px"><div class="ptitle">미션용 프롬프트</div><button class="copy" type="button">복사</button><pre>{E(L["mprompt"])}</pre></div></div></section>
<section class="block"><p class="label">CHECKLIST</p><h2>다 했는지 <em>확인</em></h2><ul class="checks">{checks}</ul></section>
<section class="block"><p class="label">NEXT</p><h2>이어서 <em>보면 좋아요</em></h2><div class="dt-rel">{nxt}</div>{nav}</section>
<section class="cta"><small>GREEN AI LAB</small><h2>혼자 하기 막막하면<br><em>클래스에서 같이</em></h2><p>레슨 내용을 내 업무·프로젝트에 적용하는 1:1 클래스예요.</p><a href="/class" class="btn btn-green">클래스 보기 →</a></section>
<p class="updated">업데이트 2026.11.19 · 그린 AI Lab 자체 제작 · 툴 화면과 기능은 업데이트로 달라질 수 있어요</p>
<footer><div class="f-brand">그린 AI Lab<b>.</b></div>© 2026 Green AI Lab · <a href="/class">1:1 클래스</a> · <a href="mailto:greenai.lab3@gmail.com">문의하기</a></footer>
</div>
<script>document.addEventListener('change',function(e){{var c=e.target.closest('.checks input');if(c)c.closest('li').classList.toggle('done',c.checked)}});</script>
</body></html>'''
for i, L in enumerate(lessons.L):
    (OUT / f'{L["slug"]}.html').write_text(page(L, i, lessons.L), encoding="utf-8")
print("lessons", len(lessons.L))
