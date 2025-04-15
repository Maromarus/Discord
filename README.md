# 디스코드 수업시간 알람 봇

---

## 프로젝트 설명

- EST BACKEND 수업을 위해 만들어진 프로젝트
- 수업 시간과 쉬는 시간 알림 및 퇴실, 입실 체크에 필요한 내용 전달용 디스코드 봇

---

## 준비사항

### Python

- [python 다운로드 페이지](https://www.python.org/downloads/)

  - 위의 페이지를 눌러 다운로드 진행
  - 파이썬으로 개발을 진행하실 분이 아니라면 굳이 버전 상관 쓰지 않으셔도 괜찮습니다.

- 다운로드 후 터미널(cmd / powershell)을 이용하여 현재 폴더에 접근
  - 접근하시는 방법 :
  1. 현재 폴더가 있는 경로(윈도우 : 폴더 주소창 클릭 후 전체, MAC : command + option + C) 복사
  2. 터미널에 `cd 복사한경로` 처럼 붙여넣기
  3. 터미널에 `pip install -r requirements.txt` 입력

---

### Discord Bot Token

1. [디스코드 개발자 페이지](https://discord.com/developers/applications) 접속 후 로그인
2. 오른쪽 상단의 `New Application` 클릭
3. 만들어진 Bot 설정하기
   - name : 원하는 이름
   - App icon : 봇의 프로필 사진
   - Description : 봇에 대한 설명
4. 왼쪽 탭들중 `bot` 진입
5. 가운데 `Reset Token` 버튼을 눌러 토큰 발행 후 복사해두기
   - 후술할 `.env` 파일에 붙여 넣을 예정이니 다른곳에 붙여두기
6. 모든게 끝난후 돌아올 페이지이기 때문에 종료 하지 말기

---

### .env 파일

1. 노트패드(메모장)과 같이 글을 저장 할수 있는 프로그램 켜기
2. 아래와 같은 내용으로 저장

```json
DISCORD_TOKEN=방금 복사한 디스코드 토큰 붙여넣기
```

3. 현재 폴더에 저장하는데, 저장 시 확장자 없이 `.env` 라는 이름으로 저장

---

### link.txt

1. 노트패드 켜기
2. 입장을 할 주소 입력 ex) zoom.com/~~~
3. `data` 폴더안에 link.txt 라는 이름으로 저장

---

## 실행 방법

1. 제공할 QR 코드 사진을 `images` 폴더에 `QR_test.png`라는 이름으로 저장
2. 터미널에서 현재 폴더에 접속
3. 터미널에 `python bot.py` 를 입력해 bot 실행 (켜져있어야 봇 작동)
4. [디스코드 개발자 페이지](https://discord.com/developers/applications)에서 왼쪽 탭중 `OAuth2` 접속
5. 아래 다양한 체크 박스 중 `bot` 을 찾아 체크
6. 새로 생긴 아래의 체크 박스 중 아래의 체크박스 체크
   - Send Messages
   - Embeded Links
   - Attach Files
7. 체크후 맨 아래 생성된 `Generated URL` 의 주소를 복사
8. 인터넷 주소창에 URL 입력 후 원하는 채널에 넣기

---

## BOT 의 기능

- 아침 안내 :

  - 매일 아침 8시 50분에 입장 링크(link.txt)와 함께, QR 코드(QR_test.png) 제공

- 쉬는 시간 안내 :

  - 매시 50분에 쉬는시간 알림

- 수업시간 안내 :

  - 매시 정각 수업 시작 알림

- 수업 종료 안내 :
  - 매일 오후 17시 55분에 QR 코드와 함께 종료 알림 및 퇴실체크 리마인드
