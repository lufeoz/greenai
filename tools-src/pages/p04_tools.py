TOOLS = [
 # (약칭, 이름, 설명, 쓰임, 태그)
 ("GPT", "ChatGPT", "가장 범용적인 AI 비서. 글쓰기, 아이디어, 이미지 생성, 파일 분석까지 한곳에서.", ["초안 쓰기", "아이디어", "이미지 생성"], "text image"),
 ("C", "Claude", "긴 글과 문서 작업에 강해요. 보고서·기획서 정리, 글 다듬기, 코드 작성에 자주 써요.", ["긴 문서", "글 다듬기", "코드"], "text build"),
 ("G", "Gemini", "구글 서비스(지메일, 드라이브, 문서)와 잘 이어져요. 구글 업무 환경이라면 편해요.", ["구글 연동", "요약", "리서치"], "text"),
 ("P", "Perplexity", "답마다 출처 링크를 달아 주는 검색형 AI. 최신 정보를 찾을 때 좋아요.", ["출처 있는 검색", "시장 조사"], "text"),
 ("NB", "NotebookLM", "내가 올린 자료(PDF, 문서, 링크)만 근거로 답해요. 자료 공부·강의 준비에 좋아요.", ["내 자료 요약", "학습"], "text"),
 ("MJ", "Midjourney", "감성적이고 완성도 높은 이미지. 브랜드 무드 보드, 콘셉트 이미지에 강해요.", ["무드 이미지", "콘셉트 아트"], "image"),
 ("ID", "Ideogram", "이미지 안에 글자를 비교적 잘 넣어요. 포스터·썸네일 시안에 유용해요.", ["글자 있는 이미지", "썸네일 시안"], "image"),
 ("K", "Kling AI", "이미지·텍스트로 영상을 만들어요. 제품 광고, 숏폼 영상 소스에 많이 써요.", ["이미지→영상", "광고 영상"], "video image"),
 ("R", "Runway", "영상 생성과 편집 기능을 함께 갖춘 툴. 배경 지우기 등 편집 기능도 있어요.", ["영상 생성", "영상 편집"], "video"),
 ("V", "Google Veo", "구글의 영상 생성 모델. Gemini 앱 등에서 쓸 수 있어요.", ["영상 생성"], "video"),
 ("CC", "CapCut", "자동 자막, 템플릿, 음악까지 되는 편집 앱. 숏폼 마무리 편집용으로 가장 쉬워요.", ["숏폼 편집", "자동 자막"], "video"),
 ("VR", "Vrew", "말소리를 인식해 한국어 자막을 자동으로 만들어요. 강의·인터뷰 영상에 편해요.", ["한국어 자막", "강의 영상"], "video"),
 ("11", "ElevenLabs", "자연스러운 AI 음성(내레이션). 여러 언어 지원.", ["내레이션", "더빙"], "audio"),
 ("TC", "Typecast", "한국어 AI 성우 목소리가 다양해요. 국내 콘텐츠 내레이션에 많이 써요.", ["한국어 성우"], "audio"),
 ("S", "Suno", "가사와 분위기만 적으면 노래·배경음악을 만들어요.", ["배경음악", "징글"], "audio"),
 ("F", "Figma", "UI 디자인의 기본 툴. AI 기능으로 시안 생성, 이름 정리 등을 도와줘요.", ["UI 디자인", "프로토타입"], "design build"),
 ("CV", "Canva", "템플릿 기반 디자인. 카드뉴스, 썸네일, 상세페이지를 빠르게 만들 때.", ["카드뉴스", "썸네일"], "design image"),
 ("GM", "Gamma", "글만 넣으면 발표 슬라이드 초안을 만들어 줘요.", ["슬라이드", "제안서"], "design text"),
 ("N", "Notion AI", "노션 안에서 요약, 글쓰기, 회의록 정리를 해줘요.", ["회의록", "문서 정리"], "text"),
 ("LV", "Lovable · v0", "말로 설명하면 웹 화면을 코드로 만들어 줘요. 아이디어 시제품을 빠르게.", ["웹 시제품", "랜딩페이지"], "build"),
]
TAG = {"text": "글·리서치", "image": "이미지", "video": "영상", "audio": "음성·음악", "design": "디자인·문서", "build": "만들기(시제품)"}

