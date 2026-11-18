GROUPS = [
 ("empty", "① 입력 전 · 첫 화면", "사용자가 무엇을 물어야 할지 모르는 순간", [
  ("이 AI가 할 수 있는 일을 한 줄로 알려준다", "예) \"여행 일정을 짜고 숙소를 비교해 드려요\""),
  ("바로 눌러볼 수 있는 예시 질문 2~4개가 있다", "빈 입력창만 있으면 첫 질문에서 이탈이 많아요"),
  ("할 수 없는 일·한계를 짧게 알려준다", "예) \"실시간 가격은 확인하지 못해요\""),
  ("입력창 안내 문구가 구체적이다", "\"무엇이든 물어보세요\"보다 \"예) 3박 4일 오사카 일정\""),
 ]),
 ("input", "② 입력 중", "질문을 쓰고 보내는 순간", [
  ("긴 글·파일을 넣을 수 있는지, 한도가 얼마인지 보인다", ""),
  ("보내기 버튼은 내용이 있을 때만 활성화된다", ""),
  ("엔터·줄바꿈 동작이 명확하다", "모바일은 줄바꿈, PC는 엔터=보내기가 일반적"),
  ("첨부한 파일이 제대로 올라갔는지 보인다", "파일명·미리보기·업로드 진행률"),
 ]),
 ("wait", "③ 요청 직후 · 기다리는 중", "응답이 시작되기 전, 가장 불안한 구간", [
  ("보낸 즉시(0.1초 안) 무언가 반응한다", "내 메시지가 바로 올라가고 대기 표시가 뜨기"),
  ("오래 걸리면 지금 무엇을 하는지 알려준다", "예) \"자료를 찾는 중… → 정리하는 중…\""),
  ("기다리는 중에도 멈추기(취소)를 할 수 있다", ""),
  ("대기 표시가 화면을 막지 않는다", "다른 대화 내용을 계속 볼 수 있게"),
 ]),
 ("stream", "④ 답이 나오는 중 · 스트리밍", "글자가 차례로 나타나는 구간", [
  ("글자가 나오는 동안 화면이 위아래로 튀지 않는다", ""),
  ("사용자가 위로 스크롤하면 자동 스크롤을 멈춘다", "읽고 있는 걸 끌어내리지 않기"),
  ("'맨 아래로' 버튼으로 최신 답으로 돌아갈 수 있다", ""),
  ("답이 끝났다는 것이 분명하게 보인다", "커서 사라짐 + 후속 버튼 등장"),
 ]),
 ("done", "⑤ 답 완료 · 다음 행동", "답을 받고 무엇을 할지 정하는 순간", [
  ("복사, 다시 생성, 수정 요청 버튼이 있다", ""),
  ("좋아요·싫어요 등 가벼운 피드백을 줄 수 있다", "싫어요를 누르면 이유를 짧게 고르게"),
  ("이어서 할 만한 질문을 제안한다", "추천 질문 2~3개"),
  ("결과를 저장·공유·내보낼 수 있다", "업무용이라면 특히 중요"),
 ]),
 ("error", "⑥ 오류 · 실패", "네트워크, 서버, 한도 초과", [
  ("무슨 일이 생겼는지 사람 말로 알려준다", "\"Error 500\" 대신 \"잠시 연결이 끊겼어요\""),
  ("다시 시도 버튼이 바로 옆에 있다", ""),
  ("실패해도 사용자가 쓴 질문은 지워지지 않는다", ""),
  ("사용 한도에 걸렸을 때 언제 다시 쓸 수 있는지 알려준다", ""),
  ("답이 중간에 끊기면 '이어서 받기'를 할 수 있다", ""),
 ]),
 ("refuse", "⑦ 빈 응답 · 거절 · 모를 때", "AI가 답하지 못하거나 확신이 없을 때", [
  ("답할 수 없을 때 이유와 대안을 함께 준다", "\"이 요청은 도와드리기 어려워요. 대신 ~는 가능해요\""),
  ("모르는 것은 모른다고 표시한다", "추측과 사실을 구분해 보여주기"),
  ("질문이 모호하면 되묻는다", "선택지를 주면 더 쉬워요"),
 ]),
 ("trust", "⑧ 신뢰 · 투명성", "AI 답을 믿어도 되는지 판단하는 정보", [
  ("근거·출처가 있으면 링크로 보여준다", ""),
  ("AI가 만든 결과라는 것이 분명하다", ""),
  ("중요한 결정(돈, 건강, 법)에는 확인을 권한다", ""),
  ("내 데이터가 어떻게 쓰이는지 쉽게 찾을 수 있다", "학습 사용 여부, 대화 삭제 방법"),
 ]),
 ("a11y", "⑨ 접근성 · 기본기", "모두가 쓸 수 있게", [
  ("스트리밍 중 스크린리더가 끝없이 읽지 않는다", "완료 후 한 번에 알리기 등"),
  ("대기·오류 상태를 색으로만 구분하지 않는다", "아이콘·문구 함께"),
  ("글자 크기를 키워도 레이아웃이 깨지지 않는다", ""),
  ("버튼 터치 영역이 44pt(48dp) 이상이다", ""),
 ]),
]

