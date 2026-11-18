"""7개 영역 페이지 생성기 — 데이터만 바꾸고 python3 lab_build.py"""
import json, html, importlib.util, pathlib
ROOT = pathlib.Path(__file__).parent; OUT = ROOT.parent / "greenai"
SITE = "https://greenai-205.pages.dev"
E = html.escape
import lab_more as M

SHELL = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="theme-color" content="#000000">
  <title>{title} — 그린 AI Lab</title>
  <meta name="description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} — 그린 AI Lab">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{site}/og.png">
  <meta property="og:url" content="{site}/{slug}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
  <link rel="stylesheet" href="/assets/guide.css">
  <script src="/assets/lab.js"></script>
</head>
<body>
<div class="page">
  <header class="nav"><a class="brand" href="/"><i>G</i>그린 AI Lab<b>.</b></a><a class="back" href="/class">1:1 클래스 →</a></header>
  <nav class="labnav" id="labnav"></nav>
  <section class="hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p>{intro}</p>
  </section>
{body}
  <section class="cta">
    <small>GREEN AI LAB</small>
    <h2>자료로 익혔다면<br><em>내 결과물로</em> 만들어 봐요</h2>
    <p>구독하면 템플릿·체크리스트·워크북이 있는 자료실이 바로 열려요.</p>
    <a href="/" class="btn btn-green">무료 자료실 받기 →</a>
  </section>
  <footer><div class="f-brand">그린 AI Lab<b>.</b></div>© 2026 Green AI Lab · <a href="/class">1:1 클래스</a> · <a href="mailto:greenai.lab3@gmail.com">문의하기</a></footer>
