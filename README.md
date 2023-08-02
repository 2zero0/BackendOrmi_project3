# 냉장고 구조대 (Fridge Rescuer) 🍽 (feat. DRF)

#### 냉장고에 있는 재료들을 구조하기 위한 요리를 구상해 내고, 레시피를 검색할 수 있는 서비스입니다.
- JavaScript를 통해 동작하던 기존 코드를 Django DRF로 변경하여 동작하도록 수정하였습니다.

## 1. 목표와 기능

### 1.1 목표

- DRF 이해와 활용
- JWT 이해와 활용
- JavaScript를 통한 프론트와 백엔드 통신

### 1.2 기능

- ChatGPT API를 이용한 요리 목록, 레시피 출력
- Kakao 이미지검색 API를 이용한 음식 사진 출력
- 회원가입 / 로그인 / 로그아웃
- 채팅 목록 조회 / 채팅 상세 내용

## 2. 개발 환경 및 배포 URL

### 2.1 개발 환경

- Front-end
  - HTML
  - JavaScript
  - CSS
- API
  - ChatGPT API (OpenAI)
  - Kakao 이미지검색 API
- Back-end
  - Python
  - Django REST framework
  - JSON Web Token 인증

### 2.2 배포 URL

- 

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조
- Front-end
```bash
|   .gitignore
|   README.md
|
\---project_1
    |   index.html
    |   result.html
    |   search.html
    |   user_chatlog_detail.html ➕
    |   user_chatlog_list.html   ➕
    |   user_register.html       ➕
    |
    +---css
    |       chat.css             ➕
    |       style.css
    |       style2.css           ➕
    |
    +---img
    |       back.png
    |       cancel.png
    |       carrot.png
    |       chef.png
    |       chef_user.png
    |       cooking.gif
    |       exit.png
    |       fridge.png
    |       goback.png
    |       hotpot.png
    |       kitchen_01.png
    |       kitchen_02.png
    |       log-file.png         
    |       logo.png
    |       pot.png
    |       recipebook.png
    |       search.png
    |
    \---js
            apikey.js
            data.js
            formatDate.js        ➕
            index.js
            lineHighlight.js
            loading.js
            modal.js
            openApi.js
            openApi_DRF.js       ➕
            result.js
            search.js
            userChatlogForm.js   ➕
            userChatlog_DRF.js   ➕
            userInfo_DRF.js      ➕
            userRegisterForm.js  ➕
            userRegister_DRF.js  ➕
```
<br>

- Back-end
```bash
|   .env
|   .gitignore
|   db.sqlite3
|   manage.py
|   README.md
|   requirements.txt
|   
+---chat_project
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
|   |   
|   \---__pycache__
|           
+---chatlog
|   |   admin.py
|   |   apps.py
|   |   models.py
|   |   serializers.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---migrations
|   |   |   0001_initial.py
|   |   |   0002_initial.py
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   \---__pycache__
|           
+---mychatbot
|   |   admin.py
|   |   apps.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---migrations
|   |   |   0001_initial.py
|   |   |   0002_chatrequestcounter.py
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           
|   +---templates
|   |       base.html
|   |       chat.html
|   |       
|   \---__pycache__
|           
+---myvenv
|   |   pyvenv.cfg
|   |   
|   +---Include
|   +---Lib
|   +---Scripts
|           
\---user
    |   admin.py
    |   apps.py
    |   forms.py
    |   models.py
    |   serializers.py
    |   tests.py
    |   urls.py
    |   views.py
    |   __init__.py
    |   
    +---migrations
    |   |   0001_initial.py
    |   |   __init__.py
    |   |   
    |   \---__pycache__
    |          
    |           
    +---templates
    |   \---user
    |           user_login.html
    |           user_register.html
    |           
    \---__pycache__
```

### 3.1 개발 일정(WBS)

- 7/26: DB 구조 및 개발 일정 계획
- 7/27: DRF 기본 세팅, 모델 구현
- 7/28 ~ 7/29: 기존 JS코드 DRF로 변경 (ChatGPT 요청-응답 부분)
- 7/30 ~ 7/31: 회원가입, 로그인, 로그아웃 구현
- 8/1: 유저별 채팅 목록, 채팅 상세 내용 구현
- 8/2: 유저별 챗봇 이용 횟수 제한 추가, 코드 모듈화 및 디자인 상세 수정 
- 8/3: 프로젝트 마무리 및 리뷰

## 4. 역할 분담

- 모든 역할과 작업은 개인이 수행함

## 5. UI / BM

- user_register.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/2357035f-4708-4c4f-988c-67475a4d81a2" width="80%">
  <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/650a7e3a-9a39-475a-9739-055b48ca24d5" width="80%">
<br>

- index.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/60e67837-b2d4-4903-92a3-bd14d780393b" width="80%">
<br>

- search.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/1441162f-3f36-4cc6-98fb-849bfdc8e1e7" width="80%">
<br>

- result.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/7c7ddcb8-25d6-4cc3-a736-3c092bd29e61" width="80%">
<br>

- user_chatlog_list.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/a4817a8f-e8c9-41f9-9b6f-909a11b2909f" width="80%">
<br>

- user_chatlog_detail.html
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/1375fe69-8396-4838-9d68-1c719950e453" width="80%">
<br>

## 6. 메인 기능

- 사용자가 냉장고 속 재료를 입력하면 재료를 활용해 만들 수 있는 요리 목록 출력
  (ChatGPT API 이용) <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/ccab4bb4-55a0-47ad-8609-84e94f2b5c6b" width="80%">
  <br>
  - 챗봇 5회 초과 사용 불가<br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/47442eb6-f544-4536-ad69-f03f2ad76c3e" width="80%">
<br>

- 사용자가 만들고자하는 요리 이름을 검색하면 요리 사진과 레시피 출력
  (Kakao 이미지 검색 API, ChatGPT API 이용) <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/5b04e8b6-6c47-44f3-8da1-627f5140a8c0" width="80%">
<br>

- 회원가입 / 로그인 / 로그아웃 <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/3cb97e95-0560-4c78-a69e-b19ac19405c2" width="80%">
<br>

- 채팅 목록 / 상세내용 <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/522c5b41-80d1-40b3-88e1-0a43473df797" width="80%">
<br>

## 7. 개발하며 느낀점

- 
