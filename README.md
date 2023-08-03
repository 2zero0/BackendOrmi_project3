# 냉장고 구조대 (Fridge Rescuer) 🍽 (feat. DRF)

#### 냉장고에 있는 재료들을 구조하기 위한 요리를 구상해 내고, 레시피를 검색할 수 있는 서비스입니다.
- JavaScript를 통해 동작하던 기존 코드를 DRF로 변경하여 동작하도록 수정하였습니다.

## 1. 목표와 기능

### 1.1 목표

- DRF 이해와 활용
- JWT 이해와 활용
- JavaScript를 통한 프론트와 백엔드 통신

### 1.2 기능

- ChatGPT API를 이용한 요리 목록, 레시피 출력
- Kakao 이미지검색 API를 이용한 음식 사진 출력
- 회원가입 / 로그인 / 로그아웃
- 사용자별 채팅 목록 조회 / 채팅 상세 내용

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
### 3.2 DB 구조(ERD)

<img width="80%" src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/5ee94c40-2cde-442f-9921-6f26a892c614">


### 3.3 개발 일정(WBS)

- 7/26: DB 구조 및 개발 일정 계획
- 7/27: DRF 기본 세팅, 모델 구현
- 7/28 ~ 7/29: 기존 JS코드 DRF로 변경 (ChatGPT 요청-응답 부분)
- 7/30 ~ 7/31: 회원가입, 로그인, 로그아웃 기능 구현
- 8/1: 사용자별 채팅 목록, 채팅 상세 내용 조회 기능 구현
- 8/2: 사용자 챗봇 이용 횟수 제한 추가, 코드 모듈화 및 디자인 상세 수정 
- 8/3: 프로젝트 마무리 및 리뷰

## 4. 역할 분담

- 모든 역할과 작업은 개인이 수행

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
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/d6894448-9635-4013-a21b-35b804d960bb" width="80%">
<br>

- user_chatlog_detail.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/1375fe69-8396-4838-9d68-1c719950e453" width="80%">
<br>

## 6. 메인 기능

- 사용자가 냉장고 속 재료를 입력하면 재료를 활용해 만들 수 있는 요리 목록 출력
  (ChatGPT API 이용) <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/ccab4bb4-55a0-47ad-8609-84e94f2b5c6b" width="80%">
  <br>

  - 미로그인 사용자 챗봇 사용 불가<br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/04503dd2-2005-4675-969b-b1db42dd7079" width="80%">
  <br>
  
  - 챗봇 하루 5회 초과시 사용 불가<br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/47442eb6-f544-4536-ad69-f03f2ad76c3e" width="80%">
<br>

- 사용자가 만들고자하는 요리 이름을 검색하면 요리 사진과 레시피 출력
  (Kakao 이미지 검색 API, ChatGPT API 이용) <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/5b04e8b6-6c47-44f3-8da1-627f5140a8c0" width="80%">
<br>

- 회원가입 / 로그인 / 로그아웃 <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/3cb97e95-0560-4c78-a69e-b19ac19405c2" width="80%">
<br>

- 사용자별 채팅 목록 / 상세내용 <br>
  <img src="https://github.com/2zero0/BackendOrmi_project3/assets/43246395/44622f70-e87c-4e0a-9099-3feb62bbcf7a" width="80%">
<br>

## 7. 개발하며 느낀점

- 개인으로 OpenAI 키를 발급 받아 여러차례 테스트하면서 개발을 진행했었는데 RateLimitError가 났었습니다. 무료에는 사용량 한계가 있는 점을 간과하고 과도한 테스트를 하다보니 한 2일만에 그 사용량을 초과 해 버렸습니다. 이에 결국 멘토님께 요청하여 키를 한번 더 발급 받아 사용하게 되었습니다. 무료 계정일 경우 테스트를 다소 가볍게하지 않는 것이 좋겠습니다.

- 초기 CORS 에러로 인하여 settings.py 파일의 INSTALLED_APPS에 'corsheaders'를 추가해줬고 MIDDLEWARE에 'corsheaders.middleware.CorsMiddleware'를 추가, 프론트엔드와 원할한 통신을 위하여
CORS_ALLOWED_ORIGINS = [ "FrontURL", ] 이러한 코드를 설정에 추가하여 해결하였습니다.

- 채팅 내용 상세보기 같은 경우 프론트단에서 "user_chatlog_detail.html?logId=${log.id}" 이러한 형식으로 각 질문마다 a 태그의 하이퍼링크 뒤에 매개변수를 걸어주고 상세보기 페이지에서는 JavaScript의 API와 내장 함수인
URLSearchParams(window.location.search).get("logId")
URLSearchParams를 이용하여 특정 채팅 내용 id 값을 추출한 후 
chatLogs.find(log => log.id === logId)
find로 채팅 목록 중 앞서 추출한 id값을 가진 채팅 내용을 찾아 사용자에게 보여줄 수 있도록하였습니다.

- 인증과 관련하여 JWT를 사용하였는데 로그인시 발급 받은 ACCESS토큰을 로컬 스토리지에 저장하고 사용자 정보 관련한 접근시 클라이언트는 로컬스토리지에 있는 토큰 값을 headers에 담아 장고 DRF서버로 요청하면 인증 관련 응답을 보내줍니다. <br>
JWT를 완벽히 이해하는데는 시간이 짧아 사실 제대로 알고 쓴 건지는 잘 모르겠습니다. 프로젝트를 더욱 고도화시키면서 JWT를 이해하고 활용하기 위해서 시간을 들여야할 것 같습니다.

- Serializer 없이 json형식으로 요청을 보내고 받아오는식으로 직접 구현하였습니다.<br>
Serializer와 Router, ViewSet이 DRF의 대표적인 클래스라고하여 이 세가지를 활용해 보고 싶었는데 그러지 못하여 아쉽습니다. 이제 첫 걸음을 뗐으니 더욱 걸음을 내딛으면서 DRF와 친숙해지도록 해야겠습니다.