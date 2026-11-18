from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

F = "Arial"
HEAD = PatternFill("solid", fgColor="111111"); EX = PatternFill("solid", fgColor="EAF6EE"); IN = PatternFill("solid", fgColor="FFFFFF")
thin = Side(style="thin", color="D9D9D9"); BD = Border(top=thin, bottom=thin, left=thin, right=thin)
wb = Workbook()

# ── 사용법
ws = wb.active; ws.title = "사용법"
ws.column_dimensions["A"].width = 3; ws.column_dimensions["B"].width = 90
rows = [
 ("기능명세서 템플릿 — 그린 AI Lab", Font(name=F, size=16, bold=True)),
 ("", None),
 ("1. '기능명세서' 시트에 기능을 한 줄에 하나씩 적어요. 연두색 줄은 작성 예시예요(자료실 구독 서비스). 지우고 써도 돼요.", None),
 ("2. 흰 칸이 입력하는 곳이에요. 우선순위·상태는 칸을 누르면 목록에서 고를 수 있어요.", None),
 ("3. '화면목록' 시트의 화면 ID(S-01…)를 기능명세서 '화면 ID' 칸에 같이 적으면 연결이 쉬워요.", None),
 ("4. '진행현황' 시트는 자동으로 계산돼요. 직접 입력할 필요 없어요.", None),
 ("", None),
 ("작성 팁", Font(name=F, size=12, bold=True, color="3E9A58")),
 ("· 시스템 동작은 '누르면 → 무엇이 → 어떻게 된다'처럼 개발자가 그대로 만들 수 있게 적어요.", None),
 ("· 예외·오류 칸이 비어 있으면 아직 덜 쓴 거예요. 빈 값, 잘못된 값, 네트워크 오류를 꼭 생각해 보세요.", None),
 ("· 정책은 숫자로 — '적당히'가 아니라 '최대 20자', '7일 보관'처럼.", None),
]
for i, (t, f) in enumerate(rows, 1):
    c = ws.cell(row=i, column=2, value=t); c.font = f or Font(name=F, size=11); c.alignment = Alignment(wrap_text=True, vertical="top")

# ── 기능명세서
ws = wb.create_sheet("기능명세서")
cols = [("기능 ID",9),("화면 ID",9),("기능명",18),("설명",30),("우선순위",10),("사용자 행동",26),("시스템 동작",34),("예외·오류 처리",34),("정책",26),("상태",10),("담당",10),("비고",20)]
for i,(h,w) in enumerate(cols,1):
    c = ws.cell(row=1, column=i, value=h); c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = HEAD
    c.alignment = Alignment(horizontal="center", vertical="center"); c.border = BD
    ws.column_dimensions[c.column_letter].width = w
ws.row_dimensions[1].height = 24
ex = [
 ("F-01","S-01","이메일 구독 신청","이메일·이름을 입력해 뉴스레터를 구독한다","Must","이메일 입력 → 동의 체크 → [자료실 받기] 클릭","입력값 확인 후 구독 API로 전송 → 완료 창 표시 → 1.5초 뒤 자료실로 이동","이메일 형식 오류: 입력칸 아래 안내 / 동의 미체크: 안내 문구 / 전송 실패: 다시 시도 안내, 입력값 유지","이름은 선택 입력 / 동의는 필수","확정","그린",""),
 ("F-02","S-02","자료실 접근 확인","구독자만 자료실을 볼 수 있게 한다","Must","자료실 주소로 접속","구독 표시가 있으면 자료실 표시, 없으면 신청 페이지로 이동 + 안내 띠","메일 링크(?k=키)로 접속하면 구독 표시를 저장하고 자료실 표시","구독 표시는 브라우저에 저장","확정","그린","다른 기기는 메일 링크로 접속"),
 ("F-03","S-02","자료 필터","종류별로 자료를 걸러 본다","Should","종류 탭 클릭","해당 종류 자료만 표시, 탭에 개수 표시","결과 0개면 '조건에 맞는 자료가 없어요' 표시","탭은 자료 목록에서 자동 생성","개발중","그린",""),
 ("F-04","S-02","자료 추천","질문 2개에 답하면 자료 3개를 추천한다","Could","[나에게 맞는 자료 찾기] → 질문 2개 선택","분야·필요에 맞는 점수로 상위 3개 표시","—","인기 자료는 가산점","검토중","그린",""),
]
r = 2
for row in ex:
    for i,v in enumerate(row,1):
        c = ws.cell(row=r, column=i, value=v); c.font = Font(name=F, size=10); c.fill = EX; c.border = BD
        c.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
