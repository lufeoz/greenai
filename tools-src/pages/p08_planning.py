META = dict(
    slug="planning-templates",
    title="서비스 기획서 · 기능명세서 템플릿",
    desc="바로 쓰는 서비스 기획서(워드)와 기능명세서(엑셀) 템플릿, 작성법과 AI 초안 프롬프트",
    eyebrow="PLANNING TEMPLATES",
    h1="바로 쓰는<br><em>서비스 기획서 · 기능명세서</em>",
    intro="빈 문서 앞에서 막막하지 않게, 목차와 작성 예시가 들어 있는<br>워드·엑셀 템플릿을 받아 가세요.",
    buttons=[("템플릿 받기", "#download"), ("작성법 보기", "#guide")],
    badges=["무료 자료", "워드 · 엑셀", "작성 예시 포함", "AI 초안 프롬프트"],
    toc=[("문서 구분", "kind"), ("다운로드", "download"), ("기획서 작성법", "guide"), ("기능명세 작성법", "spec"), ("AI 초안", "ai"), ("점검표", "check")],
    cta_h2="기획 문서, 혼자 쓰기 막막하다면<br><em>실무 기획 클래스</em>에서",
    cta_p="실제 서비스를 주제로 기획서와 기능명세서를 끝까지 써 보는 그린 AI Lab 서비스 기획 클래스예요.",
)

