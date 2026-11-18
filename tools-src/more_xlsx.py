from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
import datetime
F="Arial"; HEAD=PatternFill("solid",fgColor="111111"); EX=PatternFill("solid",fgColor="EAF6EE")
thin=Side(style="thin",color="D9D9D9"); BD=Border(top=thin,bottom=thin,left=thin,right=thin)
def sheet(ws, cols, ex, blank=40, note=None):
    for i,(h,w) in enumerate(cols,1):
        c=ws.cell(row=1,column=i,value=h); c.font=Font(name=F,bold=True,color="FFFFFF"); c.fill=HEAD; c.border=BD; c.alignment=Alignment(horizontal="center",vertical="center",wrap_text=True)
        ws.column_dimensions[c.column_letter].width=w
    ws.row_dimensions[1].height=26; ws.freeze_panes="A2"
    for r,row in enumerate(ex,2):
        for i,v in enumerate(row,1):
            c=ws.cell(row=r,column=i,value=v); c.font=Font(name=F,size=10); c.fill=EX; c.border=BD; c.alignment=Alignment(wrap_text=True,vertical="top")
    for r in range(len(ex)+2,len(ex)+2+blank):
        for i in range(1,len(cols)+1):
            c=ws.cell(row=r,column=i); c.font=Font(name=F,size=10); c.border=BD
    if note:
        n=ws.cell(row=len(ex)+3+blank,column=1,value=note); n.font=Font(name=F,size=9,italic=True,color="8A8A8A")
    return len(ex)+1+blank
def dv(ws,rng,opts):
    d=DataValidation(type="list",formula1='"'+",".join(opts)+'"',allow_blank=True); ws.add_data_validation(d); d.add(rng)
NOTE="연두색 줄은 작성 예시예요. 흰 칸에 입력하고, 수식 칸(회색 글씨 열)은 자동 계산돼요. — 그린 AI Lab"

# 1 콘텐츠 캘린더
wb=Workbook(); ws=wb.active; ws.title="콘텐츠 캘린더"
d0=datetime.date(2026,12,1)
ex=[[d0,None,"인스타","캐러셀","회의록 프롬프트 3개","아직도 회의록 쓰느라 야근하세요?","게시 완료","",1200,85],
    [d0+datetime.timedelta(2),None,"릴스","릴스","Kling 광고 영상 만들기","이 광고, 촬영 0번 했어요","제작 중","",None,None],
    [d0+datetime.timedelta(4),None,"스레드","스레드","AI 툴 고르는 3가지 질문","툴 10개보다 하나를 깊게","아이디어","",None,None]]
last=sheet(ws,[("날짜",12),("요일",6),("채널",10),("형식",10),("주제",26),("첫 문장(훅)",30),("상태",10),("링크",18),("도달",9),("저장",9),("저장률",9)],ex,note=NOTE)
for r in range(2,last+1):
    ws.cell(row=r,column=1).number_format="yyyy-mm-dd"
    ws.cell(row=r,column=2,value=f'=IF(A{r}="","",CHOOSE(WEEKDAY(A{r}),"일","월","화","수","목","금","토"))')
    c=ws.cell(row=r,column=11,value=f'=IF(OR(I{r}="",I{r}=0),"",J{r}/I{r})'); c.number_format="0.0%"
dv(ws,f"C2:C{last}",["인스타","릴스","스레드","유튜브","블로그","뉴스레터"]); dv(ws,f"D2:D{last}",["캐러셀","릴스","스레드","쇼츠","글","메일"]); dv(ws,f"G2:G{last}",["아이디어","제작 중","예약","게시 완료"])
wb.save("content-calendar.xlsx")

# 2 광고 A/B 테스트
wb=Workbook(); ws=wb.active; ws.title="AB 테스트"
ex=[["A","제품 단독컷 + 숫자형","숫자 헤드라인이 클릭을 더 부른다",12000,240,None,12,None,180000,None,""],
    ["B","라이프스타일컷 + 공감형","공감 장면이 전환을 더 부른다",11800,206,None,15,None,180000,None,""]]