cards = "\n".join(
    f'''      <div class="tool" data-item data-tags="{t}"><span class="ic">{ab}</span><div><b>{n}</b><p>{d}</p><div class="use">{"".join(f"<span>{u}</span>" for u in us)}</div></div></div>'''
    for ab, n, d, us, t in TOOLS)
chips = '<button class="chip on" data-v="all">전체</button>' + "".join(f'<button class="chip" data-v="{k}">{v}</button>' for k, v in TAG.items())

META = dict(
    source="각 툴 공식 소개 기준 정리(2026.11) · 기능·요금은 변동될 수 있음",
    slug="ai-tools",
    title="목적별 생성형 AI 툴 가이드",
    desc="글·이미지·영상·음성·디자인·시제품까지, 이 작업엔 어떤 AI를 쓸지 한눈에",
    eyebrow="AI TOOL MAP · 2026",
    h1="이 작업엔 이 툴,<br><em>목적별 AI 툴 가이드</em>",
    intro="툴이 너무 많아서 뭘 써야 할지 모르겠다면<br>하고 싶은 일부터 고르세요. 툴은 그다음이에요.",
    buttons=[("툴 찾기", "#map"), ("조합 레시피", "#recipe")],
    badges=["무료 자료", "툴 20개", "작업별 조합 4가지"],
    toc=[("고르는 법", "pick"), ("툴 지도", "map"), ("조합 레시피", "recipe"), ("주의할 점", "care")],
    cta_h2="툴을 아는 것에서<br><em>결과물을 만드는 것</em>까지",
    cta_p="툴 조합으로 실제 콘텐츠·광고·시제품을 만들어 보는 그린 AI Lab 클래스예요.",
)

