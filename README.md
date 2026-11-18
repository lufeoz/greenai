# 그린 AI Lab 자료실

스티비 구독 → 자료실 → 자료 상세 페이지로 이어지는 정적 사이트예요.

- 사이트: https://greenai-205.pages.dev
- 배포: Cloudflare Pages (이 저장소 `main`에 올리면 자동 배포, 빌드 설정 없음 · 출력 폴더 `/`)

## 구조
```
index.html            구독 신청 페이지 (/)
archive.html          자료실 목록 (/archive)
class.html            1:1 클래스 소개·신청 (/class) — 신청은 크몽으로 연결
guides/*.html         자료 상세 페이지 10종 (/guides/...)
assets/guide.css      자료 페이지 공통 스타일
assets/guide.js       자료 페이지 공통 스크립트 (클래스 링크·구독자 확인 키)
files/                다운로드 파일 (기획서 .docx, 기능명세서 .xlsx)
og.png                공유 미리보기 이미지
```

## 자주 바꾸는 곳
| 바꿀 것 | 위치 |
|---|---|
| 자료 목록 | `archive.html` 아래쪽 `ITEMS` |
| 클래스 페이지 주소 | `assets/guide.js`의 `CLASS_URL`, `archive.html`의 `CLASS_URL` (지금은 `/class`) |
| 크몽 신청 링크 | `class.html` 아래쪽 `KMONG_URL` |
| 구독자 확인 키 | `assets/guide.js`의 `KEY`, `archive.html`의 `KEY` (환영 메일 링크 `?k=`와 같게) |
| 신청 페이지 미리보기·후기 | `index.html` 아래쪽 `PEEK`, `PROOF`, `REVIEWS` |

## 방문 통계
Cloudflare 대시보드 → Pages 프로젝트 → Metrics → Web Analytics를 켜면 방문 수가 집계돼요.
