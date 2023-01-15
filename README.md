# quiz_backend_django

장고 설치
python -m pip install Django

폴더 만들고 들어가서 프로젝트 생성
django-admin startproject myapi .

quiz 폴더 생성
python .\manage.py startapp quiz

가상환경 생성
python -m venv venv

가상환경 활성화
source 명령어는 안된다
quiz_backend/venv/Scripts/activate 파일 그냥 실행하면 가상환경 시작됨

장고 restframework 설치
pip install djangorestframework 

마이그레이트 확인
python manage.py makemigrations

마이그레이트
python manage.py migrate

서버 실행ㄷ
python manage.py runserver

이거 하고 뜨는 로컬 주소로 들어가면 장고 기본 페이지가 뜸

관리자 계정 만들기
python manage.py createsuperuser

헤로쿠 배포하기
pip install django-cors-headers gunicorn psycopg2-binary whitenoise dj-database-url
-django-cors-headers : CORS(Cross-Origin Resource Sharing) 헤더를 추가해주는 라이브러리
-gunicorn : 파이썬 웹서버
-psycopg2-binary : PostgreSQL 데이터베이스를 사용하기 위한 라이브러리
-whitenoise : 정적 파일을 처리하기 위한 라이브러리
-dj-database-url : 데이터베이스 설정을 위한 라이브러리
