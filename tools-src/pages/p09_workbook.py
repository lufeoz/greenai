STEPS = [
 ("problem", "문제", "누가, 어떤 상황에서, 무엇이 불편한가", [
   ("who", "누가 불편한가요?", "최대한 좁게 — '직장인'보다 '야근이 잦은 3년 차 디자이너'"),
   ("when", "어떤 상황에서 불편한가요?", "언제, 어디서, 무엇을 하다가"),
   ("pain", "무엇이 불편한가요?", "그 사람이 실제로 쓸 법한 말로"),
 ], "내 앱 아이디어의 문제 정의를 검토해 줘.\n- 누가: {who}\n- 상황: {when}\n- 불편: {pain}\n대상이 너무 넓은지, 불편이 진짜 문제인지 아니면 '있으면 좋은 것'인지 판단하고, 더 날카로운 문제 정의 문장 3개를 제안해 줘."),
 ("alt", "지금의 해결 방법", "사람들은 지금 이 문제를 어떻게 버티고 있나", [
   ("now", "지금은 어떻게 해결하고 있나요?", "다른 앱, 엑셀, 메모, 지인에게 부탁, 그냥 참기 등"),
   ("gap", "그 방법의 아쉬운 점은?", "비싸다, 번거롭다, 시간이 걸린다…"),
 ], "아래 문제를 사람들이 지금 어떻게 해결하는지 대안 5가지를 찾아 줘(기존 서비스 포함). 각 대안의 아쉬운 점과, 내 아이디어가 파고들 틈을 정리해 줘. 확실하지 않은 서비스 정보는 확실하지 않다고 표시해 줘.\n- 문제: {who} / {when} / {pain}\n- 내가 아는 대안: {now}\n- 아쉬운 점: {gap}"),
 ("idea", "해결 아이디어", "한 문장으로 말할 수 있어야 해요", [
   ("oneline", "내 서비스를 한 문장으로", "[누구]가 [무엇]을 [어떻게] 할 수 있게 해 주는 서비스"),
   ("why", "왜 기존 방법보다 나은가요?", "더 빠르다 · 더 싸다 · 더 쉽다 중 무엇이, 얼마나"),
 ], "내 서비스 아이디어를 냉정하게 평가해 줘.\n- 한 문장: {oneline}\n- 기존보다 나은 점: {why}\n- 대상 문제: {pain}\n사용자가 '굳이 바꿀 만큼' 나은지, 가장 약한 가정이 무엇인지, 그 가정을 1주일 안에 확인할 방법 3가지를 알려 줘."),
 ("test", "검증 방법", "만들기 전에 확인하기", [
   ("assume", "가장 불확실한 가정은?", "이게 틀리면 아이디어 전체가 무너지는 것"),
   ("method", "어떻게 확인할 건가요?", "인터뷰 5명, 랜딩페이지 신청 받기, 설문, 수작업으로 먼저 해주기 등"),
   ("pass", "어떤 결과면 '된다'고 볼까요?", "미리 숫자로 — 예) 방문자 100명 중 10명 이상 신청"),
 ], "아래 가정을 검증할 사용자 인터뷰 질문 8개를 만들어 줘. 유도 질문은 빼고, 과거의 실제 행동을 묻는 질문 위주로.\n- 대상: {who}\n- 가정: {assume}\n- 검증 방법: {method}\n- 통과 기준: {pass}\n그리고 이 통과 기준이 너무 느슨하거나 빡빡하지 않은지도 봐 줘."),
 ("mvp", "MVP 범위", "가장 작게 만들어 보기", [
   ("must", "꼭 있어야 하는 기능 (최대 3개)", "이게 없으면 핵심 가치가 전달되지 않는 것만"),
   ("wont", "이번엔 안 만들 기능", "로그인, 결제, 알림… 수작업이나 기존 툴로 대신할 수 있는 것"),
 ], "내 MVP 범위를 줄여 줘.\n- 서비스: {oneline}\n- 꼭 필요하다고 생각한 기능: {must}\n- 뺄 기능: {wont}\n이 중 노코드 툴·수작업으로 대신할 수 있는 것을 알려주고, 2주 안에 만들 수 있는 가장 작은 버전을 제안해 줘."),
 ("metric", "성공 기준", "언제, 무엇을 보고 계속할지 정하기", [
   ("kpi", "가장 중요한 숫자 하나", "가입 수보다 '다시 쓴 사람 수'처럼 가치를 보여주는 숫자"),
   ("deadline", "언제까지 확인할 건가요?", "예) 출시 후 4주"),
   ("next", "결과가 안 좋으면?", "방향을 바꿀지, 접을지 미리 정해 두기"),
 ], "내 서비스의 성공 기준을 검토해 줘.\n- 서비스: {oneline}\n- 핵심 지표: {kpi}\n- 확인 기한: {deadline}\n- 안 좋을 때 계획: {next}\n지표가 진짜 가치를 보여주는지, 측정 방법은 무엇인지, 보조 지표 2개를 추천해 줘."),
]