BODY = r'''
  <section class="block" id="kind">
    <p class="label">WHICH DOCUMENT</p>
    <h2>어떤 문서를 <em>언제</em> 쓸까</h2>
    <div class="tbl-wrap"><table class="tbl">
      <tr><th>문서</th><th>답하는 질문</th><th>주로 읽는 사람</th></tr>
      <tr><td>서비스 기획서</td><td>왜, 누구를 위해, 무엇을 만드나</td><td>팀 전체, 의사결정자</td></tr>
      <tr><td>기능명세서</td><td>기능이 정확히 어떻게 동작하나</td><td>개발자, QA</td></tr>
      <tr><td>화면설계서(SB)</td><td>화면에 무엇이 어디에 있나</td><td>디자이너, 개발자</td></tr>
      <tr><td>정책서</td><td>예외·규칙은 어떻게 처리하나</td><td>개발자, 운영</td></tr>
    </table></div>
    <div class="note"><b>작은 팀이라면</b> 기획서 1장 + 기능명세서 엑셀 1개로 시작해도 충분해요. 화면설계서는 피그마 화면 옆에 설명을 붙이는 것으로 대신할 수 있어요.</div>
  </section>

  <section class="block" id="download">
    <p class="label">DOWNLOAD</p>
    <h2>템플릿 <em>다운로드</em></h2>
    <div class="dl">
      <a href="/files/service-plan-template.docx" download data-dl="기획서"><span class="fi docx">DOC</span><div><b>서비스 기획서 템플릿</b><span>워드 · 10개 목차 · 작성 안내 문장 포함</span></div><em>받기 ↓</em></a>
      <a href="/files/feature-spec-template.xlsx" download data-dl="기능명세서"><span class="fi xlsx">XLS</span><div><b>기능명세서 템플릿</b><span>엑셀 · 기능명세서 · 화면목록 · 진행현황 자동 계산</span></div><em>받기 ↓</em></a>
    </div>
    <div class="note gray">구글 드라이브에 올리면 구글 문서·스프레드시트로도 열 수 있어요. 엑셀 템플릿에는 '자료실 구독 서비스'를 예로 든 작성 예시 4줄이 들어 있어요.</div>
  </section>

  <section class="block" id="guide">
    <p class="label">HOW TO WRITE · 기획서</p>
    <h2>기획서 목차별 <em>작성 포인트</em></h2>
    <details class="acc" open><summary><div>1~2. 개요 · 문제 정의<small>가장 중요한 앞 1페이지</small></div></summary><div class="acc-body">
      <p>"이 서비스는 [누구]가 [상황]에서 겪는 [불편]을 [방법]으로 해결한다" 한 문장을 먼저 쓰세요. 이 문장이 안 써지면 아직 기획이 덜 된 거예요. 문제에는 반드시 <b>근거</b>(인터뷰, 리뷰, 데이터)를 붙여요.</p></div></details>
    <details class="acc"><summary><div>3. 목표와 성공 지표<small>숫자로, 기간과 함께</small></div></summary><div class="acc-body">
      <p>"사용자 만족도 향상"은 지표가 아니에요. "출시 4주 안에 가입자의 30%가 2회 이상 사용"처럼 <b>측정 방법·목표치·기간</b>을 같이 적어요.</p></div></details>
    <details class="acc"><summary><div>5. 핵심 기능과 출시 범위<small>Won't가 있어야 범위가 지켜져요</small></div></summary><div class="acc-body">
      <p>Must는 "이게 없으면 서비스가 성립하지 않는 것"만. 이번에 <b>하지 않을 것(Won't)</b>을 명시하면 일정 중간에 기능이 불어나는 걸 막을 수 있어요.</p></div></details>
    <details class="acc"><summary><div>6~7. 유저 플로우 · 화면 목록<small>예외 흐름까지</small></div></summary><div class="acc-body">
      <p>정상 흐름만 쓰면 개발 중에 질문이 쏟아져요. 단계마다 "값이 비어 있으면?", "실패하면?"을 한 칸씩 채워 두세요. 화면 ID(S-01…)는 모든 문서에서 같은 번호를 써요.</p></div></details>
    <details class="acc"><summary><div>8~10. 정책 · 일정 · 리스크<small>모르는 건 모른다고 적기</small></div></summary><div class="acc-body">
      <p>정책은 "최대 20자", "7일 보관"처럼 숫자로. 아직 못 정한 건 리스크·질문 칸에 <b>누구에게, 언제까지</b> 확인할지와 함께 적어 두면 문서가 살아 있어요.</p></div></details>
  </section>

  <section class="block" id="spec">
    <p class="label">HOW TO WRITE · 기능명세서</p>
    <h2>한 줄에 기능 하나, <em>이렇게</em> 써요</h2>
    <div class="tbl-wrap"><table class="tbl">
      <tr><th>칸</th><th>쓰는 법</th><th>예시</th></tr>
      <tr><td>기능명</td><td>동사로 끝나는 짧은 이름</td><td>이메일 구독 신청</td></tr>
      <tr><td>사용자 행동</td><td>사용자가 하는 순서</td><td>이메일 입력 → 동의 체크 → 버튼 클릭</td></tr>
      <tr><td>시스템 동작</td><td>누르면 → 무엇이 → 어떻게</td><td>입력값 확인 후 전송 → 완료 창 → 1.5초 뒤 자료실 이동</td></tr>
      <tr><td>예외·오류</td><td>빈 값, 잘못된 값, 실패</td><td>형식 오류 시 입력칸 아래 안내, 전송 실패 시 입력값 유지</td></tr>
      <tr><td>정책</td><td>숫자로 정한 규칙</td><td>이름은 선택, 동의는 필수</td></tr>
      <tr><td>우선순위·상태</td><td>목록에서 선택</td><td>Must · 확정</td></tr>
    </table></div>
  </section>

  <section class="block" id="ai">
    <p class="label">WITH AI</p>
    <h2>AI로 <em>초안 빠르게</em> 쓰기</h2>
    <div class="pgrid">
      <div class="prompt"><div class="ptitle">기획서 초안</div><button class="copy" type="button">복사</button>
<pre>[서비스 아이디어]의 서비스 기획서 초안을 써 줘.
목차: 1 개요 2 문제 정의 3 목표와 성공 지표 4 타깃 사용자 5 핵심 기능과 출시 범위(Must/Should/Won't 표) 6 유저 플로우(표) 7 화면 목록 8 정책과 예외 9 일정 10 리스크와 확인할 질문
- 내가 준 정보에 없는 건 지어내지 말고 [확인 필요]로 표시해 줘
- 내가 아는 정보: [타깃, 문제, 근거, 기간 등]</pre></div>
      <div class="prompt"><div class="ptitle">기능명세 표로 바꾸기</div><button class="copy" type="button">복사</button>
<pre>아래 기능 설명을 기능명세서 표로 바꿔 줘.
열: 기능명 | 사용자 행동 | 시스템 동작 | 예외·오류 처리 | 정책 | 우선순위
예외·오류 칸은 빈 값, 잘못된 값, 네트워크 실패를 빠짐없이 생각해서 채워 줘.
엑셀에 붙여넣기 좋게 탭으로 구분해 줘.
[기능 설명]</pre></div>
      <div class="prompt"><div class="ptitle">개발자 입장에서 검토</div><button class="copy" type="button">복사</button>
<pre>너는 10년 차 개발자야. 아래 기획 문서를 읽고 개발 시작 전에 물어볼 질문을 모두 뽑아 줘.
정책이 비어 있는 곳, 예외 처리가 없는 곳, 서로 모순되는 곳을 구분해서 표로.
[기획 문서 붙여넣기]</pre></div>
    </div>
  </section>

  <section class="block" id="check">
    <p class="label">CHECKLIST</p>
    <h2>리뷰 전 <em>점검표</em></h2>
    <div data-checklist="planning">
      <div class="progress"><div class="progress-top">점검 진행<span data-num>0 / 0</span></div><div class="bar"><i></i></div><button class="reset" type="button">처음부터 다시</button></div>
      <ul class="checks">
        <li><label><input type="checkbox" id="pl1"><div class="t"><b>서비스 한 줄 정의가 있다</b></div></label></li>
        <li><label><input type="checkbox" id="pl2"><div class="t"><b>문제에 근거(인터뷰·데이터)가 붙어 있다</b></div></label></li>
        <li><label><input type="checkbox" id="pl3"><div class="t"><b>성공 지표에 목표치와 기간이 있다</b></div></label></li>
        <li><label><input type="checkbox" id="pl4"><div class="t"><b>이번에 하지 않을 것(Won't)이 적혀 있다</b></div></label></li>
        <li><label><input type="checkbox" id="pl5"><div class="t"><b>모든 기능에 예외·오류 처리가 있다</b></div></label></li>
        <li><label><input type="checkbox" id="pl6"><div class="t"><b>정책이 숫자로 정해져 있다</b></div></label></li>
        <li><label><input type="checkbox" id="pl7"><div class="t"><b>화면 ID가 모든 문서에서 같다</b></div></label></li>
        <li><label><input type="checkbox" id="pl8"><div class="t"><b>못 정한 것에 담당자와 기한이 있다</b></div></label></li>
      </ul>
    </div>
  </section>
'''

SCRIPT = r'''<script>
document.addEventListener('DOMContentLoaded', function(){
  document.querySelectorAll('[data-dl]').forEach(function(a){ a.addEventListener('click', function(){ GAL.track('다운로드', { file: a.dataset.dl }); }); });
});
</script>
'''