for rr in range(r, r+40):
    ws.cell(row=rr, column=1, value=f'=IF(C{rr}="","","F-"&TEXT(ROW()-1,"00"))')
    for i in range(1, len(cols)+1):
        c = ws.cell(row=rr, column=i); c.font = Font(name=F, size=10); c.border = BD; c.alignment = Alignment(wrap_text=True, vertical="top")
LAST = r+39
dv1 = DataValidation(type="list", formula1='"Must,Should,Could,Won\'t"', allow_blank=True); ws.add_data_validation(dv1); dv1.add(f"E2:E{LAST}")
dv2 = DataValidation(type="list", formula1='"작성중,검토중,확정,개발중,완료,보류"', allow_blank=True); ws.add_data_validation(dv2); dv2.add(f"J2:J{LAST}")
ws.conditional_formatting.add(f"E2:E{LAST}", CellIsRule(operator="equal", formula=['"Must"'], font=Font(name=F, bold=True, color="C0392B")))
ws.conditional_formatting.add(f"J2:J{LAST}", CellIsRule(operator="equal", formula=['"완료"'], fill=PatternFill("solid", fgColor="D9F0E0")))
ws.freeze_panes = "D2"; ws.auto_filter.ref = f"A1:L{LAST}"

# ── 화면목록
ws2 = wb.create_sheet("화면목록")
c2 = [("화면 ID",10),("화면명",18),("주소·경로",22),("설명",40),("관련 기능 ID",16),("상태",10)]
for i,(h,w) in enumerate(c2,1):
    c = ws2.cell(row=1, column=i, value=h); c.font = Font(name=F, bold=True, color="FFFFFF"); c.fill = HEAD; c.border = BD
    c.alignment = Alignment(horizontal="center"); ws2.column_dimensions[c.column_letter].width = w
ex2 = [("S-01","구독 신청","/","자료실 소개와 구독 신청 폼","F-01","확정"),("S-02","자료실","/archive","자료 목록, 필터, 추천","F-02, F-03, F-04","개발중"),("S-03","자료 상세","/guides/…","자료별 가이드 페이지","—","작성중")]
for ri,row in enumerate(ex2,2):
    for i,v in enumerate(row,1):
        c = ws2.cell(row=ri, column=i, value=v); c.font = Font(name=F, size=10); c.fill = EX; c.border = BD
for rr in range(5, 35):
    for i in range(1,7):
        c = ws2.cell(row=rr, column=i); c.font = Font(name=F, size=10); c.border = BD
dv3 = DataValidation(type="list", formula1='"작성중,검토중,확정,개발중,완료,보류"', allow_blank=True); ws2.add_data_validation(dv3); dv3.add("F2:F34")
ws2.freeze_panes = "A2"

# ── 진행현황
ws3 = wb.create_sheet("진행현황")
ws3.column_dimensions["A"].width = 16; ws3.column_dimensions["B"].width = 12; ws3.column_dimensions["C"].width = 12
ws3["A1"] = "진행현황 (자동 계산)"; ws3["A1"].font = Font(name=F, size=14, bold=True)
ws3["A3"], ws3["B3"], ws3["C3"] = "상태", "기능 수", "비율"
for c in ("A3","B3","C3"): ws3[c].font = Font(name=F, bold=True, color="FFFFFF"); ws3[c].fill = HEAD
states = ["작성중","검토중","확정","개발중","완료","보류"]
for i,s in enumerate(states, 4):
    ws3[f"A{i}"] = s; ws3[f"B{i}"] = f'=COUNTIF(기능명세서!$J$2:$J${LAST},A{i})'
    ws3[f"C{i}"] = f'=IF($B$10=0,0,B{i}/$B$10)'; ws3[f"C{i}"].number_format = "0%"
ws3["A10"] = "합계"; ws3["B10"] = "=SUM(B4:B9)"; ws3["A10"].font = ws3["B10"].font = Font(name=F, bold=True)
ws3["A12"], ws3["B12"] = "우선순위", "기능 수"
for c in ("A12","B12"): ws3[c].font = Font(name=F, bold=True, color="FFFFFF"); ws3[c].fill = HEAD
for i,s in enumerate(["Must","Should","Could","Won't"], 13):
    ws3[f"A{i}"] = s; ws3[f"B{i}"] = f'=COUNTIF(기능명세서!$E$2:$E${LAST},A{i})'
ws3["A18"] = "완료율"; ws3["B18"] = '=IF(B10=0,0,B8/B10)'; ws3["B18"].number_format = "0%"
ws3["A18"].font = ws3["B18"].font = Font(name=F, bold=True, color="3E9A58")
for row in ws3.iter_rows(min_row=4, max_row=18):
    for c in row:
        if c.font is None or not c.font.bold: c.font = Font(name=F, size=10)

wb.save("feature-spec-template.xlsx")
