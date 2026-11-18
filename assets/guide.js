/* 그린 AI Lab — 자료 상세 페이지 공통 스크립트
   ─────────────────────────────────────────────
   여기 두 줄만 바꾸면 모든 자료 페이지에 적용돼요. */
var GAL = {
  CLASS_URL: '/class', // 클래스 신청 페이지
  KEY: 'green'         // 환영 메일 링크 /archive?k=green 의 green 과 같아야 해요
};

/* 1. 구독자만 보기 — <head> 에서 바로 실행 */
(function(){
  try{
    var q = new URLSearchParams(location.search);
    if (q.get('k') === GAL.KEY) { localStorage.setItem('gal_sub','1'); history.replaceState(null,'',location.pathname + location.hash); }
    if (!localStorage.getItem('gal_sub')) location.replace('/?from=archive');
  }catch(e){}
})();

/* 2. 방문 통계 */
window.va = window.va || function(){ (window.vaq = window.vaq || []).push(arguments); };
GAL.track = function(name, data){ try{ window.va('event', { name:name, data:data || {} }); }catch(e){} };
GAL.page = location.pathname.split('/').pop() || 'guide';

document.addEventListener('DOMContentLoaded', function(){
  var $$ = function(s, r){ return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* 토스트 */
  var toast = document.createElement('div'); toast.className = 'toast'; document.body.appendChild(toast);
  var tt; GAL.toast = function(msg){ toast.textContent = msg; toast.classList.add('show'); clearTimeout(tt); tt = setTimeout(function(){ toast.classList.remove('show'); }, 1500); };

  /* 클래스 링크 */
  $$('[data-class]').forEach(function(a){
    a.href = GAL.CLASS_URL;
    a.addEventListener('click', function(){ GAL.track('클래스 클릭', { from: GAL.page }); });
  });

  /* 복사 */
  function copyText(text){
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    var ta = document.createElement('textarea'); ta.value = text; ta.style.position='fixed'; ta.style.opacity='0';
    document.body.appendChild(ta); ta.select(); try{ document.execCommand('copy'); }catch(e){} document.body.removeChild(ta);
    return Promise.resolve();
  }
  GAL.copy = copyText;
  document.addEventListener('click', function(e){
    var btn = e.target.closest('.copy'); if (!btn) return;
    var src = btn.dataset.target ? document.getElementById(btn.dataset.target) : btn.parentElement.querySelector('pre');
    var text = typeof src.value === 'string' ? src.value : src.innerText;
    copyText(text.trim()).then(function(){
      var old = btn.textContent; btn.textContent = '복사됨'; btn.classList.add('ok'); GAL.toast('복사했어요');
      setTimeout(function(){ btn.textContent = old; btn.classList.remove('ok'); }, 1400);
    });
    GAL.track('복사', { page: GAL.page });
  });

  /* 검색 + 칩 필터: <input data-search="목록id">, <div class="chips" data-filter="목록id">, 항목에 data-tags, data-text */
  $$('[data-search],[data-filter]').forEach(function(){});
  function applyFilter(listId){
    var list = document.getElementById(listId); if (!list) return;
    var input = document.querySelector('[data-search="'+listId+'"]');
    var chipOn = document.querySelector('[data-filter="'+listId+'"] .chip.on');
    var q = input ? input.value.trim().toLowerCase() : '';
    var tag = chipOn ? chipOn.dataset.v : 'all';
    var shown = 0;
    $$('[data-item]', list).forEach(function(el){
      var ok = (tag === 'all' || (' '+el.dataset.tags+' ').indexOf(' '+tag+' ') >= 0)
            && (!q || el.innerText.toLowerCase().indexOf(q) >= 0);
      el.style.display = ok ? '' : 'none'; if (ok) shown++;
    });
    var em = document.querySelector('[data-empty="'+listId+'"]'); if (em) em.style.display = shown ? 'none' : 'block';
    var cm = document.querySelector('[data-count="'+listId+'"]'); if (cm) cm.textContent = shown + '개';
  }
  $$('[data-search]').forEach(function(inp){ inp.addEventListener('input', function(){ applyFilter(inp.dataset.search); }); });
  $$('[data-filter]').forEach(function(box){
    box.addEventListener('click', function(e){
      var c = e.target.closest('.chip'); if (!c) return;
      $$('.chip', box).forEach(function(x){ x.classList.toggle('on', x === c); });
      applyFilter(box.dataset.filter);
    });
    applyFilter(box.dataset.filter);
  });

  /* 체크리스트 — 진행 상황을 이 브라우저에 저장 */
  $$('[data-checklist]').forEach(function(wrap){
    var key = 'gal_chk_' + wrap.dataset.checklist;
    var saved = {}; try{ saved = JSON.parse(localStorage.getItem(key) || '{}'); }catch(e){}
    var boxes = $$('.checks input[type=checkbox]', wrap);
    var bar = wrap.querySelector('.bar i'), num = wrap.querySelector('[data-num]');
    function update(){
      var done = 0;
      boxes.forEach(function(b){ b.closest('li').classList.toggle('done', b.checked); if (b.checked) done++; saved[b.id] = b.checked; });
      try{ localStorage.setItem(key, JSON.stringify(saved)); }catch(e){}
      if (bar) bar.style.width = (boxes.length ? done / boxes.length * 100 : 0) + '%';
      if (num) num.textContent = done + ' / ' + boxes.length;
    }
    boxes.forEach(function(b){ if (saved[b.id]) b.checked = true; b.addEventListener('change', update); });
    var rs = wrap.querySelector('.reset'); if (rs) rs.addEventListener('click', function(){ boxes.forEach(function(b){ b.checked = false; }); update(); });
    update();
  });

  /* 입력칸 자동 저장: <textarea data-save="키"> */
  $$('[data-save]').forEach(function(el){
    var key = 'gal_f_' + el.dataset.save;
    try{ if (localStorage.getItem(key)) el.value = localStorage.getItem(key); }catch(e){}
    el.addEventListener('input', function(){ try{ localStorage.setItem(key, el.value); }catch(e){} });
  });
});