blocks = []
for i, (k, t, sub, fields, prompt) in enumerate(STEPS, 1):
    fs = "".join(f'''
      <div class="field"><label>{lab}<small>{hint}</small></label><textarea data-save="wb_{fk}" data-wb="{fk}" data-label="{lab}"></textarea></div>''' for fk, lab, hint in fields)
    blocks.append(f'''
  <section class="block" id="s-{k}">
    <p class="label">STEP {i}</p>
    <h2>{t} <small style="font-size:14px;font-weight:600;color:var(--gray)">{sub}</small></h2>
    <div class="card">{fs}
      <button class="btn btn-black" type="button" data-ask="{i-1}" style="width:100%;margin-top:14px">내 답을 넣어 AI 질문 복사</button>
    </div>
  </section>''')

import json
PROMPTS = json.dumps([s[4] for s in STEPS], ensure_ascii=False)

META = dict(
    slug="idea-validation-workbook",
    title="AI로 하는 앱 아이디어 검증 워크북",
    desc="문제 정의부터 MVP 범위, 성공 기준까지 6단계로 채우고 AI에게 검토받는 워크북",
    eyebrow="IDEA VALIDATION WORKBOOK",
    h1="만들기 전에 확인하는<br><em>앱 아이디어 검증 워크북</em>",
    intro="6단계 칸을 채우면 단계마다 내 답이 들어간 AI 질문이 만들어져요.<br>다 쓰면 한 장짜리 정리본으로 복사할 수 있어요.",
    buttons=[("워크북 시작하기", "#s-problem"), ("정리본 만들기", "#export")],
    badges=["무료 자료", "6단계", "자동 저장", "AI 검토 프롬프트"],
    toc=[("① 문제", "s-problem"), ("② 대안", "s-alt"), ("③ 아이디어", "s-idea"), ("④ 검증", "s-test"), ("⑤ MVP", "s-mvp"), ("⑥ 성공 기준", "s-metric"), ("정리본", "export")],
    cta_h2="검증한 아이디어를<br><em>실제 서비스 기획</em>으로",
    cta_p="아이디어 검증부터 기획서·화면 설계까지 이어지는 그린 AI Lab 서비스 기획 클래스예요.",
)

