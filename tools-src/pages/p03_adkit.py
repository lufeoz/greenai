META = dict(
    source="Meta 광고 사이즈 가이드 기반 정리(2026.11) · 그린 AI Lab",
    slug="ad-creative-kit",
    title="AI 광고 소재 제작 키트",
    desc="광고 이미지 프롬프트 공식, 카피 공식, SNS 광고 사이즈 규격표를 한곳에",
    eyebrow="AD CREATIVE KIT",
    h1="AI로 만드는<br><em>광고 소재 제작 키트</em>",
    intro="이미지 프롬프트 공식 6종, 카피 공식, 사이즈 규격표까지.<br>광고 하나 만들 때 필요한 걸 순서대로 모았어요.",
    buttons=[("이미지 공식 보기", "#image"), ("사이즈 규격표", "#size")],
    badges=["무료 자료", "이미지 6종", "카피 공식", "2026 사이즈표"],
    toc=[("광고 구조", "struct"), ("이미지 6종", "image"), ("카피 공식", "copy"), ("사이즈표", "size"), ("점검표", "check")],
    cta_h2="내 브랜드 광고 소재를<br><em>직접 완성</em>해 보세요",
    cta_p="브랜드 톤에 맞는 이미지·영상·카피를 AI로 만들고 실제 광고까지 세팅하는 그린 AI Lab 클래스예요.",
)

def img(title, tag, body):
    return f'''      <div class="prompt"><div class="ptitle">{title}</div><button class="copy" type="button">복사</button><pre>{body}</pre><div class="ptags"><span>{tag}</span></div></div>'''