n = 0; parts = []
for key, title, sub, items in GROUPS:
    lis = []
    for t, d in items:
        n += 1
        span = f"<span>{d}</span>" if d else ""
        lis.append(f'<li><label><input type="checkbox" id="u{n}"><div class="t"><b>{t}</b>{span}</div></label></li>')
    parts.append(f'''    <h3 class="sub" id="g-{key}">{title} <small style="font-weight:500;color:var(--gray);font-size:13px">{sub}</small></h3>
    <ul class="checks">{"".join(lis)}</ul>''')
TOTAL = n

META = dict(
    source="그린 AI Lab 강의 「AI 응답 상태별 UX 설계」 기반",
    slug="ai-ux-checklist",
    title="AI 서비스 UX 상태별 설계 체크리스트",
    desc="입력 전부터 스트리밍, 오류, 거절까지 AI 서비스의 9가지 상태별 UX 점검표",
    eyebrow="AI UX CHECKLIST",
    h1="AI 서비스 UX<br><em>상태별 설계 체크리스트</em>",
    intro=f"AI 서비스는 '답이 나오기까지'의 경험이 절반이에요.<br>9가지 상태, {TOTAL}개 항목을 체크하며 설계를 점검해 보세요.",
    buttons=[("점검 시작하기", "#check"), ("상태별 문구 예시", "#copy")],
    badges=["무료 자료", f"{TOTAL}개 항목", "진행 상황 자동 저장", "디자이너 · 기획자"],
    toc=[("상태 지도", "map"), ("체크리스트", "check"), ("문구 예시", "copy"), ("AI로 점검", "ai")],
    cta_h2="AI 서비스 UX를<br><em>실제 화면으로</em> 설계해 봐요",
    cta_p="AI 응답 상태별 화면을 피그마로 직접 설계하는 그린 AI Lab UX/UI 클래스예요.",
)