</div>
<div class="sheet" id="labsheet" role="dialog" aria-modal="true"><div class="sheet-bg" data-close></div><div class="sheet-body"><button class="sheet-close" type="button" data-close aria-label="닫기">×</button><div id="labsheetin"></div></div></div>
{script}
</body>
</html>
"""

def list_body(facets, placeholder):
    rows = "".join(f'<div class="chips" id="facet-{f["key"]}"></div>' for f in facets)
    return f'''  <div class="lab-tools">
    <label class="search"><span>🔎</span><input type="search" id="labq" placeholder="{placeholder}"></label>
    {rows}
    <p class="count-msg"><span id="labcount"></span> 보는 중</p>
  </div>
  <div class="lgrid" id="lablist"></div>
  <p class="empty-msg" id="labempty" style="padding:0 20px">찾는 내용이 없어요. 다른 단어로 검색해 보세요.</p>'''

def page(slug, title, desc, eyebrow, h1, intro, lab=None, placeholder="검색", body=None, script=""):
    if lab is not None:
        body = list_body(lab.get("facets", []), placeholder)
        script = "<script>window.LAB = " + json.dumps(lab, ensure_ascii=False) + ";</script>" + script
    (OUT / f"{slug}.html").write_text(SHELL.format(slug=slug, title=E(title), desc=E(desc), site=SITE, eyebrow=eyebrow, h1=h1, intro=intro, body=body, script=script), encoding="utf-8")
    print("built", slug)

# ───────────────────────── 1. AI DIRECTORY ─────────────────────────
CAT = {"chat":"대화·글쓰기","research":"리서치·요약","image":"이미지","video":"영상","audio":"음성·음악","design":"디자인·문서","auto":"업무 자동화","build":"개발·시제품"}
PRICE = {"free":"무료로 시작","freemium":"무료 + 유료 플랜","paid":"유료 위주","oss":"오픈소스·셀프호스팅 무료"}
T = [
 ("ChatGPT","chat","freemium","https://chatgpt.com","OpenAI의 범용 AI 비서","글쓰기, 아이디어, 이미지 생성, 파일 분석, 음성 대화를 한곳에서 하는 가장 대중적인 AI 비서예요.",["기획 초안·이메일·보고서 작성","이미지 생성과 수정","엑셀·PDF 파일 분석"],"chatgpt 챗GPT 챗지피티 openai"),
 ("Claude","chat","freemium","https://claude.ai","Anthropic의 AI 비서, 긴 문서와 글에 강함","긴 문서를 읽고 정리하거나 글을 다듬는 데 강하고, 코드 작성·문서 파일 생성까지 해요. 스킬로 작업 방식을 늘릴 수 있어요.",["기획서·보고서 정리","글 톤 다듬기","문서·슬라이드·코드 만들기"],"클로드 anthropic"),
 ("Gemini","chat","freemium","https://gemini.google.com","구글 서비스와 이어지는 AI 비서","지메일·드라이브·문서 등 구글 서비스와 연결해서 쓰기 좋아요. 이미지·영상 생성 기능도 들어 있어요.",["구글 문서·메일 요약","검색 기반 리서치","구글 워크스페이스 업무"],"제미나이 google"),
 ("Microsoft Copilot","chat","freemium","https://copilot.microsoft.com","MS 오피스와 이어지는 AI 비서","워드·엑셀·파워포인트 등 마이크로소프트 업무 환경과 함께 쓰기 좋아요.",["오피스 문서 초안","엑셀 데이터 정리"],"코파일럿 마이크로소프트"),
 ("뤼튼 (Wrtn)","chat","free","https://wrtn.ai","국내 AI 서비스, 한국어 사용 환경","한국어 환경에 맞춘 국내 AI 서비스예요. 여러 AI 모델과 다양한 도구를 쉽게 써볼 수 있어요.",["한국어 글쓰기","가볍게 AI 체험"],"뤼튼 wrtn"),
 ("Perplexity","research","freemium","https://www.perplexity.ai","출처 링크를 달아 주는 검색형 AI","질문하면 웹을 찾아 출처와 함께 답해요. 최신 정보 확인과 시장 조사에 좋아요.",["시장·경쟁사 조사","최신 뉴스 확인","출처 있는 자료 모으기"],"퍼플렉시티"),
 ("NotebookLM","research","freemium","https://notebooklm.google.com","내 자료만 근거로 답하는 구글 노트","올린 PDF·문서·링크·영상만 근거로 요약하고 답해요. 강의 준비, 자료 공부에 좋아요.",["강의·스터디 자료 정리","긴 보고서 요약","오디오 요약 듣기"],"노트북LM 노트북엘엠"),
 ("클로바노트","research","freemium","https://clovanote.naver.com","네이버의 음성 기록·요약","회의·강의를 녹음하면 한국어로 받아 적고 요약해 줘요.",["회의록 자동 작성","강의 녹음 정리"],"clova note 네이버"),
 ("Midjourney","image","paid","https://www.midjourney.com","감성적이고 완성도 높은 이미지 생성","브랜드 무드, 콘셉트 아트, 광고 비주얼처럼 분위기가 중요한 이미지에 강해요.",["브랜드 무드보드","광고 비주얼 시안","콘셉트 아트"],"미드저니"),
 ("Ideogram","image","freemium","https://ideogram.ai","글자가 들어간 이미지에 강함","포스터·썸네일처럼 이미지 안에 문구를 넣는 작업에 비교적 강해요.",["썸네일 시안","포스터·배너 시안"],"아이디오그램"),
 ("Adobe Firefly","image","freemium","https://firefly.adobe.com","어도비의 이미지 생성·편집","포토샵·일러스트레이터 등 어도비 도구와 함께 쓰기 좋아요. 상업적 사용을 고려해 만든 모델이에요.",["이미지 확장·부분 수정","어도비 작업 연계"],"파이어플라이 어도비"),
 ("Kling AI","video","freemium","https://klingai.com","이미지·텍스트로 영상 생성","이미지를 넣으면 움직이는 영상으로 만들어요. 2026년 3.0 모델에서 최대 15초, 소리 생성까지 지원해요.",["제품 광고 영상","숏폼 영상 소스","이미지 → 영상"],"클링"),
 ("Runway","video","freemium","https://runwayml.com","영상 생성과 편집을 함께","영상 생성뿐 아니라 배경 지우기 등 편집 기능도 함께 있어요.",["영상 생성","영상 편집·합성"],"런웨이"),
 ("Google Flow (Veo)","video","freemium","https://labs.google/flow","구글의 영상 생성 도구","구글의 영상 생성 모델 Veo로 장면을 만들고 이어 붙여요.",["짧은 영상 장면 생성"],"플로우 비오 veo 구글"),
 ("CapCut","video","freemium","https://www.capcut.com","자동 자막·템플릿 영상 편집","숏폼 편집에 가장 쉬운 앱이에요. 자동 자막, 템플릿, 음악까지 한 번에.",["릴스·쇼츠 편집","자동 자막"],"캡컷"),
 ("Vrew","video","freemium","https://vrew.ai","말소리로 한국어 자막 자동 생성","영상의 말소리를 받아 적어 자막을 만들고, 글 편집처럼 영상을 잘라요.",["강의·인터뷰 자막","말 실수 컷 편집"],"브루"),
 ("ElevenLabs","audio","freemium","https://elevenlabs.io","자연스러운 AI 음성·더빙","텍스트를 사람 같은 목소리로 읽어 주고, 여러 언어로 더빙해요.",["영상 내레이션","다국어 더빙"],"일레븐랩스"),
 ("Typecast","audio","freemium","https://typecast.ai","한국어 AI 성우","다양한 한국어 AI 성우 목소리로 내레이션을 만들어요.",["한국어 내레이션","교육 영상 음성"],"타입캐스트"),
 ("Suno","audio","freemium","https://suno.com","가사·분위기로 노래 생성","가사나 분위기를 적으면 노래와 배경음악을 만들어요.",["배경음악","브랜드 징글"],"수노"),
 ("Figma","design","freemium","https://www.figma.com","UI 디자인·프로토타입의 기본","화면 디자인과 프로토타입의 표준 도구예요. AI 기능으로 시안 생성, 레이어 정리 등을 도와요.",["앱·웹 화면 설계","프로토타입","디자인 시스템"],"피그마"),
 ("Canva","design","freemium","https://www.canva.com","템플릿 디자인 + AI","카드뉴스, 썸네일, 상세페이지, 발표자료를 템플릿으로 빠르게 만들어요.",["카드뉴스·썸네일","SNS 콘텐츠"],"캔바"),
 ("Gamma","design","freemium","https://gamma.app","글을 넣으면 슬라이드 초안","개요나 글을 넣으면 발표 슬라이드·문서 초안을 디자인까지 만들어 줘요.",["발표자료 초안","제안서"],"감마"),
 ("Notion AI","design","freemium","https://www.notion.com/product/ai","노션 안의 AI","노션 페이지 안에서 요약, 글쓰기, 회의록 정리, 데이터베이스 채우기를 해요.",["회의록 정리","문서 요약","업무 위키"],"노션"),
 ("Miro","design","freemium","https://miro.com","협업 화이트보드 + AI","브레인스토밍, 유저 플로우, 회고를 함께 그리는 화이트보드예요.",["브레인스토밍","유저 플로우","워크숍"],"미로"),
 ("Make","auto","freemium","https://www.make.com","시각적인 업무 자동화","앱과 앱을 블록처럼 이어 반복 업무를 자동화해요. 비개발자도 쓰기 쉬워요.",["폼 응답 → 시트·메일","SNS 게시 자동화"],"메이크 integromat"),
 ("n8n","auto","oss","https://n8n.io","오픈소스 자동화 + AI 에이전트","노드를 이어 자동화를 만들어요. 직접 설치하면 무료로 쓸 수 있고, AI 노드가 풍부해요.",["AI 요약 자동화","사내 업무 자동화"],"엔에잇엔 n8n"),
 ("Zapier","auto","freemium","https://zapier.com","가장 많은 앱을 잇는 자동화","수천 개 앱을 연결하는 자동화 서비스예요. 설정이 가장 간단한 편이에요.",["앱 간 데이터 옮기기","알림 자동화"],"재피어"),
 ("Lovable","build","freemium","https://lovable.dev","말로 설명하면 웹앱을 만들어 줌","원하는 서비스를 설명하면 실제로 동작하는 웹앱을 만들어요.",["아이디어 시제품","랜딩페이지"],"러버블"),
 ("v0","build","freemium","https://v0.app","Vercel의 화면·앱 생성 AI","말이나 이미지로 웹 화면을 코드로 만들어요.",["웹 화면 시안","프론트엔드 코드"],"브이제로 vercel"),
 ("Cursor","build","freemium","https://cursor.com","AI 코드 편집기","AI와 함께 코드를 쓰고 고치는 편집기예요.",["코드 작성·수정"],"커서"),
 ("Claude Code","build","paid","https://claude.com/product/claude-code","터미널·IDE에서 쓰는 Claude 코딩 에이전트","코드베이스를 읽고 수정·실행까지 하는 코딩 에이전트예요. 스킬과 플러그인으로 확장해요.",["웹사이트 제작","자동화 스크립트","코드 리뷰"],"클로드코드"),
]
T += M.T
dir_items = [dict(t=n, d=d, cat=c, price_k=p, price=PRICE[p], url=u, urlLabel="공식 사이트", what=w, use=us, alias=al,
                  rel=[["목적별 AI 툴 가이드","/guides/ai-tools"]]) for n,c,p,u,d,w,us,al in T]
for it in dir_items: it["pk"] = it.pop("price_k")
page("directory", "AI DIRECTORY", "분야별·목적별로 고르는 생성형 AI 도구 디렉터리. 가격 형태, 주요 기능, 활용 사례, 공식 링크.",
     "01 · AI DIRECTORY", "하고 싶은 일로 찾는<br><em>AI 도구 디렉터리</em>", f"AI 도구 {len(T)}개를 분야·가격 형태로 나눴어요.<br>카드를 누르면 주요 기능, 활용 사례, 공식 링크가 나와요.",
     lab=dict(items=dir_items, facets=[dict(key="cat",label="분야",values=CAT),dict(key="pk",label="가격",values=PRICE)], useLabel="이럴 때 써요", whatLabel="주요 기능",
              note="가격 형태는 2026년 11월 기준이에요. 요금과 기능은 자주 바뀌니 공식 사이트에서 확인해 주세요."),
     placeholder="도구 이름이나 하고 싶은 일 (예: 자막, 썸네일, 회의록)")

# ───────────────────────── 2. SKILLS LIBRARY ─────────────────────────
SCAT = {"doc":"문서 만들기","design":"디자인·비주얼","work":"업무·글쓰기","dev":"개발·제작","meta":"스킬 만들기"}
SRC = "github.com/anthropics/skills (Anthropic 공식 스킬 저장소)"
APACHE = "Apache 2.0 — 상업적 사용·수정·재배포 가능 (라이선스 고지 필요)"
SA = "Source-available — 참고용으로 공개, 재배포·수정 배포 불가 (Anthropic 이용약관 적용)"
INSTALL = ("# Claude Code\n/plugin marketplace add anthropics/skills\n/plugin install example-skills@anthropic-agent-skills\n\n"
           "# Claude.ai (웹·앱)\n설정 > 기능(Capabilities) > Skills 에서 켜기\n직접 만든 스킬은 폴더를 zip으로 묶어 업로드")
INSTALL_DOC = INSTALL.replace("example-skills", "document-skills")
S = [
 ("docx","doc",SA,"워드(.docx) 문서 만들기·편집","목차·표·머리말이 있는 워드 문서를 만들고, 기존 문서를 고치거나 변경 내용 추적까지 해요.",["보고서·제안서를 워드 파일로","기존 워드 문서 수정"]),
 ("pptx","doc",SA,"파워포인트 만들기·편집","슬라이드 덱을 만들고 기존 파워포인트를 읽거나 고쳐요.",["발표자료 초안을 .pptx로","템플릿에 맞춰 슬라이드 채우기"]),
 ("xlsx","doc",SA,"엑셀 만들기·분석","수식이 살아 있는 엑셀 파일을 만들고, 표 데이터를 정리·분석해요.",["예산·추적표 만들기","엑셀 데이터 정리"]),
 ("pdf","doc",SA,"PDF 읽기·합치기·만들기","PDF에서 글·표 뽑기, 합치기·나누기, 양식 채우기, 새 PDF 만들기를 해요.",["계약서·자료 PDF 정리","PDF 양식 채우기"]),
 ("doc-coauthoring","work","폴더의 LICENSE 파일 확인","문서 함께 쓰기","제안서·기획 문서 같은 긴 문서를 단계별로 함께 쓰도록 진행해요.",["기획서·제안서 공동 작성"]),
 ("internal-comms","work",APACHE,"사내 공지·업데이트 글","주간 업데이트, 공지, 뉴스레터 같은 사내 커뮤니케이션 글을 형식에 맞춰 써요.",["주간 보고","팀 공지·뉴스레터"]),
 ("brand-guidelines","design",APACHE,"브랜드 가이드 적용","정해진 브랜드 색·글꼴·톤을 결과물에 적용하는 방법을 담은 예시 스킬이에요.",["결과물에 브랜드 톤 맞추기"]),
 ("theme-factory","design",APACHE,"테마 입히기","슬라이드·문서·페이지 등에 미리 정의된 색·글꼴 테마를 입혀요.",["발표자료 테마 통일"]),
 ("canvas-design","design",APACHE,"포스터·비주얼 디자인","포스터, 아트워크 같은 정적인 비주얼을 PNG·PDF로 디자인해요.",["포스터·카드 비주얼"]),
 ("algorithmic-art","design",APACHE,"코드로 그리는 제너러티브 아트","p5.js 등으로 규칙 기반 아트를 만들어요.",["패턴·배경 그래픽"]),
 ("slack-gif-creator","design",APACHE,"슬랙용 GIF 만들기","슬랙 이모지·메시지에 맞는 짧은 애니메이션 GIF를 만들어요.",["팀 이모지·축하 GIF"]),
 ("frontend-design","dev",APACHE,"완성도 높은 웹 화면 디자인","템플릿 같지 않은, 의도가 분명한 웹 UI를 만들도록 도와요.",["랜딩페이지","웹 화면 리디자인"]),
 ("web-artifacts-builder","dev",APACHE,"복잡한 웹 결과물 만들기","여러 컴포넌트로 된 인터랙티브 웹 결과물을 만들어요.",["대시보드·미니 웹앱"]),
 ("webapp-testing","dev",APACHE,"웹앱 테스트","브라우저 자동화로 웹앱을 열어 동작을 확인하고 스크린샷을 찍어요.",["배포 전 화면 점검"]),
 ("mcp-builder","dev",APACHE,"MCP 서버 만들기","Claude가 외부 서비스와 연결되도록 MCP 서버를 설계·구현하는 방법을 담았어요.",["사내 도구를 Claude에 연결"]),
 ("skill-creator","meta",APACHE,"나만의 스킬 만들기","새 스킬을 만들고, 테스트하고, 설명을 다듬는 과정을 도와요.",["반복 업무를 스킬로 만들기","스킬 품질 테스트"]),
]
sk_items = []
for name, c, lic, d, w, us in S:
    sk_items.append(dict(t=name, d=d, cat=c, what=w, use=us, lic=lic, src=SRC,
        how=["설치 명령으로 스킬 묶음 설치 (아래 코드)","Claude에게 평소처럼 요청 — 관련 요청이면 스킬이 자동으로 쓰여요","결과를 보고 이어서 수정 요청"],
        code=INSTALL_DOC if c == "doc" else INSTALL, url=f"https://github.com/anthropics/skills/tree/main/skills/{name}", urlLabel="원본 보기 (GitHub)",
        rel=[["Claude Skills 시작하기 (LEARNING LAB)","/learn#스킬"]]))
for name, c, d, w, md in M.CS:
    sk_items.append(dict(t=name, d=d+" (커스텀 템플릿)", cat=c, kind="custom", what=w, use=[d], lic=M.CS_LIC, src="그린 AI Lab 제작", how=M.CS_HOW, code=md, alias="커스텀 템플릿 skill.md"))
for it in sk_items: it.setdefault("kind","official")
page("skills", "SKILLS LIBRARY", "Claude Skills와 재사용 가능한 AI 스킬 모음. 스킬별 설명, 사용 목적, 설치 방법, 원본 출처와 라이선스.",
     "02 · SKILLS LIBRARY", "Claude에게 일 잘하는 법을<br><em>가르치는 스킬</em> 모음", "공식 스킬 16개와 바로 고쳐 쓰는 커스텀 스킬 템플릿 10개.<br>쓰임새, 설치 방법, SKILL.md, 라이선스를 정리했어요.",
     lab=dict(items=sk_items, facets=[dict(key="kind",label="종류",values={"official":"공식 스킬","custom":"커스텀 템플릿"}),dict(key="cat",label="분야",values=SCAT)], whatLabel="이 스킬은", useLabel="이럴 때 써요", howLabel="쓰는 법",
              note="설치 방법은 바뀔 수 있어요. 사용 전 저장소 README와 각 스킬 폴더의 LICENSE를 꼭 확인해 주세요."),
     placeholder="스킬 이름이나 작업 (예: 엑셀, 포스터, 테스트)")

# ───────────────────────── 3. PROMPT LIBRARY ─────────────────────────
spec = importlib.util.spec_from_file_location("p2", ROOT / "pages" / "p02_prompts.py"); p2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p2)
ROLE = {"plan":"pm","design":"designer","mkt":"marketer","write":"creator","work":"office"}
PR = []
for key, (label, lst) in p2.P.items():
    for title, body in lst:
        PR.append(dict(t=title, d=label + " · 대화형 AI", work=key, role=ROLE[key], tool="chat", prompt=body,
                       ex="ChatGPT·Claude·Gemini에 붙여넣고 [대괄호]를 내 상황으로 바꿔요. 첫 답을 본 뒤 \"더 짧게\", \"2번 안을 발전시켜 줘\"처럼 이어서 다듬어요."))
EXTRA = [
 ("미드저니 광고 이미지","mkt","marketer","image","[제품], centered on a [color] seamless background, soft studio lighting, subtle shadow, premium commercial product photography, minimal --ar 4:5","[제품]·[color]만 바꿔 제품 단독컷을 만들어요. --ar 은 9:16(릴스), 1:1(피드) 등으로 바꿔요."),
 ("이미지 스타일 통일","design","designer","image","같은 브랜드 시리즈 이미지야. 조명: [조명], 색감: [색 2가지], 배경: [배경], 분위기: [분위기]. 이 조건을 모든 이미지에 똑같이 유지해 줘. 이번 장면: [장면]","시리즈 이미지의 톤을 맞출 때 장면만 바꿔 반복해요."),
 ("Kling 제품 영상","mkt","marketer","video","[제품]이 천천히 회전한다. 카메라는 고정. 배경의 먼지 입자가 빛을 받아 떠다닌다. 세련되고 고급스러운 분위기, 슬로모션.","이미지→영상 방식으로 5초씩 만들어요. 움직임은 하나만."),
 ("Kling 카메라 무빙","mkt","creator","video","[피사체]를 향해 카메라가 천천히 다가간다(push in). [움직이는 요소]가 살짝 흔들린다. [분위기].","첫 컷 클로즈업에 좋아요. 움직이는 요소: 김, 물방울, 잎사귀, 천."),
 ("숏폼 자막 3세트","write","creator","video","[제품/주제] 15초 세로 영상의 화면 자막을 써 줘. 컷 1: [장면] / 컷 2: [장면] / 컷 3: [장면]. 컷마다 10자 안팎, 감성·정보·유머 3가지 톤으로.","편집 앱에서 자막으로 바로 써요."),
 ("Perplexity 시장 조사","plan","pm","research","[분야]의 2026년 주요 서비스 5개를 찾아 핵심 기능, 타깃, 가격 형태, 최근 소식을 표로 정리해 줘. 각 항목에 출처 링크를 달아 줘.","출처 링크를 열어 사실을 한 번 더 확인해요."),
 ("NotebookLM 강의 요약","write","creator","research","올린 자료만 근거로 [주제] 강의 목차를 만들어 줘. 파트마다 핵심 개념 3개, 자료 속 예시, 수강생이 헷갈릴 만한 점을 정리해 줘.","PDF·문서를 올린 노트북에서 써요."),
 ("Gamma 발표 초안","work","office","slide","[주제]로 10장 발표자료를 만들어 줘. 대상: [청중]. 1장 제목, 2장 문제, 3~7장 핵심 내용, 8장 사례, 9장 실행 계획, 10장 요약. 장마다 핵심 문장 1개와 근거 2개.","Gamma에 붙여넣어 초안을 만든 뒤 디자인을 다듬어요."),
 ("피그마 화면 설명","design","designer","chat","이 화면 캡처를 보고 개발자 전달용 설명을 써 줘. 요소별 동작, 상태(기본·눌림·비활성·오류), 간격·글자 크기 규칙을 표로.","캡처를 첨부할 수 있는 AI에서 써요."),
 ("Claude 프로젝트 지침","work","office","chat","너는 [회사/브랜드]의 [역할]이야. 말투는 [말투], 독자는 [독자]. 항상 결론을 먼저, 3줄 요약을 끝에. 모르는 건 모른다고 말하고 [확인 필요]로 표시해.","프로젝트·GPTs 지침에 넣어 매번 같은 기준으로 답하게 해요."),
 ("n8n 워크플로 설계","work","office","auto","[반복 업무]를 n8n으로 자동화하려고 해. 트리거, 필요한 노드 순서, 각 노드 설정 값, 실패할 때 처리 방법을 단계별로 알려 줘.","WORKFLOW LAB의 예시와 함께 써요."),
 ("코딩 없이 웹 시제품","plan","pm","build","[서비스]의 랜딩페이지를 만들어 줘. 섹션: 문제, 해결, 기능 3개, 후기 자리, 신청 폼. 모바일 우선, [브랜드 색] 사용.","Lovable·v0·Claude에 넣어 시제품을 만들어요."),
]
for t, w, r, tool, pr, ex in EXTRA:
    PR.append(dict(t=t, d=f"{p2.P[w][0]} · 도구 특화", work=w, role=r, tool=tool, prompt=pr, ex=ex))
for t, w, r, tool, pr, ex in M.PR:
    PR.append(dict(t=t, d=f"{p2.P[w][0]} · {'대화형 AI' if tool=='chat' else '도구 특화'}", work=w, role=r, tool=tool, prompt=pr, ex=ex))
WORK = {k: v[0] for k, v in p2.P.items()}
ROLES = {"pm":"기획자·PM","designer":"디자이너","marketer":"마케터","creator":"크리에이터","office":"직장인"}
TOOLS_ = {"chat":"대화형 AI","image":"이미지 AI","video":"영상 AI","audio":"음성·음악 AI","research":"리서치 AI","slide":"슬라이드 AI","auto":"자동화","build":"시제품 제작"}
page("prompts", "PROMPT LIBRARY", f"업무별·역할별·도구별 프롬프트 {len(PR)}개. 복사하고 활용 예시를 보며 바로 쓰기.",
     "03 · PROMPT LIBRARY", f"업무·역할·도구로 찾는<br><em>프롬프트 {len(PR)}</em>", "초록 [대괄호]만 내 상황으로 바꾸면 돼요.<br>카드를 누르면 복사 버튼과 활용 예시가 나와요.",
     lab=dict(items=PR, inlinePrompt=True, facets=[dict(key="work",label="업무",values=WORK),dict(key="role",label="역할",values=ROLES),dict(key="tool",label="도구",values=TOOLS_)], src="그린 AI Lab 자체 제작"),
     placeholder="예) 회의록, 릴스, 미드저니, 오류 문구")

# ───────────────────────── 4. WORKFLOW LAB ─────────────────────────
WCAT = {"content":"콘텐츠","sales":"고객·문의","ops":"업무 정리","report":"리포트"}
WF = [
 ("블로그 새 글 → SNS 게시물 초안","content","중급",["n8n","Make","RSS","ChatGPT/Claude API","Notion"],"블로그에 글을 올리면 AI가 인스타 캡션·스레드 글·뉴스레터 소개문 초안을 만들어 노션에 쌓아요.",
  ["RSS 트리거: 블로그 RSS 주소에서 새 글 감지","HTTP/RSS 노드: 글 제목·본문 가져오기","AI 노드: 캡션(300자)·스레드(5줄)·뉴스레터 소개 3종 생성","Notion 노드: '게시 대기' 데이터베이스에 저장","검토 후 직접 게시 (자동 게시는 계정 정책 확인 후)"],"글 1편당 30분 → 5분"),
 ("구독 신청 → 시트 기록 + 환영 알림","sales","초급",["Make","Google Forms/웹훅","Google Sheets","Gmail","Slack"],"신청이 들어오면 시트에 쌓고, 나에게 알림을 보내고, 신청자에게 안내 메일을 보내요.",
  ["트리거: 폼 제출 또는 웹훅으로 신청 정보 받기","Google Sheets: 이름·이메일·유입 경로 한 줄 추가","Slack/카카오 알림: '새 신청 1건'","Gmail: 신청자에게 안내 메일 발송","주간 합계는 시트 수식으로 자동 집계"],"신청 관리 수작업 0"),
 ("문의 메일 자동 분류 + 답장 초안","sales","중급",["n8n","Gmail","ChatGPT/Claude API","Google Sheets"],"새 문의 메일을 AI가 '클래스·협업·기타'로 분류하고, 답장 초안을 임시보관함에 만들어요.",
  ["Gmail 트리거: 특정 라벨/주소로 온 새 메일","AI 노드: 분류 + 핵심 요청 요약 + 답장 초안","Switch 노드: 분류별로 라벨 붙이기","Gmail: 답장 초안을 임시보관함에 저장 (자동 발송 X)","Sheets: 문의 기록 남기기"],"답장 작성 시간 절반"),
 ("유튜브 영상 → 블로그 글 초안","content","중급",["n8n","YouTube","자막/전사","ChatGPT/Claude API","Google Docs"],"새로 올린 영상의 자막을 바탕으로 블로그 글 초안과 SEO 제목 후보를 만들어요.",
  ["YouTube/RSS 트리거: 새 영상 감지","자막 가져오기 (자동 자막 또는 전사 도구)","AI 노드: 소제목 구조 블로그 글 + 제목 10개","Google Docs: 초안 문서 생성","직접 사례·이미지 추가 후 발행"],"영상 1개 → 글 1편"),
 ("회의 녹음 → 회의록 → 노션","ops","초급",["클로바노트/전사 도구","ChatGPT/Claude","Notion","Make"],"회의 녹음 전사본을 '결정 사항 / 할 일 / 미정'으로 정리해 노션 회의록 DB에 저장해요.",
  ["회의 녹음 → 전사본 만들기","전사본을 폴더에 저장하면 자동화 시작 (Make: Watch files)","AI: 결정·할 일(담당·기한)·미정 정리","Notion: 회의록 DB에 페이지 생성","할 일은 담당자에게 알림"],"회의록 작성 20분 → 2분"),
 ("주간 트렌드 뉴스 리포트","report","중급",["n8n","Schedule","RSS","ChatGPT/Claude API","Gmail"],"매주 월요일 아침, 관심 분야 뉴스를 모아 AI가 5줄 요약과 인사이트를 붙여 메일로 보내요.",
  ["Schedule 트리거: 매주 월 08:00","RSS 노드 여러 개: AI·디자인·기획 뉴스 사이트","Merge + 중복 제거, 최근 7일만 남기기","AI 노드: 주제별 묶기, 5줄 요약, 콘텐츠 아이디어 3개","Gmail: 나에게 리포트 발송"],"리서치 1시간 → 0"),
 ("클래스 신청 → 일정·사전 설문","sales","초급",["Make","Google Calendar","Google Forms","Gmail"],"클래스 결제·신청 정보를 받으면 상담 일정 링크와 사전 설문을 자동으로 보내요.",
  ["트리거: 신청 시트에 새 줄 추가","Gmail: 사전 설문 링크 + 일정 선택 링크 발송","응답이 오면 Calendar 일정 생성","수업 전날 리마인드 메일"],"신청 응대 자동화"),
 ("댓글 키워드 → 자료 링크 DM","content","초급",["인스타그램 DM 자동화 도구(ManyChat 등)","Make"],"게시물에 '프롬프트' 같은 키워드 댓글이 달리면 자료실 링크를 DM으로 보내요.",
  ["DM 자동화 도구에 인스타 계정 연결","게시물·키워드 규칙 만들기 (예: '프롬프트')","DM 문구: 자료 소개 + 자료실 링크(?from=insta)","플랫폼 자동화 정책을 확인하고 과도한 발송 피하기"],"댓글 응대 자동"),
]
WF += M.WF
wf_items = [dict(t=t, d=w, cat=c, level=lv, tools=tl, what=w, how=st, use=[f"기대 효과: {eff}"],
                 rel=[["프롬프트: n8n 워크플로 설계","/prompts#n8n"]]) for t,c,lv,tl,w,st,eff in WF]
page("workflows", "WORKFLOW LAB", "Make, n8n으로 만드는 업무 자동화 워크플로. 사례, 단계별 실행 방법, 연결 도구.",
     "04 · WORKFLOW LAB", "반복 업무를 맡기는<br><em>자동화 워크플로</em>", "Make·n8n으로 바로 따라 만들 수 있는 자동화 사례예요.<br>카드를 누르면 단계별 실행 방법과 연결 도구가 나와요.",
     lab=dict(items=wf_items, facets=[dict(key="cat",label="분야",values=WCAT)], whatLabel="무엇을 자동화하나요?", useLabel="효과", howLabel="단계별 실행", toolsLabel="연결 도구",
              note="개인정보가 오가는 자동화는 저장 위치와 권한을 꼭 확인하세요. 자동 발송보다 '초안 만들기 → 사람이 확인'을 권해요.", src="그린 AI Lab 자체 설계"),
     placeholder="예) 블로그, 회의록, 메일, n8n")

# ───────────────────────── 6. LEARNING LAB ─────────────────────────
LCAT = {"basic":"AI 기초","prompt":"프롬프트","content":"콘텐츠 제작","ux":"UX/UI","pm":"기획·PM","build":"자동화·제작"}
LV = ["초급","중급","고급"]
LS = [
 ("생성형 AI, 처음 시작하기","basic","초급","AI 비서 하나를 골라 오늘 업무 하나를 맡겨 보는 첫 실습",["ChatGPT·Claude·Gemini 중 하나 가입","오늘 할 일 중 '글로 된 것' 하나 고르기 (메일, 요약, 아이디어)","자료실 프롬프트 하나 복사해 써 보기","답을 보고 '더 짧게', '표로'처럼 한 번 더 요청"],[["AI 도구 디렉터리","/directory"]]),
 ("AI 답을 믿어도 될까: 확인 습관","basic","초급","그럴듯한 오답을 걸러내는 3가지 확인법",["숫자·인물·법 정보는 원문으로 확인","출처를 달라고 요청하고 링크 열어보기","민감한 정보는 넣기 전에 지우기"],[["목적별 AI 툴 가이드","/guides/ai-tools"]]),
 ("좋은 프롬프트의 4요소","prompt","초급","역할·맥락·작업·형식만 넣어도 답이 달라져요",["역할: '너는 10년 차 마케터야'","맥락: 대상, 목적, 제약","작업: 무엇을 몇 개","형식: 표, 글자 수, 톤","TOOLS LAB 프롬프트 생성기로 연습"],[["프롬프트 생성기","/tools#prompt"],["PROMPT LIBRARY","/prompts"]]),
 ("내 업무 전용 프롬프트 만들기","prompt","중급","자주 하는 일을 [대괄호] 템플릿으로 바꾸기",["지난주 반복 업무 3개 적기","잘 나온 대화를 템플릿으로 정리","[대괄호]로 바뀌는 부분 표시","프로젝트·GPTs 지침에 저장"],[["프롬프트: 나만의 프롬프트 만들기","/prompts#나만의"]]),
 ("Claude 스킬 시작하기","prompt","고급","반복 작업을 스킬로 만들어 Claude가 매번 같은 방식으로 일하게",["공식 스킬 설치해 써 보기","skill-creator로 내 스킬 초안 만들기","SKILL.md에 언제 쓰는지 한 줄로 분명히","테스트 질문 3개로 동작 확인"],[["SKILLS LIBRARY","/skills"]]),
 ("AI로 15초 광고 영상","content","중급","이미지 → Kling 영상 → 편집까지 실습",["3컷 기획표 채우기","컷별 이미지 만들기","5초 영상 3개 생성","CapCut으로 자막·음악"],[["Kling AI 가이드 (자료실)","/guides/kling-ai"],["광고 소재 키트 (자료실)","/guides/ad-creative-kit"]]),
 ("자료 1개로 콘텐츠 5개","content","중급","하나의 자료를 캐러셀·릴스·스레드·블로그·뉴스레터로",["자료의 핵심 3가지 뽑기","캐러셀 10장 구조로 나누기","릴스 3컷 대본 만들기","TOOLS LAB 콘텐츠 기획 도구 활용"],[["콘텐츠 기획 도구","/tools#plan"]]),
 ("AI 서비스 UX 상태 설계","ux","중급","로딩·스트리밍·오류·거절까지 설계",["9가지 상태 지도 보기","내 화면에서 빠진 상태 찾기","상태별 문구 다듬기"],[["AI UX 체크리스트 (자료실)","/guides/ai-ux-checklist"]]),
 ("모바일 UI 규격 익히기","ux","초급","44·48·4의 배수만 기억하기",["터치 영역 44pt/48dp","간격 4의 배수","본문 대비 4.5:1"],[["모바일 UI 치트시트 (자료실)","/guides/mobile-ui-cheatsheet"]]),
 ("아이디어 검증 6단계","pm","중급","만들기 전에 확인하는 문제-대안-가설-검증-MVP-지표",["문제를 좁게 정의","지금의 대안 찾기","가장 약한 가정 고르기","5명과 이야기하기"],[["아이디어 검증 워크북 (자료실)","/guides/idea-validation-workbook"]]),
 ("기획서·기능명세서 쓰기","pm","중급","AI로 초안을 쓰고 사람이 정책을 채우기",["한 줄 정의 쓰기","Must/Won't 정하기","예외·오류 칸 채우기","개발자 관점 AI 검토"],[["기획 템플릿 (자료실)","/guides/planning-templates"]]),
 ("n8n 첫 자동화 만들기","build","고급","매주 뉴스 요약 메일 자동화를 처음부터",["n8n 클라우드 가입 또는 설치","Schedule → RSS → AI → Gmail 노드 연결","테스트 실행으로 결과 확인","실패 알림 추가"],[["WORKFLOW LAB","/workflows"]]),
 ("말로 만드는 웹 시제품","build","고급","Lovable·v0·Claude로 랜딩페이지 시제품",["문제·해결·기능 3개 정리","프롬프트로 화면 생성","폼·링크 연결","지인 5명 테스트"],[["프롬프트: 코딩 없이 웹 시제품","/prompts#시제품"]]),
]
LS += M.LS
ln_items = [dict(t=t, d=d, cat=c, level=lv, how=st, rel=rel, alias=c) for t,c,lv,d,st,rel in LS]
page("learn", "LEARNING LAB", "초급·중급·고급으로 나눈 AI 활용 가이드와 실습 튜토리얼.",
     "06 · LEARNING LAB", "단계별로 익히는<br><em>AI 실무 학습</em>", "초급부터 고급까지, 짧게 읽고 바로 실습해요.<br>각 레슨은 관련 자료·도구로 이어져요.",
     lab=dict(items=ln_items, facets=[dict(key="level",label="난이도",values={v:v for v in LV}),dict(key="cat",label="주제",values=LCAT)], howLabel="실습 순서", src="그린 AI Lab 자체 제작"),
     placeholder="예) 프롬프트, 영상, n8n, 기획서")

# ───────────────────────── 5. TOOLS LAB ─────────────────────────
TOOLS_BODY = r'''
  <section class="block" id="prompt">
    <p class="label">TOOL 01</p>
    <h2>프롬프트 <em>생성기</em></h2>
    <p class="lead">칸을 채우면 역할·맥락·작업·형식이 갖춰진 프롬프트가 만들어져요.</p>
    <div class="card">
      <div class="field"><label>AI의 역할</label><select id="g_role" class="sel"><option>10년 차 서비스 기획자</option><option>UX/UI 디자이너</option><option>퍼포먼스 마케터</option><option>콘텐츠 에디터</option><option>데이터 분석가</option><option>꼼꼼한 비서</option></select></div>
      <div class="field"><label>하고 싶은 일<small>예) 신규 앱 온보딩 화면 아이디어</small></label><input id="g_task" data-save="g_task"></div>
      <div class="field"><label>상황·맥락<small>대상, 목적, 제약 조건</small></label><textarea id="g_ctx" data-save="g_ctx" style="min-height:70px"></textarea></div>
      <div class="grid2" style="margin-top:0">
        <div class="field"><label>결과 형식</label><select id="g_fmt" class="sel"><option>표</option><option>번호 목록</option><option>3가지 안 비교</option><option>짧은 글(300자)</option><option>단계별 가이드</option></select></div>
        <div class="field"><label>말투</label><select id="g_tone" class="sel"><option>전문적이고 간결하게</option><option>친근하게</option><option>초보자도 이해하게 쉽게</option><option>설득력 있게</option></select></div>
      </div>
      <label class="chk"><input type="checkbox" id="g_q" checked> 부족한 정보는 먼저 질문하게 하기</label>
      <label class="chk"><input type="checkbox" id="g_v" checked> 확실하지 않은 내용은 표시하게 하기</label>
      <div class="prompt" style="margin-top:14px"><div class="ptitle">완성된 프롬프트</div><button class="copy" type="button" data-target="g_out">복사</button><pre id="g_out"></pre></div>
    </div>
  </section>

  <section class="block" id="plan">
    <p class="label">TOOL 02</p>
    <h2>콘텐츠 <em>기획 도구</em></h2>
    <p class="lead">주제 하나로 캐러셀·릴스·스레드 기획 틀과 AI 요청문을 한 번에 만들어요.</p>
    <div class="card">
      <div class="field"><label>주제</label><input id="c_topic" data-save="c_topic" placeholder="예) 회의록 정리 프롬프트"></div>
      <div class="field"><label>타깃</label><input id="c_who" data-save="c_who" placeholder="예) 매주 회의가 많은 3년 차 직장인"></div>
      <div class="field"><label>핵심 메시지 (한 줄)</label><input id="c_msg" data-save="c_msg" placeholder="예) 질문만 바꾸면 회의록이 2분에 끝나요"></div>
      <div class="field"><label>형식</label><div class="chips" id="c_fmt" style="margin-top:6px"><button class="chip on" data-v="carousel">캐러셀 10장</button><button class="chip" data-v="reels">릴스 30초</button><button class="chip" data-v="threads">스레드 5줄</button></div></div>
      <div class="prompt" style="margin-top:14px"><div class="ptitle">기획 틀</div><button class="copy" type="button" data-target="c_out">복사</button><pre id="c_out"></pre></div>
      <div class="prompt light"><div class="ptitle">AI에게 원고 요청하기</div><button class="copy" type="button" data-target="c_ai">복사</button><pre id="c_ai"></pre></div>
    </div>
  </section>

  <section class="block" id="hook">
    <p class="label">TOOL 03</p>
    <h2>후킹 문장 <em>생성기</em></h2>
    <p class="lead">제품·주제와 장점을 넣으면 6가지 공식으로 첫 문장을 만들어요.</p>
    <div class="card">
      <div class="grid2" style="margin-top:0">
        <div class="field"><label>제품·주제</label><input id="h_what" data-save="h_what" placeholder="예) AI 프롬프트"></div>
        <div class="field"><label>타깃</label><input id="h_who" data-save="h_who" placeholder="예) 직장인"></div>
      </div>
      <div class="grid2" style="margin-top:0">
        <div class="field"><label>장점·결과</label><input id="h_gain" data-save="h_gain" placeholder="예) 회의록 2분 정리"></div>
        <div class="field"><label>불편·통념</label><input id="h_pain" data-save="h_pain" placeholder="예) 회의록 쓰느라 야근"></div>
      </div>
      <div id="h_out" class="hooks"></div>
    </div>
    <div class="note gray">지금은 입력값으로 문장을 조합하는 템플릿 도구예요. 앞으로 AI 기능을 붙여 더 자연스러운 문장을 만들 수 있게 확장할 예정이에요.</div>
  </section>

  <section class="block" id="persona">
    <p class="label">TOOL 04</p>
    <h2>페르소나 <em>카드 생성기</em></h2>
    <div class="card">
      <div class="grid2" style="margin-top:0">
        <div class="field"><label>이름·나이</label><input id="p_name" data-save="p_name" placeholder="예) 김민지, 29세"></div>
        <div class="field"><label>직업·상황</label><input id="p_job" data-save="p_job" placeholder="예) 3년 차 마케터, 야근 잦음"></div>
      </div>
      <div class="field"><label>목표</label><input id="p_goal" data-save="p_goal" placeholder="예) 광고 소재를 빨리 만들고 싶다"></div>
      <div class="field"><label>불편</label><input id="p_pain" data-save="p_pain" placeholder="예) 디자인 툴이 어렵고 시간이 없다"></div>
      <div class="field"><label>지금 쓰는 대안</label><input id="p_alt" data-save="p_alt" placeholder="예) 캔바 템플릿, 외주"></div>
      <div class="prompt" style="margin-top:14px"><div class="ptitle">페르소나 카드</div><button class="copy" type="button" data-target="p_out">복사</button><pre id="p_out"></pre></div>
      <div class="prompt light"><div class="ptitle">AI로 보강하기</div><button class="copy" type="button" data-target="p_ai">복사</button><pre id="p_ai"></pre></div>
    </div>
  </section>

  <section class="block" id="course">
    <p class="label">TOOL 05</p>
    <h2>강의 커리큘럼 <em>틀 생성기</em></h2>
    <div class="card">
      <div class="field"><label>강의 주제</label><input id="k_topic" data-save="k_topic" placeholder="예) 생성형 AI로 만드는 브랜드 광고"></div>
      <div class="grid2" style="margin-top:0">
        <div class="field"><label>총 시간(시간)</label><input id="k_hours" type="number" min="1" max="40" value="6"></div>
        <div class="field"><label>수강생 수준</label><select id="k_lv" class="sel"><option>입문</option><option>초중급</option><option>실무자</option></select></div>
      </div>
      <div class="prompt" style="margin-top:14px"><div class="ptitle">커리큘럼 틀</div><button class="copy" type="button" data-target="k_out">복사</button><pre id="k_out"></pre></div>
      <div class="prompt light"><div class="ptitle">AI에게 상세 설계 요청</div><button class="copy" type="button" data-target="k_ai">복사</button><pre id="k_ai"></pre></div>
    </div>
  </section>

  <section class="block" id="size">
    <p class="label">TOOL 06</p>
    <h2>SNS 사이즈 · <em>안전 영역 계산기</em></h2>
    <div class="card">
      <div class="chips" id="z_fmt"><button class="chip on" data-v="reels">릴스·스토리 9:16</button><button class="chip" data-v="feed">피드 4:5</button><button class="chip" data-v="sq">정사각 1:1</button><button class="chip" data-v="yt">유튜브 썸네일 16:9</button></div>
      <div class="zbox"><div id="z_frame"><div id="z_top"></div><div id="z_safe">글자·로고는 여기</div><div id="z_bot"></div></div></div>
      <pre id="z_out" class="zout"></pre>
    </div>
    <div class="note gray">안전 영역은 릴스·스토리 기준 위 약 14%, 아래 약 20%를 비우는 일반적인 기준이에요. 올리기 전 앱 미리보기로 한 번 더 확인해 주세요.</div>
  </section>
'''
TOOLS_STYLE = '''<style>
.sel{margin-top:8px;width:100%;height:48px;border:1.5px solid var(--line);border-radius:14px;background:#fff;padding:0 12px;font:inherit;font-size:15px}
.chk{display:flex;gap:8px;align-items:center;margin-top:10px;font-size:14px;color:var(--ink2)}
.hooks{margin-top:14px;display:grid;gap:8px}
.hk{display:flex;gap:10px;align-items:center;justify-content:space-between;background:var(--bg);border-radius:14px;padding:12px 14px}
.hk small{display:block;font-size:11.5px;font-weight:800;color:var(--green-deep)}
.hk b{font-size:15.5px;font-weight:800;line-height:1.4}
.hk button{flex:none;border:0;border-radius:999px;background:#111;color:#fff;font:inherit;font-size:12.5px;font-weight:700;padding:6px 12px;cursor:pointer}
@media (min-width:768px){.hooks{grid-template-columns:1fr 1fr}}
.zbox{margin-top:14px;display:flex;justify-content:center}
#z_frame{position:relative;width:200px;background:#f1f1ef;border:2px solid #111;border-radius:10px;overflow:hidden}
#z_top,#z_bot{position:absolute;left:0;right:0;background:rgba(229,72,77,.18)}
#z_top{top:0}#z_bot{bottom:0}
#z_safe{position:absolute;left:6%;right:6%;display:grid;place-items:center;border:2px dashed #3E9A58;border-radius:8px;font-size:12px;font-weight:800;color:#3E9A58}
.zout{margin-top:12px;white-space:pre-wrap;font-family:inherit;font-size:14px;color:var(--ink2);background:var(--bg);border-radius:12px;padding:12px}
</style>'''
TOOLS_JS = r'''<script>
document.addEventListener('DOMContentLoaded', function(){
  var $ = function(id){ return document.getElementById(id); };
  document.querySelectorAll('[data-save]').forEach(function(el){ var k = 'gal_t_' + el.dataset.save; try{ if (localStorage.getItem(k)) el.value = localStorage.getItem(k); }catch(e){} el.addEventListener('input', function(){ try{ localStorage.setItem(k, el.value); }catch(e){} }); });
  function v(id, d){ var x = $(id).value.trim(); return x || d; }
  function gen(){
    var p = '너는 ' + $('g_role').value + '야.\n\n'
      + '[하고 싶은 일]\n' + v('g_task','[하고 싶은 일]') + '\n\n'
      + '[상황·맥락]\n' + v('g_ctx','[대상, 목적, 제약 조건]') + '\n\n'
      + '[결과 형식]\n' + $('g_fmt').value + ' 형태로, 말투는 ' + $('g_tone').value + '.\n';
    if ($('g_q').checked) p += '\n시작하기 전에 꼭 필요한 정보가 부족하면 먼저 질문 3개 이내로 물어봐 줘.';
    if ($('g_v').checked) p += '\n확실하지 않은 내용은 [확인 필요]로 표시해 줘.';
    $('g_out').textContent = p;
  }
  ['g_role','g_task','g_ctx','g_fmt','g_tone','g_q','g_v'].forEach(function(id){ $(id).addEventListener('input', gen); $(id).addEventListener('change', gen); });
  gen();
  var fmt = 'carousel';
  function plan(){
    var t = v('c_topic','[주제]'), w = v('c_who','[타깃]'), m = v('c_msg','[핵심 메시지]'), o, ai;
    if (fmt === 'carousel'){
      o = '1장 표지: ' + m + ' (15자 이내로 다듬기)\n2장 공감: ' + w + '이 겪는 불편 한 장면\n3장 문제: 왜 이런 일이 생기는지\n4~8장 해결: ' + t + ' 핵심 5가지 (장마다 1개)\n9장 요약: 오늘 내용 한눈에\n10장 행동: 저장·팔로우·프로필 링크 안내';
      ai = '인스타그램 캐러셀 10장 원고를 써 줘.\n주제: ' + t + '\n타깃: ' + w + '\n핵심 메시지: ' + m + '\n1장은 15자 이내 제목, 2~9장은 장마다 핵심 한 줄 + 설명 2줄, 10장은 저장·팔로우 유도. 과장 없이 구체적으로.';
    } else if (fmt === 'reels'){
      o = '0~3초 훅: ' + m + '\n3~10초 문제: ' + w + '의 불편 장면\n10~25초 해결: ' + t + ' 3포인트 (화면 자막 3개)\n25~30초 행동: 프로필 링크에서 자료 받기';
      ai = '30초 릴스 대본을 써 줘.\n주제: ' + t + ' / 타깃: ' + w + ' / 핵심 메시지: ' + m + '\n장면별 화면 설명, 자막(10자 안팎), 내레이션을 표로. 첫 3초 훅은 3가지 안.';
    } else {
      o = '1줄: ' + m + '\n2줄: ' + w + '이 공감할 상황\n3줄: ' + t + ' 핵심 팁 1\n4줄: 핵심 팁 2\n5줄: 더 보고 싶으면 프로필 링크';
      ai = '스레드에 올릴 5줄 글을 써 줘.\n주제: ' + t + ' / 타깃: ' + w + ' / 핵심 메시지: ' + m + '\n줄마다 40자 안팎, 이모지는 2개 이하, 마지막 줄은 행동 유도. 3가지 버전.';
    }
    $('c_out').textContent = o; $('c_ai').textContent = ai;
  }
  ['c_topic','c_who','c_msg'].forEach(function(id){ $(id).addEventListener('input', plan); });
  $('c_fmt').addEventListener('click', function(e){ var c = e.target.closest('.chip'); if (!c) return; $('c_fmt').querySelectorAll('.chip').forEach(function(x){ x.classList.toggle('on', x === c); }); fmt = c.dataset.v; plan(); });
  plan();
  function hooks(){
    var w = v('h_what','[주제]'), u = v('h_who','[타깃]'), g = v('h_gain','[장점]'), p = v('h_pain','[불편]');
    var H = [['질문형','아직도 ' + p + '하세요?'],['숫자형','3가지만 알면 ' + g],['반전형', w + ', 이렇게 쓰는 줄 몰랐죠?'],['공감형', u + '라면 ' + p + ' 다 겪어봤잖아요'],['금지형', w + ', 이것 모르고 시작하지 마세요'],['결과형', w + ' 하나로 ' + g]];
    $('h_out').innerHTML = H.map(function(h){ return '<div class="hk"><div><small>' + h[0] + '</small><b>' + GALAB.esc(h[1]) + '</b></div><button type="button" data-h="' + GALAB.esc(h[1]) + '">복사</button></div>'; }).join('');
  }
  $('h_out').addEventListener('click', function(e){ var b = e.target.closest('[data-h]'); if (b) GALAB.copy(b.dataset.h).then(function(){ GALAB.say('복사했어요'); }); });
  ['h_what','h_who','h_gain','h_pain'].forEach(function(id){ $(id).addEventListener('input', hooks); });
  hooks();

  function persona(){
    var n = v('p_name','[이름·나이]'), j = v('p_job','[직업·상황]'), g = v('p_goal','[목표]'), p = v('p_pain','[불편]'), a = v('p_alt','[대안]');
    $('p_out').textContent = '👤 ' + n + '\n직업·상황: ' + j + '\n목표: ' + g + '\n불편: ' + p + '\n지금 대안: ' + a + '\n한 줄: "' + p + ' 때문에 ' + g + '을(를) 못 하고 있어요."';
    $('p_ai').textContent = '아래 페르소나를 현실적으로 보강해 줘. 하루 일과, 정보를 얻는 채널, 구매를 결정하는 기준, 망설이는 이유, 이 사람에게 통할 메시지 3개를 추가해 줘. 과장 없이.\n\n' + $('p_out').textContent;
  }
  ['p_name','p_job','p_goal','p_pain','p_alt'].forEach(function(id){ $(id).addEventListener('input', persona); }); persona();
  function course(){
    var t = v('k_topic','[강의 주제]'), h = Math.max(1, Math.min(40, +$('k_hours').value || 6)), lv = $('k_lv').value;
    var parts = Math.max(2, Math.min(8, Math.round(h / 1.5))), per = Math.round(h * 60 / parts);
    var names = ['이해: 개념과 사례','도구: 핵심 툴 익히기','실습 1: 따라 만들기','실습 2: 내 주제로 적용','심화: 품질 높이기','검증: 피드백과 개선','확장: 자동화·응용','발표: 결과물 공유'];
    var o = '강의: ' + t + ' (' + h + '시간 · ' + lv + ')\n학습 목표: 1) ___을 설명할 수 있다 2) ___을 직접 만든다 3) ___에 적용한다\n\n';
    for (var i = 0; i < parts; i++) o += (i+1) + '회 (' + per + '분) ' + names[i % names.length] + '\n   실습: ____ / 결과물: ____\n';
    $('k_out').textContent = o;
    $('k_ai').textContent = '[' + t + '] 강의를 ' + h + '시간, ' + lv + ' 수강생 대상으로 설계해 줘. ' + parts + '개 파트로 나누고 파트마다 학습 목표, 내용, 실습, 결과물, 소요 시간을 표로. 90분마다 실습 1개 이상, 마지막에 수강생 체크리스트.';
  }
  ['k_topic','k_hours','k_lv'].forEach(function(id){ $(id).addEventListener('input', course); $(id).addEventListener('change', course); }); course();
  var Z = { reels:[9,16,'1080 × 1920 (권장 1440 × 2560)',14,20,'릴스·스토리·쇼츠·틱톡'], feed:[4,5,'1080 × 1350 (권장 1440 × 1800)',5,5,'인스타·페북 피드'], sq:[1,1,'1080 × 1080',5,5,'피드·캐러셀·마켓플레이스'], yt:[16,9,'1280 × 720',6,12,'유튜브 썸네일 (오른쪽 아래 재생 시간 표시 피하기)'] };
  function zone(k){
    var z = Z[k], w = 200, hh = Math.round(w * z[1] / z[0]); if (hh > 360){ hh = 360; w = Math.round(hh * z[0] / z[1]); }
    $('z_frame').style.width = w + 'px'; $('z_frame').style.height = hh + 'px';
    $('z_top').style.height = z[3] + '%'; $('z_bot').style.height = z[4] + '%';
    $('z_safe').style.top = (z[3] + 2) + '%'; $('z_safe').style.bottom = (z[4] + 2) + '%';
    var H = parseInt(z[2].split('×')[1]);
    $('z_out').textContent = '쓰는 곳: ' + z[5] + '\n비율: ' + z[0] + ':' + z[1] + '\n크기: ' + z[2] + '\n피할 영역: 위 ' + z[3] + '% (약 ' + Math.round(H * z[3] / 100) + 'px), 아래 ' + z[4] + '% (약 ' + Math.round(H * z[4] / 100) + 'px)';
  }
  $('z_fmt').addEventListener('click', function(e){ var c = e.target.closest('.chip'); if (!c) return; $('z_fmt').querySelectorAll('.chip').forEach(function(x){ x.classList.toggle('on', x === c); }); zone(c.dataset.v); }); zone('reels');
  if (location.hash) { var el = document.querySelector(location.hash); if (el) setTimeout(function(){ el.scrollIntoView(); }, 50); }
});
</script>'''
page("tools", "TOOLS LAB", "웹에서 바로 쓰는 미니 AI 도구 6종: 프롬프트·콘텐츠 기획·후킹 문장·페르소나·커리큘럼·SNS 사이즈.",
     "05 · TOOLS LAB", "웹에서 바로 쓰는<br><em>미니 AI 도구</em>", "가입 없이 바로 써요. 입력한 내용은 이 브라우저에만 저장돼요.",
     body=TOOLS_STYLE + TOOLS_BODY, script=TOOLS_JS)
