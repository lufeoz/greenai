/* 그린 AI Lab — 7개 영역 공통 렌더러 (공개 페이지, 구독 확인 없음)
   페이지마다 window.LAB = { items:[...], facets:[{key,label,values:{값:'이름'}}], cardMeta:fn } 를 두고 이 파일을 불러요.
   항목 필드: t 제목 · d 한 줄 설명 · tags[] · what · use[] · how[] · tools[] · price · url(공식/관련 링크) · urlLabel
             prompt(복사 가능) · ex(활용 예시) · src 출처 · lic 라이선스 · upd 업데이트 · rel[[이름,링크]] 관련 콘텐츠 · level */
window.va = window.va || function(){ (window.vaq = window.vaq || []).push(arguments); };
(function(){
  var NAV = [['AI DIRECTORY','/directory'],['SKILLS','/skills'],['PROMPTS','/prompts'],['WORKFLOW','/workflows'],['TOOLS','/tools'],['LEARNING','/learn'],['ARCHIVE','/archive']];
  function esc(s){ return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
  function track(n, d){ try{ window.va('event', { name:n, data:d||{} }); }catch(e){} }
  window.GALAB = { esc: esc, track: track };

  document.addEventListener('DOMContentLoaded', function(){
    /* 상단 7개 메뉴 */
    var here = location.pathname.replace(/\.html$/,'').replace(/\/$/,'');
    var nav = document.getElementById('labnav');
    if (nav) nav.innerHTML = NAV.map(function(n){ return '<a href="'+n[1]+'"'+(here === n[1] ? ' class="on"' : '')+'>'+n[0]+'</a>'; }).join('');

    /* 토스트 · 복사 */
    var toast = document.createElement('div'); toast.className = 'toast'; document.body.appendChild(toast); var tt;
    function say(m){ toast.textContent = m; toast.classList.add('show'); clearTimeout(tt); tt = setTimeout(function(){ toast.classList.remove('show'); }, 1500); }
    function copy(text){
      if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
      var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select();
      try{ document.execCommand('copy'); }catch(e){} document.body.removeChild(ta); return Promise.resolve();
    }
    window.GALAB.copy = copy; window.GALAB.say = say;
    document.addEventListener('click', function(e){
      var b = e.target.closest('.copy'); if (!b) return;
      var src = b.dataset.target ? document.getElementById(b.dataset.target) : b.parentElement.querySelector('pre');
      copy((src.value != null ? src.value : src.innerText).trim()).then(function(){ var o = b.textContent; b.textContent = '복사됨'; b.classList.add('ok'); say('복사했어요'); setTimeout(function(){ b.textContent = o; b.classList.remove('ok'); }, 1300); });
      track('복사', { page: here });
    });

    var L = window.LAB; if (!L || !L.items) return;
    var list = document.getElementById('lablist'), q = document.getElementById('labq'), empty = document.getElementById('labempty'), cnt = document.getElementById('labcount');
    var sel = {};
    (L.facets || []).forEach(function(f){
      sel[f.key] = 'all';
      var box = document.getElementById('facet-' + f.key); if (!box) return;
      var counts = {}; L.items.forEach(function(it){ [].concat(it[f.key] || []).forEach(function(v){ counts[v] = (counts[v]||0) + 1; }); });
      box.innerHTML = '<button class="chip on" data-v="all">' + esc(f.label) + ' 전체</button>' + Object.keys(f.values).filter(function(v){ return counts[v]; }).map(function(v){ return '<button class="chip" data-v="'+esc(v)+'">'+esc(f.values[v])+' <em>'+counts[v]+'</em></button>'; }).join('');
      box.addEventListener('click', function(e){ var c = e.target.closest('.chip'); if (!c) return; box.querySelectorAll('.chip').forEach(function(x){ x.classList.toggle('on', x === c); }); sel[f.key] = c.dataset.v; render(); });
    });
    function hay(it){ return [it.t, it.d, it.what, (it.tags||[]).join(' '), (it.tools||[]).join(' '), (it.use||[]).join(' '), it.prompt, it.alias].join(' ').toLowerCase(); }
    function label(f, v){ var fc = (L.facets||[]).filter(function(x){ return x.key === f; })[0]; return fc ? (fc.values[v] || v) : v; }
    function render(){
      var kw = q ? q.value.trim().toLowerCase().split(/\s+/).filter(Boolean) : [], n = 0;
      list.innerHTML = L.items.map(function(it, i){
        for (var k in sel) if (sel[k] !== 'all' && [].concat(it[k] || []).indexOf(sel[k]) < 0) return '';
        var h = hay(it); if (kw.some(function(w){ return h.indexOf(w) < 0; })) return '';
        n++;
        var f0 = (L.facets||[])[0];
        return '<div class="lcard" role="button" tabindex="0" data-i="'+i+'">'
          + '<div class="lc-top">' + (f0 ? '<span class="lc-k">'+esc(label(f0.key, [].concat(it[f0.key])[0]))+'</span>' : '')
          + (it.price ? '<span class="lc-p">'+esc(it.price)+'</span>' : '') + (it.level ? '<span class="lc-l lv-'+esc(it.level)+'">'+esc(it.level)+'</span>' : '') + '</div>'
          + '<h3>'+esc(it.t)+'</h3><p>'+esc(it.d)+'</p>'
          + (it.prompt && L.inlinePrompt ? '<pre class="lc-pre">'+esc(it.prompt)+'</pre>' : '')
          + (it.tools ? '<div class="lc-tools">'+it.tools.slice(0,3).map(function(t){ return '<span>'+esc(t)+'</span>'; }).join('')+'</div>' : '')
          + '<span class="lc-go">자세히 →</span></div>';
      }).join('');
      if (cnt) cnt.textContent = n + '개';
      if (empty) empty.style.display = n ? 'none' : 'block';
    }
    if (q){ var qt; q.addEventListener('input', function(){ render(); clearTimeout(qt); qt = setTimeout(function(){ if (q.value.trim()) track('검색', { page: here, q: q.value.trim() }); }, 1200); }); }

    /* 상세 시트 */
    var sheet = document.getElementById('labsheet'), inner = document.getElementById('labsheetin');
    function sec(t, body){ return body ? '<div class="dt-sec"><h4>'+t+'</h4>'+body+'</div>' : ''; }
    function ul(a, o){ return a && a.length ? '<'+(o?'ol':'ul')+'>'+a.map(function(x){ return '<li>'+esc(x)+'</li>'; }).join('')+'</'+(o?'ol':'ul')+'>' : ''; }
    function detail(i){
      var it = L.items[i]; if (!it) return;
      var meta = (L.facets||[]).map(function(f){ return [].concat(it[f.key]||[]).map(function(v){ return '<span>'+esc(label(f.key, v))+'</span>'; }).join(''); }).join('')
        + (it.price && !(L.facets||[]).some(function(f){ return [].concat(it[f.key]||[]).some(function(v){ return label(f.key, v) === it.price; }); }) ? '<span class="pp">'+esc(it.price)+'</span>' : '') + (it.level && !(L.facets||[]).some(function(f){ return f.key === 'level'; }) ? '<span>'+esc(it.level)+'</span>' : '');
      inner.innerHTML = '<div class="dt"><div class="dt-meta">'+meta+'</div><h3>'+esc(it.t)+'</h3><p class="dt-d">'+esc(it.d)+'</p>'
        + sec(L.whatLabel || '무엇인가요?', it.what ? '<p>'+esc(it.what)+'</p>' : '')
        + sec(L.useLabel || '이럴 때 써요', ul(it.use))
        + (it.prompt ? '<div class="dt-sec"><h4>프롬프트</h4><div class="prompt" style="margin-top:6px"><button class="copy" type="button">복사</button><pre>'+esc(it.prompt)+'</pre></div></div>' : '')
        + sec('활용 예시', it.ex ? '<p>'+esc(it.ex)+'</p>' : '')
        + sec(L.howLabel || '이렇게 해요', ul(it.how, true))
        + (it.code ? '<div class="dt-sec"><h4>설치 · 실행</h4><div class="prompt" style="margin-top:6px"><button class="copy" type="button">복사</button><pre>'+esc(it.code)+'</pre></div></div>' : '')
        + sec(L.toolsLabel || '연결 도구', it.tools ? '<div class="dt-tools">'+it.tools.map(function(t){ return '<span>'+esc(t)+'</span>'; }).join('')+'</div>' : '')
        + sec('관련 콘텐츠', it.rel ? '<div class="dt-rel">'+it.rel.map(function(r){ return '<a href="'+esc(r[1])+'">'+esc(r[0])+' →</a>'; }).join('')+'</div>' : '')
        + '<div class="dt-trust">' + (it.src ? '<b>출처</b> '+esc(it.src)+'<br>' : '') + (it.lic ? '<b>라이선스</b> '+esc(it.lic)+'<br>' : '') + '<b>업데이트</b> '+esc(it.upd || L.upd || '2026.11.18') + (L.note ? '<br>'+esc(L.note) : '') + '</div>'
        + (it.url ? '<div class="dt-btns"><a class="p1" href="'+esc(it.url)+'"'+(/^https?:/.test(it.url)?' target="_blank" rel="noopener"':'')+'>'+esc(it.urlLabel || '바로가기')+' →</a></div>' : '')
        + '</div>';
      sheet.classList.add('show'); inner.parentElement.scrollTop = 0; track('상세 보기', { page: here, title: it.t });
    }
    list.addEventListener('click', function(e){ var c = e.target.closest('[data-i]'); if (c) detail(+c.dataset.i); });
    list.addEventListener('keydown', function(e){ var c = e.target.closest('[data-i]'); if (c && (e.key === 'Enter' || e.key === ' ')){ e.preventDefault(); detail(+c.dataset.i); } });
    sheet.addEventListener('click', function(e){ if (e.target.closest('[data-close]')) sheet.classList.remove('show'); });
    var h = decodeURIComponent(location.hash.slice(1)); if (h && q){ q.value = h; }
    render();
  });
})();
