## instagram

- `zzu.li/install-pyenv`

- 코드 복붙  +  `pyenv install 3.6.7` +  `pyenv-global 3.6.7`

- `mkdir INSTAGRAM` - `cd INSTAGRAM` - ` pyenv virtualenv 3.6.7 insta-venv` - `pyenv local insta-venv`

- `pip install django==2.1.7`  - `pip install --upgrade pip`

- ` django-admin startproject instagram .`

- 루트폴더에 `.gitigmore` 파일 생성 후 알맞게 ignore 리스트 작성

  - 참고 : `gitignore.io` - `django` 생성  

    장고 프로젝트 생성시 필요한 gitignore 리스트 생성해준다. 복붙만 하면 됨.

- `git init ` - `git status` - `git add .gitignore` 등  

- 개발 순서(flow)를 추적하기 위해 깃 관리를 잘 해야한다. 좋은 개발자의 기본 자세. 

  폴더별 또는 작업 별 등 commit을 쪼개는 기준은 프로젝트팀(기업) 마다 다르므로 눈치껏 하면 된다.  

  commit message는 상세하게 가는 것이 좋다. 

- `git log ` : 커밋 히스토리를 볼 수 있다.

- github 접속 - 레퍼지토리 생성 - Initialize this repository with a README 는 체크안하는게 좋다. 체크 = README 자동커밋하고 시작 

- `git remote add .... ` : 깃 리모트 (연동) - `git push -u origin master`

###  서비스 기획 순서 (BDD -> TDD)

- BDD : 사용자 행동을 중심으로 기획 
- TDD : 테스트 주도 개발 . 테스트 후 개발 

1. 무엇을 하는 서비스인지?  :  사용자 interact 
2. mock up : 사용자가 어떤 화면을 볼지 
3. 데이터 모델링 : 어떤 데이터를 사용할 지  
4. 코딩



###  앱 생성

- `python manage.py startapp posts`

- model 테이블 생성 - `python manage.py makemigrations` - ` python manage.py migrate` - `git commit -m '구체적인 작업내용'`

- admin.py 클래스 설정, createsuperuser 생성 - commit 

- 루트폴더/Templates 폴더 - base.html 생성 - bootstrap starter templates 복붙

  - 참고 : Tab space가 2step 인지 4step인지 개발환경을 체크하고 통일하기 

- settings.py 

  ``` python
  TEMPLATES = [
      {
          ...
          'DIRS': [os.path.join(BASE_DIR,'templates')],
  ```

  루트폴더에 대한 BASE_DIR 절대경로에 대해 : 운영체제마다 폴더경로를 구분하는 법이 다르기 때문에 ( \ or / )  파이썬이 os 모듄 내 path 내 경로생성을 해주도록 한다. 