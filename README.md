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
            formatDate.js       ➕
            index.js
            lineHighlight.js
            loading.js
            modal.js
            openApi.js
            openApi_DRF.js      ➕
            result.js
            search.js
            userChatlogForm.js  ➕
            userChatlog_DRF.js  ➕
            userInfo_DRF.js     ➕
            userRegisterForm.js ➕
            userRegister_DRF.js ➕
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

- index.html <br>
  <img src="https://github.com/2zero0/BackendOrmi_project1/assets/43246395/4c6b4b01-c545-49df-8a30-ee9f2a7860cc" alt="index" width="80%">
- search.html<br>
  <img src="https://github.com/2zero0/BackendOrmi_project1/assets/43246395/0be8a85e-d733-4270-aaa1-0ca61831bbf7" alt="search" width="80%">
- result.html<br>
  <img src="https://github.com/2zero0/BackendOrmi_project1/assets/43246395/5cab789a-0b0d-445d-9598-19cd015e623c" alt="search" width="80%">

## 6. 메인 기능

- 사용자가 냉장고 속 재료를 입력하면 재료를 활용해 만들 수 있는 요리 목록 출력
  (ChatGPT API 이용)<br>
  <img src="https://github.com/2zero0/BackendOrmi_project1/assets/43246395/13401b2e-2909-4c93-a41c-4a1a8e6d3f76" width="80%">
- 사용자가 만들고자하는 요리 이름을 검색하면 요리 사진과 레시피 출력
  (Kakao 이미지 검색 API, ChatGPT API 이용)<br>
  <img src="https://github.com/2zero0/BackendOrmi_project1/assets/43246395/bdad59f3-4f08-48ae-bdca-a11dd96b9f00" width="80%">
- 회원가입 / 로그인 / 로그아웃
- 채팅 목록 / 상세내용

## 7. 개발하며 느낀점

- 우선 확실히 프로젝트를 해보아야 기술이나 언어에 대한 이해도/숙련도가 높아지는 것 같다. 이론으로 배웠을 때 잘 이해가 가지 않아 결국 넘어갔던 개념들을 프로젝트를 하면서 마주하게 되었을 때 비로소 이해하고 사용을 할 수 있었다. Java와 Python과는 달리 나에게 있어 다른 결로 느껴지는 JavaScript라는 언어는 예전부터 하나의 산처럼 오르기에 막막한 느낌이 있었다. 하지만 프로젝트를 진행하면서 JavaScript라는 산을 1/3만큼은 오른 것 같아 마음이 한결 가볍다.
- 이번 프로젝트를 하면서 가장 크게 느낀 점 중에 하나가 계속해서 개발하기에 더욱 좋은 환경이 되고있다는 점이다. ChatGPT 덕분에 프로젝트 중 오류가 생기거나 로직이 막혔을 때의 그 막막함을 해소시킬 수 있어서 정말 좋았다. 이전에 프로젝트를 했을 때 사실 한번씩 좌절을 했던 적이 있었는데 이번 프로젝트는 개인 프로젝트이지만 ChatGPT를 동료라고 생각하니 든든하기도하고 좌절의 순간이 오려고할 때 마다 힘이 많이 되었고 큰 도움을 받았다.
- 이번 프로젝트에서 기능 구현보다 코드 모듈화와 정리에 있어 더욱 시간이 오래 걸리고 힘들었던 점을 보아 초기 단계부터 네이밍 규칙이나 코드 구조를 신경써서 짜야할 것 같다고 느꼈다. 또한 하나의 기능도 세부적으로 나눠 깃에 commit을 해야 나중에 수정-관리하기도, 정리하거나 돌아보기도 편하다고 느꼈다.
- readme.md파일을 필히 신경 써 작성할 필요도 느꼈다. 이전에 진행했던 프로젝트들은 깃허브에서 readme.md파일도 작성 안하고 관리를 소홀히 했던 점을 반성했다. 왜냐하면 그 프로젝트를 이제와서 정리 해 놓으려 돌아보니 코드를 뜯어 봐야하고 시간을 또 할애해서 프로젝트 내용을 상기시켜야하니 정말 비효율적이었다. 이 점을 앞으로는 꼭 유의하여 프로젝트마다 정리를 잘 해놓고 언제 다시 들여다보아도 와닿도록 관리를 해야겠다고 깨달았다.