BODY = r'''
  <section class="block" id="struct">
    <p class="label">BEFORE YOU START</p>
    <h2>잘 되는 광고 소재의 <em>3요소</em></h2>
    <div class="grid2 c3">
      <div class="mini"><span class="k">이미지</span><b>0.5초 안에 멈추게</b><p>제품이 크게, 배경은 단순하게, 색 대비는 강하게.</p></div>
      <div class="mini"><span class="k">헤드라인</span><b>한 가지 약속</b><p>이 제품으로 얻는 것 하나만. 15자 안팎.</p></div>
      <div class="mini"><span class="k">행동 문구</span><b>다음 행동 하나</b><p>"지금 구매", "무료 체험", "자세히 보기" 중 하나만.</p></div>
    </div>
    <div class="note gray"><b>팁</b> 한 번에 완벽한 소재 하나보다, 이미지 2개 × 헤드라인 2개 = 4개 조합을 만들어 성과를 비교하는 게 훨씬 빨라요.</div>
  </section>

  <section class="block" id="image">
    <p class="label">IMAGE PROMPTS</p>
    <h2>광고 이미지 <em>프롬프트 6종</em></h2>
    <p class="lead">ChatGPT 이미지, Midjourney, Kling 이미지 등 어디서든 쓸 수 있어요. <b>[대괄호]</b>만 바꾸고 마지막 비율은 광고 위치에 맞춰 주세요.</p>
    <div class="pgrid">
''' + "\n".join([
 img("① 제품 단독컷 (기본)", "피드 · 상세페이지", "[제품], 화면 가운데, 단색 [배경색] 배경, 부드러운 스튜디오 조명, 아래로 은은한 그림자, 제품 디테일이 선명한 상업 광고 사진, 미니멀, 비율 4:5"),
 img("② 라이프스타일컷", "공감 · 브랜드 무드", "[타깃]이 [장소]에서 [제품]을 자연스럽게 사용하는 장면, 얼굴은 화면 밖, 손과 제품 위주, 따뜻한 자연광, 일상 사진 같은 분위기, 비율 4:5"),
 img("③ 플랫레이", "구성품 · 세트 상품", "[제품]과 [함께 쓰는 소품 3가지]를 위에서 내려다본 플랫레이 구도, [배경 재질] 위, 간격을 두고 정돈된 배치, 밝고 깨끗한 조명, 비율 1:1"),
 img("④ 전·후 비교", "효과 강조", "화면을 반으로 나눈 비교 이미지, 왼쪽은 [사용 전 상태]로 어둡고 흐릿한 톤, 오른쪽은 [사용 후 상태]로 밝고 선명한 톤, 가운데 세로 구분선, 비율 1:1"),
 img("⑤ 문구 여백컷", "텍스트 배너용", "[제품]이 화면 아래쪽 1/3에 놓임, 위쪽 2/3는 비어 있는 [배경색] 배경, 문구를 넣을 넓은 여백, 고급 광고 사진, 비율 9:16"),
 img("⑥ 시즌·이벤트컷", "할인 · 시즌 프로모션", "[제품] 주변에 [시즌 소품: 눈송이/벚꽃/선물상자], [시즌 색] 톤, 축제 분위기지만 제품이 가장 또렷하게, 상업 광고 사진, 비율 4:5"),
]) + r'''
    </div>
    <div class="note"><b>글자는 AI에 맡기지 마세요.</b> 이미지 속 한글은 깨지기 쉬워요. 문구·가격·로고는 캔바나 피그마에서 따로 얹는 게 정확해요.</div>
    <h3 class="sub">브랜드 톤을 고정하는 문장</h3>
    <div class="prompt light"><div class="ptitle">모든 이미지 프롬프트 끝에 붙이기</div><button class="copy" type="button">복사</button>
<pre>브랜드 톤: [브랜드 색 2가지] 위주의 색감, [미니멀/따뜻한/고급스러운/발랄한] 분위기, 과한 장식 없음, 같은 조명과 색 보정 유지</pre></div>
  </section>

  <section class="block" id="copy">
    <p class="label">COPY FORMULA</p>
    <h2>헤드라인 <em>공식 6가지</em></h2>
    <div class="tbl-wrap"><table class="tbl">
      <tr><th>공식</th><th>틀</th><th>예시</th></tr>
      <tr><td>숫자형</td><td>[숫자]로 [결과]</td><td>하루 3분으로 끝나는 홈케어</td></tr>
      <tr><td>질문형</td><td>아직도 [불편]하세요?</td><td>아직도 손으로 일정 정리하세요?</td></tr>
      <tr><td>반전형</td><td>[통념]인 줄 알았는데</td><td>비싼 게 좋은 줄 알았는데</td></tr>
      <tr><td>공감형</td><td>[상황]일 때 있잖아요</td><td>월요일 아침, 눈 뜨기 싫을 때</td></tr>
      <tr><td>금지형</td><td>[행동] 하지 마세요</td><td>이 글 보기 전엔 사지 마세요</td></tr>
      <tr><td>결과형</td><td>[기간] 뒤 [달라진 모습]</td><td>2주 뒤 달라진 피부 결</td></tr>
    </table></div>
    <div class="pgrid" style="margin-top:12px">
      <div class="prompt"><div class="ptitle">헤드라인 18개 한 번에</div><button class="copy" type="button">복사</button>
<pre>[제품]의 광고 헤드라인을 써 줘.
타깃: [타깃] / 핵심 장점: [장점] / 톤: [톤]
숫자형·질문형·반전형·공감형·금지형·결과형으로 3개씩, 각 15자 안팎.
과장 광고 표현(최고, 1위, 100% 등)은 근거 없이 쓰지 마.</pre></div>
      <div class="prompt"><div class="ptitle">본문 + 행동 문구 세트</div><button class="copy" type="button">복사</button>
<pre>아래 헤드라인에 맞는 광고 본문을 써 줘.
헤드라인: [헤드라인]
- 본문 2줄: 장점 1개 + 그걸 믿을 이유 1개
- 행동 문구 3안 (8자 이내)
- 릴스·스토리용 짧은 버전(40자 이내)도 따로</pre></div>
      <div class="prompt"><div class="ptitle">A/B 테스트 조합표</div><button class="copy" type="button">복사</button>
<pre>[제품] 광고 A/B 테스트를 하려고 해.
이미지 콘셉트 2개, 헤드라인 2개를 제안하고 4가지 조합을 표로 만들어 줘.
조합마다 어떤 가설을 확인하는지 한 줄씩 적어 줘.</pre></div>
      <div class="prompt"><div class="ptitle">경쟁사 광고 분석</div><button class="copy" type="button">복사</button>
<pre>아래는 경쟁 브랜드 광고 문구들이야. 자주 쓰는 메시지, 아무도 말하지 않는 빈틈, 우리가 차별화할 수 있는 메시지 3개를 정리해 줘.
[경쟁사 광고 문구 붙여넣기]</pre></div>
    </div>
  </section>

  <section class="block" id="size">
    <p class="label">SIZE GUIDE · 2026</p>
    <h2>SNS 광고 <em>사이즈 규격표</em></h2>
    <p class="lead">메타(인스타그램·페이스북) 광고는 <b>4:5, 1:1, 9:16</b> 세 가지 비율이면 대부분의 자리를 덮을 수 있어요.</p>
    <div class="tbl-wrap"><table class="tbl">
      <tr><th>자리</th><th>비율</th><th>권장 크기 (px)</th><th>메모</th></tr>
      <tr><td>인스타·페북 피드</td><td>4:5</td><td>1080×1350 이상<br>(1440×1800 권장)</td><td>모바일 화면을 가장 많이 차지해요</td></tr>
      <tr><td>피드 (정사각)</td><td>1:1</td><td>1080×1080</td><td>마켓플레이스·캐러셀에도 무난</td></tr>
      <tr><td>스토리 · 릴스</td><td>9:16</td><td>1080×1920 이상<br>(1440×2560 권장)</td><td>위 14%, 아래 20%는 글자 피하기</td></tr>
      <tr><td>링크 · 가로형</td><td>1.91:1</td><td>1200×628</td><td>일부 자리에서만 쓰여요</td></tr>
      <tr><td>유튜브 쇼츠</td><td>9:16</td><td>1080×1920</td><td>릴스용 영상 그대로 활용 가능</td></tr>
      <tr><td>유튜브 썸네일</td><td>16:9</td><td>1280×720</td><td>작게 보여도 읽히는 큰 글자</td></tr>
    </table></div>
    <div class="note gray">규격은 플랫폼 정책에 따라 바뀌어요. 광고를 올리기 전 메타 광고 관리자 미리보기에서 한 번 더 확인해 주세요. (2026년 11월 기준 정리)</div>
    <h3 class="sub">한 번 만들어 세 비율로 쓰는 법</h3>
    <div class="card"><ol>
      <li><b>9:16으로 먼저 만들기</b> — 위아래 여백을 넉넉히 두고 핵심은 가운데에</li>
      <li><b>4:5로 자르기</b> — 위아래를 잘라도 제품과 문구가 살아 있는지 확인</li>
      <li><b>1:1로 자르기</b> — 가운데 정사각형 안에 핵심이 다 들어가는지 확인</li>
    </ol></div>
  </section>

  <section class="block" id="check">
    <p class="label">CHECKLIST</p>
    <h2>광고 올리기 전 <em>점검표</em></h2>
    <div data-checklist="adkit">
      <div class="progress"><div class="progress-top">점검 진행<span data-num>0 / 0</span></div><div class="bar"><i></i></div><button class="reset" type="button">처음부터 다시</button></div>
      <ul class="checks">
        <li><label><input type="checkbox" id="a1"><div class="t"><b>썸네일 크기로 줄여도 제품이 보인다</b></div></label></li>
        <li><label><input type="checkbox" id="a2"><div class="t"><b>헤드라인은 약속 하나만 담았다</b></div></label></li>
        <li><label><input type="checkbox" id="a3"><div class="t"><b>이미지 속 글자가 깨지지 않았다</b><span>AI가 만든 글자는 지우고 직접 얹기</span></div></label></li>
        <li><label><input type="checkbox" id="a4"><div class="t"><b>9:16 소재의 글자가 안전 영역 안에 있다</b></div></label></li>
        <li><label><input type="checkbox" id="a5"><div class="t"><b>근거 없는 최상급 표현이 없다</b><span>최고, 1위, 100% 효과 등</span></div></label></li>
        <li><label><input type="checkbox" id="a6"><div class="t"><b>실제 제품과 너무 다르게 보이지 않는다</b><span>AI 이미지는 실제보다 과하게 나오기 쉬워요</span></div></label></li>
        <li><label><input type="checkbox" id="a7"><div class="t"><b>비교할 조합을 2개 이상 준비했다</b></div></label></li>
        <li><label><input type="checkbox" id="a8"><div class="t"><b>플랫폼의 AI 생성 콘텐츠 표시 정책을 확인했다</b></div></label></li>
      </ul>
    </div>
  </section>
'''
