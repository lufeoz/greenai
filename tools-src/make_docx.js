const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType, HeadingLevel, LevelFormat, BorderStyle, Footer, PageNumber } = require('docx');

const FONT = 'Malgun Gothic';
const W = 9026; // A4 content width (11906 - 2*1440)
const gray = (t) => new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: t, color: '8A8A8A', size: 19, italics: true, font: FONT })] });
const p = (t, o = {}) => new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: t, size: 21, font: FONT, ...o })] });
const blank = (label) => new Paragraph({ numbering: { reference: 'b', level: 0 }, spacing: { after: 60 }, children: [new TextRun({ text: label, size: 21, font: FONT, color: '3E9A58' })] });
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });

const border = { style: BorderStyle.SINGLE, size: 4, color: 'D9D9D9' };
const borders = { top: border, bottom: border, left: border, right: border };
function table(head, rows, widths) {
  const mk = (t, h) => new TableCell({
    width: { size: 0, type: WidthType.DXA }, borders,
    shading: h ? { type: ShadingType.CLEAR, fill: '111111', color: 'auto' } : undefined,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({ children: [new TextRun({ text: t, size: 19, font: FONT, bold: !!h, color: h ? 'FFFFFF' : (t.startsWith('[') ? '3E9A58' : '333333') })] })],
  });
  const fix = (cells) => cells.map((c, i) => { c.options = c.options; return c; });
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: [head, ...rows].map((r, ri) => new TableRow({ tableHeader: ri === 0, children: r.map((t, ci) => {
      const c = new TableCell({
        width: { size: widths[ci], type: WidthType.DXA }, borders,
        shading: ri === 0 ? { type: ShadingType.CLEAR, fill: '111111', color: 'auto' } : (ci === 0 ? { type: ShadingType.CLEAR, fill: 'F6F6F4', color: 'auto' } : undefined),
        margins: { top: 80, bottom: 80, left: 100, right: 100 },
        children: [new Paragraph({ children: [new TextRun({ text: t, size: 19, font: FONT, bold: ri === 0 || ci === 0, color: ri === 0 ? 'FFFFFF' : (t.startsWith('[') ? '3E9A58' : '333333') })] })],
      }); return c; }) })),
  });
}
const sp = () => new Paragraph({ spacing: { after: 120 }, children: [] });

const sections = [
  ['1. 개요', '이 서비스가 무엇인지 처음 보는 사람도 한 문단으로 이해하게 써요.', ['[서비스 한 줄 정의: 누구를 위한, 무엇을 해주는 서비스]', '[만들게 된 배경 2~3문장]']],
  ['2. 문제 정의', '“누가, 어떤 상황에서, 무엇 때문에 불편한가”를 근거와 함께 적어요.', ['[핵심 사용자]', '[불편을 겪는 상황]', '[불편의 원인]', '[근거: 인터뷰·데이터·리뷰 등]']],
  ['3. 목표와 성공 지표', '출시 후 무엇이 달라지면 성공인지 숫자로 정해요.', ['[목표 한 줄]', '[핵심 지표 1개 + 목표치 + 측정 기간]', '[보조 지표 2~3개]']],
  ['4. 타깃 사용자', '핵심 사용자 1~2명을 구체적으로 그려요.', ['[이름·나이·직업·상황]', '[목표와 불편]', '[지금 쓰는 대안]']],
];
const children = [
  new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('서비스 기획서')] }),
  gray('초록색 [대괄호]와 회색 안내 문장은 작성 후 지워 주세요. — 그린 AI Lab 템플릿'),
  sp(),
  table(['항목', '내용'], [['서비스명', '[서비스 이름]'], ['작성자', '[이름 · 역할]'], ['버전', 'v0.1'], ['작성일', '[YYYY.MM.DD]'], ['상태', '작성 중 / 검토 중 / 확정']], [2200, W - 2200]),
  sp(),
  new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun('변경 이력')] }),
  table(['버전', '날짜', '변경 내용', '작성자'], [['v0.1', '[날짜]', '최초 작성', '[이름]'], ['', '', '', '']], [1200, 1800, W - 1200 - 1800 - 1600, 1600]),
];
for (const [t, g, items] of sections) { children.push(h1(t), gray(g), ...items.map(blank)); }
children.push(h1('5. 핵심 기능과 출시 범위'), gray('첫 출시(MVP)에 꼭 필요한 것만 Must에 넣어요. 자세한 동작은 기능명세서(엑셀)에 적어요.'),
  table(['구분', '기능', '이유'], [['Must', '[기능]', '[없으면 서비스가 성립하지 않는 이유]'], ['Must', '[기능]', '[이유]'], ['Should', '[기능]', '[이유]'], ["Won't", '[이번엔 하지 않는 기능]', '[미루는 이유]']], [1500, 3200, W - 4700]));
children.push(h1('6. 유저 플로우'), gray('사용자가 목표를 이루기까지의 단계를 순서대로 적어요. 예외 흐름도 함께.'),
  table(['단계', '사용자 행동', '시스템 반응', '예외'], [['1', '[행동]', '[반응]', '[오류·빈 값]'], ['2', '[행동]', '[반응]', '[예외]'], ['3', '[행동]', '[반응]', '[예외]']], [800, 2742, 2742, W - 800 - 2742 - 2742]));
children.push(h1('7. 화면 목록'), gray('화면 ID는 기능명세서·화면설계서와 같은 번호를 써요.'),
  table(['화면 ID', '화면명', '설명'], [['S-01', '[화면명]', '[이 화면에서 하는 일]'], ['S-02', '[화면명]', '[설명]'], ['S-03', '[화면명]', '[설명]']], [1500, 2500, W - 4000]));
children.push(h1('8. 정책과 예외'), gray('개발자가 “이럴 땐 어떻게 해요?”라고 물을 만한 것을 미리 정해요.'),
  ...['[회원·권한 정책]', '[입력값 규칙: 글자 수, 형식]', '[오류·실패 시 처리]', '[개인정보·보관 기간]'].map(blank));
children.push(h1('9. 일정과 담당'),
  table(['단계', '기간', '담당', '산출물'], [['기획', '[기간]', '[이름]', '기획서 · 기능명세서'], ['디자인', '[기간]', '[이름]', '화면 디자인'], ['개발', '[기간]', '[이름]', '구현'], ['QA · 출시', '[기간]', '[이름]', '테스트 결과']], [1800, 2200, 2000, W - 6000]));
children.push(h1('10. 리스크와 확인할 질문'), gray('아직 정하지 못한 것, 막힐 수 있는 것을 숨기지 말고 적어요.'),
  ...['[리스크 1과 대응 방안]', '[확인이 필요한 질문 — 누구에게, 언제까지]'].map(blank));

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: FONT, size: 44, bold: true, color: '111111' }, paragraph: { spacing: { before: 0, after: 120 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 28, bold: true, color: '111111' }, paragraph: { spacing: { before: 360, after: 100 }, keepNext: true, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: '6CC284', space: 4 } } } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 23, bold: true, color: '3E9A58' }, paragraph: { spacing: { before: 200, after: 80 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [{ reference: 'b', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 260 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: '그린 AI Lab · 서비스 기획서 템플릿 · ', size: 16, color: '8A8A8A', font: FONT }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '8A8A8A' })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(b => fs.writeFileSync('service-plan-template.docx', b));