last=sheet(ws,[("안",6),("소재 설명",24),("가설",28),("노출",10),("클릭",9),("클릭률",9),("전환",8),("전환율",9),("비용(원)",12),("전환당 비용",12),("결론",24)],ex,note=NOTE)
for r in range(2,last+1):
    c=ws.cell(row=r,column=6,value=f'=IF(OR(D{r}="",D{r}=0),"",E{r}/D{r})'); c.number_format="0.00%"
    c=ws.cell(row=r,column=8,value=f'=IF(OR(E{r}="",E{r}=0),"",G{r}/E{r})'); c.number_format="0.0%"
    c=ws.cell(row=r,column=10,value=f'=IF(OR(G{r}="",G{r}=0),"",I{r}/G{r})'); c.number_format="#,##0"
    ws.cell(row=r,column=9).number_format="#,##0"; ws.cell(row=r,column=4).number_format="#,##0"
wb.save("ab-test-log.xlsx")

# 3 사용자 인터뷰 기록지
wb=Workbook(); ws=wb.active; ws.title="인터뷰 기록"
ex=[["P1","2026-12-03","29세 마케터","광고 소재를 매주 10개 만든다","\"캔바로 하다 보면 새벽이에요\"","시간 부족","제작 속도","템플릿보다 '바로 쓸 문구'를 원함"],
    ["P2","2026-12-04","33세 기획자","회의록을 직접 정리한다","\"회의록 쓰는 게 일의 절반\"","반복 작업","문서 정리","정리 형식이 정해져 있으면 AI에 맡길 의향"]]
last=sheet(ws,[("참가자",8),("날짜",12),("특징",16),("현재 행동",26),("인상적인 말(그대로)",30),("불편 태그",12),("기회 태그",12),("인사이트",30)],ex,note=NOTE)
dv(ws,f"F2:F{last}",["시간 부족","반복 작업","비용","어려움","신뢰 부족","기타"]); dv(ws,f"G2:G{last}",["제작 속도","문서 정리","학습","자동화","기타"])
s2=wb.create_sheet("태그 집계")
s2["A1"],s2["B1"]="불편 태그","횟수"
for c in ("A1","B1"): s2[c].font=Font(name=F,bold=True,color="FFFFFF"); s2[c].fill=HEAD
for i,t in enumerate(["시간 부족","반복 작업","비용","어려움","신뢰 부족","기타"],2):
    s2[f"A{i}"]=t; s2[f"B{i}"]=f"=COUNTIF('인터뷰 기록'!$F$2:$F${last},A{i})"
s2.column_dimensions["A"].width=16
wb.save("interview-log.xlsx")

# 4 AI 툴 구독 관리표
wb=Workbook(); ws=wb.active; ws.title="구독 관리"
ex=[["ChatGPT","글·기획",29000,"매월 5일","매일","유지"],["Kling AI","광고 영상",15000,"매월 12일","주 1회","검토"],["Midjourney","이미지",14000,"매월 20일","월 2회","해지 고려"]]
last=sheet(ws,[("툴",16),("용도",16),("월 요금(원)",13),("결제일",12),("사용 빈도",11),("판단",11)],ex,blank=25,note=NOTE+" 예시 요금은 형식을 보여주는 임의 값이에요. 실제 요금을 넣어 주세요.")
for r in range(2,last+1): ws.cell(row=r,column=3).number_format="#,##0"
dv(ws,f"E2:E{last}",["매일","주 3회","주 1회","월 2회","거의 안 씀"]); dv(ws,f"F2:F{last}",["유지","검토","해지 고려"])
ws.cell(row=last+1,column=2,value="월 합계").font=Font(name=F,bold=True)
c=ws.cell(row=last+1,column=3,value=f"=SUM(C2:C{last})"); c.number_format="#,##0"; c.font=Font(name=F,bold=True)
ws.cell(row=last+2,column=2,value="연 환산").font=Font(name=F,bold=True)
c=ws.cell(row=last+2,column=3,value=f"=C{last+1}*12"); c.number_format="#,##0"; c.font=Font(name=F,bold=True)
ws.cell(row=last+3,column=2,value="해지 고려 합계").font=Font(name=F,bold=True)
c=ws.cell(row=last+3,column=3,value=f'=SUMIF(F2:F{last},"해지 고려",C2:C{last})'); c.number_format="#,##0"
wb.save("ai-subscription-tracker.xlsx")