BODY = r'''
  <section class="block">
    <p class="label">HOW TO USE</p>
    <h2>이렇게 <em>쓰면 돼요</em></h2>
    <div class="card"><ol>
      <li><b>칸을 채워요.</b> 짧아도 괜찮아요. 쓴 내용은 이 브라우저에 자동 저장돼요.</li>
      <li><b>단계마다 "AI 질문 복사"</b>를 눌러 ChatGPT·Claude에 붙여넣어요. 내 답이 들어간 질문이 복사돼요.</li>
      <li><b>AI 답을 보고 칸을 고쳐요.</b> AI 의견은 참고일 뿐, 결정은 내가 해요.</li>
      <li><b>마지막에 정리본</b>을 만들어 팀원·멘토에게 공유해요.</li>
    </ol></div>
    <div class="note"><b>가장 중요한 한 가지</b> 이 워크북의 답은 책상에서 나오지 않아요. STEP 4에서 실제 사람 5명과 이야기해 본 뒤 다시 돌아와 고쳐 쓰세요.</div>
  </section>
''' + "".join(blocks) + r'''

  <section class="block" id="export">
    <p class="label">EXPORT</p>
    <h2>한 장짜리 <em>정리본</em></h2>
    <button class="btn btn-black" type="button" id="wbBuild" style="width:100%;margin-top:12px">내 답으로 정리본 만들기</button>
    <div class="field"><textarea id="wbOut" style="min-height:240px" readonly placeholder="버튼을 누르면 여기에 정리돼요"></textarea></div>
    <div class="grid2" style="margin-top:8px">
      <button class="btn btn-white" type="button" id="wbCopy">정리본 복사</button>
      <button class="btn btn-white" type="button" id="wbAI">AI 종합 검토로 복사</button>
    </div>
    <button class="reset" type="button" id="wbReset" style="margin-top:14px">모든 칸 지우고 새 아이디어로 시작</button>
  </section>
'''

SCRIPT = "<script>\nvar WB_PROMPTS = " + PROMPTS + r''';
document.addEventListener('DOMContentLoaded', function(){
  function val(k){ var el = document.querySelector('[data-wb="'+k+'"]'); var v = el ? el.value.trim() : ''; return v || '(미작성)'; }
  function fill(t){ return t.replace(/\{(\w+)\}/g, function(_, k){ return val(k); }); }
  document.querySelectorAll('[data-ask]').forEach(function(b){
    b.addEventListener('click', function(){
      GAL.copy(fill(WB_PROMPTS[+b.dataset.ask])).then(function(){ GAL.toast('AI 질문을 복사했어요. ChatGPT·Claude에 붙여넣으세요'); });
      GAL.track('워크북 AI 질문', { step: +b.dataset.ask + 1 });
    });
  });
  var out = document.getElementById('wbOut');
  function build(){
    var lines = ['# 앱 아이디어 검증 정리본', ''];
    document.querySelectorAll('section[id^="s-"]').forEach(function(sec, i){
      lines.push('## ' + (i+1) + '. ' + sec.querySelector('h2').childNodes[0].textContent.trim());
      sec.querySelectorAll('[data-wb]').forEach(function(t){ lines.push('- ' + t.dataset.label + ' ' + (t.value.trim() || '(미작성)')); });
      lines.push('');
    });
    out.value = lines.join('\n'); return out.value;
  }
  document.getElementById('wbBuild').onclick = function(){ build(); GAL.toast('정리본을 만들었어요'); };
  document.getElementById('wbCopy').onclick = function(){ GAL.copy(build()).then(function(){ GAL.toast('정리본을 복사했어요'); }); };
  document.getElementById('wbAI').onclick = function(){
    GAL.copy('아래는 내 앱 아이디어 검증 정리본이야. 투자자이자 경험 많은 PM의 입장에서 검토해 줘.\n1) 가장 위험한 가정 3개\n2) 논리가 이어지지 않는 곳\n3) 다음 2주 동안 할 일 우선순위 5개\n4) 계속할지 방향을 바꿀지에 대한 의견과 그 이유\n\n' + build())
      .then(function(){ GAL.toast('종합 검토 프롬프트를 복사했어요'); });
  };
  document.getElementById('wbReset').onclick = function(){
    if (!confirm('모든 칸을 지울까요?')) return;
    document.querySelectorAll('[data-wb]').forEach(function(t){ t.value = ''; try{ localStorage.removeItem('gal_f_' + t.dataset.save); }catch(e){} });
    out.value = ''; GAL.toast('모두 지웠어요');
  };
});
</script>
'''