BODY = f'''
  <section class="block" id="pick">
    <p class="label">HOW TO PICK</p>
    <h2>툴 고르기 전 <em>3가지 질문</em></h2>
    <div class="card"><ol>
      <li><b>결과물이 뭔가요?</b> — 글, 이미지, 영상, 소리, 화면 중 하나로 좁혀요.</li>
      <li><b>내 자료를 넣어야 하나요?</b> — 그렇다면 파일을 올릴 수 있는 툴(ChatGPT, Claude, NotebookLM 등).</li>
      <li><b>최신 정보가 필요한가요?</b> — 그렇다면 출처를 보여주는 검색형(Perplexity 등)으로 확인해요.</li>
    </ol></div>
    <div class="note"><b>하나만 고른다면</b> 범용 AI 비서(ChatGPT·Claude·Gemini 중 하나) 하나를 깊게 쓰는 게 툴 열 개를 얕게 쓰는 것보다 훨씬 나아요. 나머지는 필요할 때 더하세요.</div>
  </section>

  <section class="block" id="map">
    <p class="label">TOOL MAP</p>
    <h2>목적별 <em>툴 지도</em></h2>
    <div class="chips" data-filter="tlist">{chips}</div>
    <div class="tools" id="tlist">
{cards}
    </div>
    <p class="empty-msg" data-empty="tlist">해당하는 툴이 없어요.</p>
  </section>

  <section class="block" id="recipe">
    <p class="label">RECIPES</p>
    <h2>작업별 <em>툴 조합 레시피</em></h2>
    <details class="acc" open><summary><div>✍️ 블로그 글 1편<small>리서치 → 초안 → 썸네일</small></div></summary><div class="acc-body">
      <div class="card" style="margin-top:0"><ol>
        <li><b>Perplexity</b>로 주제 관련 최신 자료와 출처 모으기</li>
        <li><b>ChatGPT·Claude</b>에 자료를 붙여넣고 개요 → 초안 쓰기</li>
        <li>초안에 내 경험·사례를 직접 넣어 다듬기 (여기가 가장 중요해요)</li>
        <li><b>Canva·Ideogram</b>으로 썸네일 만들기</li>
      </ol></div></div></details>
    <details class="acc"><summary><div>🎬 15초 광고 영상<small>기획 → 이미지 → 영상 → 편집</small></div></summary><div class="acc-body">
      <div class="card" style="margin-top:0"><ol>
        <li><b>ChatGPT·Claude</b>로 3컷 구성과 자막 기획</li>
        <li><b>Midjourney·ChatGPT 이미지·Kling 이미지</b>로 컷별 기준 이미지</li>
        <li><b>Kling AI</b>로 이미지를 5초 영상으로</li>
        <li><b>CapCut</b>으로 이어 붙이고 자막·음악 넣기</li>
      </ol><p>자세한 방법은 자료실의 「Kling AI 광고 영상 제작 가이드」를 보세요.</p></div></div></details>
    <details class="acc"><summary><div>🎓 강의 자료 1세트<small>자료 정리 → 목차 → 슬라이드</small></div></summary><div class="acc-body">
      <div class="card" style="margin-top:0"><ol>
        <li><b>NotebookLM</b>에 참고 자료를 올려 핵심 정리</li>
        <li><b>Claude·ChatGPT</b>로 학습 목표와 목차, 실습 설계</li>
        <li><b>Gamma</b>로 슬라이드 초안 → 피그마·키노트에서 다듬기</li>
        <li><b>Vrew</b>로 녹화 강의 자막 넣기</li>
      </ol></div></div></details>
    <details class="acc"><summary><div>📱 앱 아이디어 시제품<small>기획 → 화면 → 동작하는 시제품</small></div></summary><div class="acc-body">
      <div class="card" style="margin-top:0"><ol>
        <li><b>ChatGPT·Claude</b>로 문제 정의와 핵심 기능 3개 정리</li>
        <li><b>Figma</b>로 주요 화면 3~5개 그리기</li>
        <li><b>Lovable·v0</b> 같은 툴로 실제로 눌러볼 수 있는 시제품 만들기</li>
        <li>지인 5명에게 써보게 하고 피드백 받기</li>
      </ol><p>아이디어 검증은 자료실의 「AI로 하는 앱 아이디어 검증 워크북」과 함께 쓰면 좋아요.</p></div></div></details>
  </section>

  <section class="block" id="care">
    <p class="label">CAUTION</p>
    <h2>쓰기 전에 <em>꼭 알아둘 것</em></h2>
    <div class="grid2">
      <div class="mini"><span class="k">사실 확인</span><b>AI는 그럴듯하게 틀려요</b><p>숫자, 인물, 법·제도 정보는 반드시 원문으로 확인해요.</p></div>
      <div class="mini"><span class="k">정보 보호</span><b>민감한 정보는 빼고</b><p>고객 개인정보, 회사 기밀은 넣기 전에 지우거나 바꿔요.</p></div>
      <div class="mini"><span class="k">저작권</span><b>상업용이면 약관 확인</b><p>유료 플랜·상업 이용 조건은 툴마다 달라요.</p></div>
      <div class="mini"><span class="k">AI 표시</span><b>플랫폼 정책 따르기</b><p>광고·SNS는 AI 생성 콘텐츠 표시 규칙이 있을 수 있어요.</p></div>
    </div>
    <div class="note gray">툴의 기능과 요금제는 자주 바뀌어요. 이 페이지는 2026년 11월 기준으로 정리했고, 가입 전에 각 툴의 공식 사이트에서 최신 내용을 확인해 주세요.</div>
  </section>
'''