BODY = r'''
  <section class="block" id="map">
    <p class="label">STATE MAP</p>
    <h2>AI 서비스의 <em>9가지 상태</em></h2>
    <p class="lead">일반 앱은 "누르면 결과"지만, AI는 기다림·스트리밍·불확실한 답이 끼어 있어요. 이 상태들을 빠짐없이 설계했는지가 품질을 갈라요.</p>
    <div class="grid2 c3">
      <div class="mini"><span class="k">①</span><b>입력 전</b><p>무엇을 물을지 안내</p></div>
      <div class="mini"><span class="k">②</span><b>입력 중</b><p>파일·한도·보내기</p></div>
      <div class="mini"><span class="k">③</span><b>기다리는 중</b><p>즉시 반응·진행 상황</p></div>
      <div class="mini"><span class="k">④</span><b>스트리밍</b><p>흔들림 없는 출력</p></div>
      <div class="mini"><span class="k">⑤</span><b>완료</b><p>다음 행동 제안</p></div>
      <div class="mini"><span class="k">⑥</span><b>오류</b><p>사람 말·다시 시도</p></div>
      <div class="mini"><span class="k">⑦</span><b>거절·모름</b><p>이유와 대안</p></div>
      <div class="mini"><span class="k">⑧</span><b>신뢰</b><p>출처·AI 표시</p></div>
      <div class="mini"><span class="k">⑨</span><b>접근성</b><p>모두가 쓸 수 있게</p></div>
    </div>
  </section>

  <section class="block" id="check">
    <p class="label">CHECKLIST</p>
    <h2>상태별 <em>점검하기</em></h2>
    <p class="lead">체크한 내용은 이 브라우저에 저장돼요. 프로젝트마다 처음부터 다시 쓰려면 "처음부터 다시"를 누르세요.</p>
    <div data-checklist="aiux">
      <div class="progress"><div class="progress-top">점검 진행<span data-num>0 / 0</span></div><div class="bar"><i></i></div><button class="reset" type="button">처음부터 다시</button></div>
''' + "\n".join(parts) + r'''
    </div>
  </section>

  <section class="block" id="copy">
    <p class="label">MICROCOPY</p>
    <h2>상태별 <em>문구 예시</em></h2>
    <div class="tbl-wrap"><table class="tbl">
      <tr><th>상태</th><th>아쉬운 문구</th><th>바꾼 문구</th></tr>
      <tr><td>첫 화면</td><td>무엇이든 물어보세요</td><td>오늘 할 일을 알려주시면 일정으로 정리해 드려요</td></tr>
      <tr><td>기다림</td><td>로딩 중…</td><td>자료를 찾고 있어요 (보통 10초 안에 끝나요)</td></tr>
      <tr><td>오래 걸림</td><td>(아무 표시 없음)</td><td>평소보다 오래 걸리고 있어요. 멈추고 다시 해볼까요?</td></tr>
      <tr><td>네트워크 오류</td><td>Error: Network failed</td><td>연결이 잠시 끊겼어요. 쓰신 내용은 그대로 있어요 · [다시 보내기]</td></tr>
      <tr><td>한도 초과</td><td>요청 한도를 초과했습니다</td><td>오늘 사용량을 다 썼어요. 내일 오전 9시에 다시 쓸 수 있어요</td></tr>
      <tr><td>거절</td><td>요청을 처리할 수 없습니다</td><td>이 부분은 도와드리기 어려워요. 대신 ○○는 할 수 있어요</td></tr>
      <tr><td>불확실</td><td>(단정적인 답)</td><td>확실하지 않아요. 공식 사이트에서 한 번 더 확인해 주세요</td></tr>
      <tr><td>완료 후</td><td>(버튼 없음)</td><td>[복사] [더 짧게] [표로 바꾸기] [다시 만들기]</td></tr>
    </table></div>
  </section>

  <section class="block" id="ai">
    <p class="label">WITH AI</p>
    <h2>AI로 <em>내 화면 점검</em>하기</h2>
    <div class="prompt"><div class="ptitle">상태별 빈틈 찾기 프롬프트</div><button class="copy" type="button">복사</button>
<pre>나는 [서비스 설명] AI 서비스를 설계하고 있어.
현재 설계한 화면은 다음과 같아: [화면 목록과 설명]
아래 9가지 상태 중 설계가 빠졌거나 부족한 부분을 찾아 표로 정리해 줘.
상태: 입력 전 / 입력 중 / 기다리는 중 / 스트리밍 / 완료 / 오류 / 거절·모름 / 신뢰 / 접근성
표 항목: 상태, 빠진 점, 사용자에게 생길 문제, 개선안, 우선순위(상/중/하)</pre></div>
    <div class="prompt"><div class="ptitle">상태별 문구 세트 만들기</div><button class="copy" type="button">복사</button>
<pre>[서비스 이름]의 말투는 [친근한/전문적인]이야.
첫 화면 안내, 예시 질문 3개, 대기 중 단계별 문구 3개, 오류 문구 4종(네트워크·서버·한도·답 끊김), 거절 문구, 불확실할 때 문구를 만들어 줘.
모든 문구는 25자 안팎, 오류 문구에는 해결 방법을 꼭 포함해 줘.</pre></div>
  </section>
'''
