# PythonChatbot_day4

## 배운내용 정리

### day1

- 폴더 안 파일들의 이름을 일괄 바꾸기  

- 홈페이지의 정보를 끌어오기 (스크랩)



### day2

- 네이버 1위 검색어 끌어오고, 1위 검색어 검색페이지 브라우저 열기 
- 화요일 웹툰 제목 끌어오고 화요일 웹툰 브라우저 열기
- 챗봇이 나에게 메세지 보내게 하기 
- 챗봇이 10초마다 메세지 보내게 하기 
- 챗봇이 미세먼지 농도를 알려주게 하기 
- 로또번호 (비복원 무작위 추출) 출력하기 
- 로또당첨번호를 스크랩해서 내 로또번호와 비교하여 "0등입니다" 출력하기



### day3 

- html 헤드와 바디 꾸리기, 색 설정 하여 페이지 만들기
- html 테이블, 사진과 동영상 넣기
- html 텍스트와 이미지에 링크걸기 
- py와 html 를 @app.route로 연결하여 입력값에 따라 결과 페이지를 보기 





### day4

- text 파일 읽기, 쓰기, 수정하기
- csv 파일 읽기, 쓰기, 수정하기
- 오늘이 새해인지 아닌지 알려주는 웹페이지 만들기
- 사용자의 이름을 받고, 랜덤으로 생성된 전생직업을 알려주기 
- 두번째 이후로 전생직업을 받는 사용자가 이전과 같은 직업을 받을 수 있도록 저장하기
- 두 사람의 이름을 받고, 둘의 궁합(랜덤숫자)을 알려주기 
- 궁합을 조회한 두 사람의 이름을 저장하고 조회하기  





### flask terminal 참고 

``` flask terminal
soowon:~/workspace $ cd ..
soowon:~ $ ls
lib/  workspace/
soowon:~ $ cd workspace
soowon:~/workspace $ ls
__pycache__/  etcapp/  fakesearch/
soowon:~/workspace $ cd fakesearch
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/fakesearch $ cd ..
soowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace $ cd fakesearch
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/fakesearch $ ^C
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: While importing "app", an ImportError was raised:

Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 1, in <module>
    from Flask import Flask, render_template
ImportError: No module named 'Flask'

soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 01:35:24] "GET / HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 01:40:35] "GET / HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 01:40:39] "GET /?query=tt HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 01:41:00] "GET /?query=tt HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 01:41:02] "GET /?query=r HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 01:43:44] "GET /?query=%E3%84%B9 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 01:44:53] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 01:48:01] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 01:48:22] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 01:49:03] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 01:49:21] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 01:51:01] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 02:01:26] "GET /?query=%E3%84%B7%E3%84%B1 HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:01:37] "GET /?msg=heyheyhey HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:01:46] "GET /?msg=heyheyhey HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 02:05:00] "GET /?msg=heyheyhey HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 02:05:10] "GET /?msg=heyheyhey HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 02:05:30] "GET / HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 02:05:49] "GET /?msg=heyheyhey HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:09:18] "GET /sendmsg?msg=heyheyhey HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:09:57] "GET /sendmsg HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 02:17:07] "GET /?msg=heyheyhey HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 02:17:30] "GET /?msg=heyheyhey HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 02:18:57] "GET /?msg=heyheyhey HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 02:18:59] "GET /?msg=df HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:19:08] "GET / HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:19:09] "GET /?msg=df HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 767, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 293, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 317, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 377, in load_app
    raise_if_not_found=False)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 12
    print msg
            ^
SyntaxError: Missing parentheses in call to 'print'
soowon:~/workspace/fakesearch $ ^C
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 02:22:43] "GET / HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 02:22:45] "GET /?msg=fd HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 02:22:49] "GET /?msg=dfg HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 02:25:52] "GET /?msg=dfg HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 02:25:55] "GET /?msg=df HTTP/1.1" 200 -
10.240.0.68 - - [20/Dec/2018 02:29:29] "GET /favicon.ico HTTP/1.1" 404 -
10.240.1.50 - - [20/Dec/2018 02:43:55] "GET /?msg=dlfm HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 767, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 293, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 317, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 377, in load_app
    raise_if_not_found=False)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 13
    url = f"https://api.telegram.org/bot{token}/"
                                                ^
SyntaxError: invalid syntax
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 03:33:27] "GET / HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 03:33:33] "GET /?msg=df HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 03:33:45] "GET /?msg=%E3%85%80 HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 03:34:42] "GET /?msg=%E3%84%B4%E3%85%87%E3%84%B9%E3%84%B4%E3%85%87%E3%85%8E HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 03:35:42] "GET /?msg=%E3%85%8A%ED%98%B8 HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 03:36:59] "GET /?msg=%E3%84%B1%E3%85%8E%E3%84%B7%E3%85%8E HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 03:37:02] "GET /?msg=%E3%84%B1%E3%85%8E%E3%84%B7%E3%85%8E HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 03:37:04] "GET /sendmsg?msg=%E3%84%B4%E3%85%87%E3%84%B9 HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 03:48:36] "GET /sendmsg?msg=%E3%85%87%E3%85%8E%E3%85%87%EB%A1%9C HTTP/1.1" 200 -
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 767, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 293, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 317, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 377, in load_app
    raise_if_not_found=False)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 29
    requests.get(url/sendMessage?)
                                ^
SyntaxError: invalid syntax
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 04:24:07] "GET / HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 04:24:20] "GET /sendmsg?msg=%EB%91%90%EA%B5%B3%EA%B5%AC HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 04:29:58] "GET /sendmsg?msg=%EB%91%90%EA%B5%B3%EA%B5%AC HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 04:30:32] "GET / HTTP/1.1" 200 -
[2018-12-20 04:30:38,720] ERROR in app: Exception on /sendmsg [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 18, in sendmsg
    result = url + token + "/sendMessage?chat_id=" + my_chat_id + "&text=" + msg
TypeError: Can't convert 'int' object to str implicitly
10.240.0.64 - - [20/Dec/2018 04:30:38] "GET /sendmsg?msg=%EB%91%90%EA%B5%B3%EA%B5%AC HTTP/1.1" 500 -
[2018-12-20 04:35:49,634] ERROR in app: Exception on /sendmsg [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 18, in sendmsg
    result = url + token + "/sendMessage?chat_id=" + my_chat_id + "&text=" + msg
TypeError: Can't convert 'int' object to str implicitly
10.240.0.64 - - [20/Dec/2018 04:35:49] "GET /sendmsg?msg=%EB%91%90%EA%B5%B3%EA%B5%AC HTTP/1.1" 500 -
10.240.1.191 - - [20/Dec/2018 04:36:16] "GET / HTTP/1.1" 200 -
[2018-12-20 04:36:20,077] ERROR in app: Exception on /sendmsg [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 18, in sendmsg
    result = url + token + "/sendMessage?chat_id=" + my_chat_id + "&text=" + msg
TypeError: Can't convert 'int' object to str implicitly
10.240.1.30 - - [20/Dec/2018 04:36:20] "GET /sendmsg?msg=dfgdfg HTTP/1.1" 500 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 04:36:31] "GET / HTTP/1.1" 200 -
[2018-12-20 04:36:32,917] ERROR in app: Exception on /sendmsg [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/fakesearch/app.py", line 18, in sendmsg
    result = url + token + "/sendMessage?chat_id=" + my_chat_id + "&text=" + msg
TypeError: Can't convert 'int' object to str implicitly
10.240.1.30 - - [20/Dec/2018 04:36:32] "GET /sendmsg?msg=sfdsg HTTP/1.1" 500 -
^Csoowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 04:37:41] "GET / HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 04:37:44] "GET /sendmsg?msg=sdf HTTP/1.1" 200 -
^Csoowon:~/workspace/fakesearch $ sudo pip3 install faker
Downloading/unpacking faker
  Downloading Faker-1.0.1-py2.py3-none-any.whl (845kB): 845kB downloaded
Downloading/unpacking six>=1.10 (from faker)
  Downloading six-1.12.0-py2.py3-none-any.whl
Downloading/unpacking text-unidecode==1.2 (from faker)
  Downloading text_unidecode-1.2-py2.py3-none-any.whl (77kB): 77kB downloaded
Downloading/unpacking python-dateutil>=2.4 (from faker)
  Downloading python_dateutil-2.7.5-py2.py3-none-any.whl (225kB): 225kB downloaded
Installing collected packages: faker, six, text-unidecode, python-dateutil
  Found existing installation: six 1.5.2
    Not uninstalling six at /usr/lib/python3/dist-packages, owned by OS
Successfully installed faker six text-unidecode python-dateutil
Cleaning up...
soowon:~/workspace/fakesearch $ python3
Python 3.4.3 (default, Nov 17 2016, 01:08:31)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import faker
>>> from faker import Faker
>>> fake = Faker()
>>> fake.name()
'Cody Smith'
>>> fake.name()
'Jason Eaton'
>>> fake.name()
'Madeline Holloway'
>>> fake.job()
'Scientific laboratory technician'
>>> fake.job()
'Journalist, magazine'
>>> fake.job()
'Environmental consultant'


```

```flask terminal
[2018-12-19 07:44:11,206] ERROR in app: Exception on /kospi [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/app.py", line 101, in kospi
    doc = bs(res.text,'html.parser')
AttributeError: 'str' object has no attribute 'text'
10.240.1.30 - - [19/Dec/2018 07:44:11] "GET /kospi HTTP/1.1" 500 -
^Csoowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-19 07:46:00,445] ERROR in app: Exception on /kospi [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/app.py", line 101, in kospi
    doc = bs(res.text,'html.parser')
AttributeError: 'str' object has no attribute 'text'
10.240.1.50 - - [19/Dec/2018 07:46:00] "GET /kospi HTTP/1.1" 500 -
[2018-12-19 07:46:02,993] ERROR in app: Exception on /kospi [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/app.py", line 101, in kospi
    doc = bs(res.text,'html.parser')
AttributeError: 'str' object has no attribute 'text'
10.240.1.50 - - [19/Dec/2018 07:46:02] "GET /kospi HTTP/1.1" 500 -
^Csoowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-19 07:47:19,379] ERROR in app: Exception on /kospi [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/app.py", line 101, in kospi
    doc = bs(res.text,'html.parser')
AttributeError: 'str' object has no attribute 'text'
10.240.1.191 - - [19/Dec/2018 07:47:19] "GET /kospi HTTP/1.1" 500 -
^Csoowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-19 07:47:45,811] ERROR in app: Exception on /kospi [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/app.py", line 101, in kospi
    doc = bs(res.text,'html.parser')
AttributeError: 'str' object has no attribute 'text'
10.240.1.30 - - [19/Dec/2018 07:47:45] "GET /kospi HTTP/1.1" 500 -
^Csoowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [19/Dec/2018 07:50:08] "GET /kospi HTTP/1.1" 200 -
^Csoowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [19/Dec/2018 07:51:22] "GET /kospi HTTP/1.1" 200 -
^Csoowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace $ pip3 install flask
Requirement already satisfied (use --upgrade to upgrade): flask in /usr/local/lib/python3.4/dist-packages
Cleaning up...
soowon:~/workspace $ sudo pip3 install flask
Requirement already satisfied (use --upgrade to upgrade): flask in /usr/local/lib/python3.4/dist-packages
Cleaning up...
soowon:~/workspace $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace $ cd ~
soowon:~ $ ls
lib/  workspace/
soowon:~ $ cd workspace
soowon:~/workspace $ ls
__pycache__/  etcapp/
soowon:~/workspace $ cd etcapp
soowon:~/workspace/etcapp $ ls
README.md  app.py  templates/
soowon:~/workspace/etcapp $ cd templates
soowon:~/workspace/etcapp/templates $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/etcapp/templates $ ls
kospi.html  lotto.html  profile.html  xmas.html
soowon:~/workspace/etcapp/templates $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/etcapp/templates $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-20 00:35:07,913] ERROR in app: Exception on /lotto [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/templates/app.py", line 80, in lotto
    return render_template('lotto.html',lotto=result, name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 113, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 58, in get_source
    return self._get_source_fast(environment, template)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 86, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: lotto.html
10.240.1.30 - - [20/Dec/2018 00:35:07] "GET /lotto HTTP/1.1" 500 -
10.240.1.30 - - [20/Dec/2018 00:35:08] "GET /favicon.ico HTTP/1.1" 404 -
[2018-12-20 00:35:10,847] ERROR in app: Exception on /lotto [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/templates/app.py", line 80, in lotto
    return render_template('lotto.html',lotto=result, name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 113, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 58, in get_source
    return self._get_source_fast(environment, template)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 86, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: lotto.html
10.240.1.191 - - [20/Dec/2018 00:35:10] "GET /lotto HTTP/1.1" 500 -
^Csoowon:~/workspace/etcapp/templates $
soowon:~/workspace/etcapp/templates $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
soowon:~/workspace/etcapp/templates $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-20 00:38:36,645] ERROR in app: Exception on /lotto [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/templates/app.py", line 80, in lotto
    return render_template('lotto.html',lotto=result, name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 113, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 58, in get_source
    return self._get_source_fast(environment, template)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 86, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: lotto.html
10.240.1.30 - - [20/Dec/2018 00:38:36] "GET /lotto HTTP/1.1" 500 -
[2018-12-20 00:38:37,536] ERROR in app: Exception on /lotto [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/templates/app.py", line 80, in lotto
    return render_template('lotto.html',lotto=result, name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 113, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 58, in get_source
    return self._get_source_fast(environment, template)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 86, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: lotto.html
10.240.1.30 - - [20/Dec/2018 00:38:37] "GET /lotto HTTP/1.1" 500 -
10.240.1.30 - - [20/Dec/2018 00:38:42] "GET / HTTP/1.1" 200 -
[2018-12-20 00:38:49,932] ERROR in app: Exception on /lotto [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/templates/app.py", line 80, in lotto
    return render_template('lotto.html',lotto=result, name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 113, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 58, in get_source
    return self._get_source_fast(environment, template)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 86, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: lotto.html
10.240.1.191 - - [20/Dec/2018 00:38:49] "GET /lotto HTTP/1.1" 500 -
^Csoowon:~/workspace/etcapp/templates $ cd ~
soowon:~ $ cd workspave
bash: cd: workspave: No such file or directory
soowon:~ $ cd workspace
soowon:~/workspace $ cd etcapp
soowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 00:51:11] "GET / HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 00:51:17] "GET /lotto HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 01:00:25] "GET /newyear HTTP/1.1" 404 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 01:00:47] "GET /newyear HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 01:05:32] "GET /newyear HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 01:05:34] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $
soowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 01:05:44] "GET /newyear HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 01:05:45] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 01:06:19] "GET /newyear HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 01:06:20] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-20 01:07:18,890] ERROR in app: Exception on /newyear [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/app.py", line 110, in newyear
    return render_template('newyear.html')
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/etcapp/templates/newyear.html", line 13, in template
    <!--{%if 오늘 ==새해(1월 1일)%} 예 {%아니면%} 아니오 }-->
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 883, in subparse
    rv = self.parse_statement()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 130, in parse_statement
    return getattr(self, 'parse_' + self.stream.current.value)()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 211, in parse_if
    node.test = self.parse_tuple(with_condexpr=False)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 620, in parse_tuple
    args.append(parse())
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 612, in <lambda>
    parse = lambda: self.parse_expression(with_condexpr=False)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 433, in parse_expression
    return self.parse_or()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 450, in parse_or
    left = self.parse_and()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 459, in parse_and
    left = self.parse_not()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 470, in parse_not
    return self.parse_compare()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 480, in parse_compare
    ops.append(nodes.Operand(token_type, self.parse_math1()))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 496, in parse_math1
    left = self.parse_concat()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 507, in parse_concat
    args = [self.parse_math2()]
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 517, in parse_math2
    left = self.parse_pow()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 528, in parse_pow
    left = self.parse_unary()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 547, in parse_unary
    node = self.parse_postfix(node)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 676, in parse_postfix
    node = self.parse_call(node)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 767, in parse_call
    self.stream.expect('comma')
  File "/usr/local/lib/python3.4/dist-packages/jinja2/lexer.py", line 384, in expect
    self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: expected token ',', got '월'
10.240.1.30 - - [20/Dec/2018 01:07:18] "GET /newyear HTTP/1.1" 500 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
[2018-12-20 01:12:41,147] ERROR in app: Exception on /newyear [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/app.py", line 110, in newyear
    print(now.month)
AttributeError: 'builtin_function_or_method' object has no attribute 'month'
10.240.1.30 - - [20/Dec/2018 01:12:41] "GET /newyear HTTP/1.1" 500 -
[2018-12-20 01:12:44,068] ERROR in app: Exception on /newyear [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/app.py", line 110, in newyear
    print(now.month)
AttributeError: 'builtin_function_or_method' object has no attribute 'month'
10.240.0.64 - - [20/Dec/2018 01:12:44] "GET /newyear HTTP/1.1" 500 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
12
20
[2018-12-20 01:14:07,636] ERROR in app: Exception on /newyear [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/app.py", line 113, in newyear
    return render_template('newyear.html',isNew=isNewyear)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/etcapp/templates/newyear.html", line 13, in template
    <!--{%if 오늘 ==새해(1월 1일)%} 예 {%아니면%} 아니오 }-->
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 883, in subparse
    rv = self.parse_statement()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 130, in parse_statement
    return getattr(self, 'parse_' + self.stream.current.value)()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 211, in parse_if
    node.test = self.parse_tuple(with_condexpr=False)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 620, in parse_tuple
    args.append(parse())
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 612, in <lambda>
    parse = lambda: self.parse_expression(with_condexpr=False)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 433, in parse_expression
    return self.parse_or()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 450, in parse_or
    left = self.parse_and()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 459, in parse_and
    left = self.parse_not()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 470, in parse_not
    return self.parse_compare()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 480, in parse_compare
    ops.append(nodes.Operand(token_type, self.parse_math1()))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 496, in parse_math1
    left = self.parse_concat()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 507, in parse_concat
    args = [self.parse_math2()]
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 517, in parse_math2
    left = self.parse_pow()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 528, in parse_pow
    left = self.parse_unary()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 547, in parse_unary
    node = self.parse_postfix(node)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 676, in parse_postfix
    node = self.parse_call(node)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 767, in parse_call
    self.stream.expect('comma')
  File "/usr/local/lib/python3.4/dist-packages/jinja2/lexer.py", line 384, in expect
    self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: expected token ',', got '월'
10.240.0.213 - - [20/Dec/2018 01:14:07] "GET /newyear HTTP/1.1" 500 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
12
20
[2018-12-20 01:15:51,771] ERROR in app: Exception on /newyear [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/etcapp/app.py", line 113, in newyear
    return render_template('newyear.html', isNew = isNewyear)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/etcapp/templates/newyear.html", line 13, in template
    <!--{%if 오늘 ==새해(1월 1일)%} 예 {%아니면%} 아니오 }-->
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 883, in subparse
    rv = self.parse_statement()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 130, in parse_statement
    return getattr(self, 'parse_' + self.stream.current.value)()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 211, in parse_if
    node.test = self.parse_tuple(with_condexpr=False)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 620, in parse_tuple
    args.append(parse())
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 612, in <lambda>
    parse = lambda: self.parse_expression(with_condexpr=False)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 433, in parse_expression
    return self.parse_or()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 450, in parse_or
    left = self.parse_and()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 459, in parse_and
    left = self.parse_not()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 470, in parse_not
    return self.parse_compare()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 480, in parse_compare
    ops.append(nodes.Operand(token_type, self.parse_math1()))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 496, in parse_math1
    left = self.parse_concat()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 507, in parse_concat
    args = [self.parse_math2()]
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 517, in parse_math2
    left = self.parse_pow()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 528, in parse_pow
    left = self.parse_unary()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 547, in parse_unary
    node = self.parse_postfix(node)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 676, in parse_postfix
    node = self.parse_call(node)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 767, in parse_call
    self.stream.expect('comma')
  File "/usr/local/lib/python3.4/dist-packages/jinja2/lexer.py", line 384, in expect
    self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: expected token ',', got '월'
10.240.1.191 - - [20/Dec/2018 01:15:51] "GET /newyear HTTP/1.1" 500 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
12
20
10.240.1.191 - - [20/Dec/2018 01:16:56] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 01:18:29] "GET /newyear HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 01:18:31] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 01:18:50] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 01:19:19] "GET /newyear HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 01:19:21] "GET /newyear HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 01:19:28] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
12
20
10.240.1.191 - - [20/Dec/2018 01:19:59] "GET /newyear HTTP/1.1" 200 -
12
20
10.240.1.30 - - [20/Dec/2018 01:20:01] "GET /newyear HTTP/1.1" 200 -
^Csoowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
12
20
10.240.0.213 - - [20/Dec/2018 01:20:27] "GET /newyear HTTP/1.1" 200 -
soowon:~/workspace/etcapp $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 771, in run_command
    threaded=with_threads, ssl_context=cert)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 814, in run_simple
    inner()
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 774, in inner
    fd=fd)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 660, in make_server
    passthrough_errors, ssl_context, fd=fd)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 577, in __init__
    self.address_family), handler)
  File "/usr/lib/python3.4/socketserver.py", line 430, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/http/server.py", line 133, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.4/socketserver.py", line 444, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
soowon:~/workspace/etcapp $ ad ..
bash: ad: command not found
soowon:~/workspace/etcapp $ cd ..
soowon:~/workspace $ cd vonvon
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 771, in run_command
    threaded=with_threads, ssl_context=cert)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 814, in run_simple
    inner()
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 774, in inner
    fd=fd)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 660, in make_server
    passthrough_errors, ssl_context, fd=fd)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/serving.py", line 577, in __init__
    self.address_family), handler)
  File "/usr/lib/python3.4/socketserver.py", line 430, in __init__
    self.server_bind()
  File "/usr/lib/python3.4/http/server.py", line 133, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.4/socketserver.py", line 444, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
soowon:~/workspace/vonvon $ ls
__pycache__/  app.py  templates/
soowon:~/workspace/vonvon $ cd ~
soowon:~ $ ls
lib/  workspace/
soowon:~ $ ls al
ls: cannot access al: No such file or directory
soowon:~ $ ls a
ls: cannot access a: No such file or directory
soowon:~ $ cat .bashrc
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

. /etc/apache2/envvars

# If not running interactively, don't do anything else
[ -z "$PS1" ] && return

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi

PS1='\[\033[01;32m\]${C9_USER}\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(__git_ps1 " (%s)") $ '

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

export rvm_silence_path_mismatch_check_flag=1

soowon:~ $ ls
lib/  workspace/
soowon:~ $ cd workspace
soowon:~/workspace $ cd vonvon
soowon:~/workspace/vonvon $ ls
__pycache__/  app.py  templates/
soowon:~/workspace/vonvon $ git init
Initialized empty Git repository in /home/ubuntu/workspace/vonvon/.git/
soowon:~/workspace/vonvon (master) $ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        app.py
        templates/

nothing added to commit but untracked files present (use "git add" to track)
soowon:~/workspace/vonvon (master) $ git add .
soowon:~/workspace/vonvon (master) $ git commit -m "first commit"
[master (root-commit) 8dd65ac] first commit
 6 files changed, 148 insertions(+)
 create mode 100644 app.py
 create mode 100644 templates/admin.html
 create mode 100644 templates/index.html
 create mode 100644 templates/match.html
 create mode 100644 templates/pastlife.html
 create mode 100644 templates/pl.html
soowon:~/workspace/vonvon (master) $ git remote add origin https://github.com/JungSWon/vonvon_project.git
soowon:~/workspace/vonvon (master) $ pit push -u origin master
bash: pit: command not found
soowon:~/workspace/vonvon (master) $ git push -u origin master
Username for 'https://github.com': JungSWon
Password for 'https://JungSWon@github.com': 
Counting objects: 9, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 2.11 KiB | 2.11 MiB/s, done.
Total 9 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), done.
To https://github.com/JungSWon/vonvon_project.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
soowon:~/workspace/vonvon (master) $ git push -u origin master
Username for 'https://github.com': 
```

```flask terminal
soowon:~/workspace $ cd ..
soowon:~ $ cd vonvon
bash: cd: vonvon: No such file or directory
soowon:~ $ ls
lib/  workspace/
soowon:~ $ cd workspace
soowon:~/workspace $ cd vonvon
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Failed to find Flask application or factory in module "app". Use "FLASK_APP=app:name to specify one.
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 05:19:42] "GET / HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 05:19:45] "GET /pastlife?username=sdd HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 05:23:23] "GET /pastlife?username=sw HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon $ python3
Python 3.4.3 (default, Nov 17 2016, 01:08:31)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> babos = {"john":"teacher","tak":"developer"}
>>> john in babos
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'john' is not defined
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 05:34:05] "GET / HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 05:34:12] "GET /pastlife?username=%EC%A0%95%EC%88%98%EC%9B%90 HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 05:34:16] "GET / HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 05:34:18] "GET /pastlife?username=%EC%A0%95%EC%88%98%EC%9B%90 HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 767, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 293, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 317, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 377, in load_app
    raise_if_not_found=False)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/vonvon/app.py", line 49, in <module>
    @app.route('admin')
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1250, in decorator
    self.add_url_rule(rule, endpoint, f, **options)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 66, in wrapper_func
    return f(self, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1213, in add_url_rule
    rule = self.url_rule_class(rule, methods=methods, **options)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/routing.py", line 603, in __init__
    raise ValueError('urls must start with a leading slash')
ValueError: urls must start with a leading slash
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 767, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 293, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 317, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 377, in load_app
    raise_if_not_found=False)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/vonvon/app.py", line 49, in <module>
    @app.route('admin')
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1250, in decorator
    self.add_url_rule(rule, endpoint, f, **options)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 66, in wrapper_func
    return f(self, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1213, in add_url_rule
    rule = self.url_rule_class(rule, methods=methods, **options)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/routing.py", line 603, in __init__
    raise ValueError('urls must start with a leading slash')
ValueError: urls must start with a leading slash
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 06:20:19] "GET / HTTP/1.1" 200 -
[2018-12-20 06:20:26,991] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{ }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.1.30 - - [20/Dec/2018 06:20:27] "GET /match?me=+%EB%82%98&you=%EB%84%88 HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 06:20:41] "GET / HTTP/1.1" 200 -
[2018-12-20 06:20:44,561] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.1.30 - - [20/Dec/2018 06:20:44] "GET /match?me=%EB%82%98&you=%EB%84%88 HTTP/1.1" 500 -
[2018-12-20 06:21:43,776] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.213 - - [20/Dec/2018 06:21:43] "GET /match?me=%EB%82%98&you=%EB%84%88 HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 06:25:33] "GET / HTTP/1.1" 200 -
[2018-12-20 06:25:36,948] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.1.50 - - [20/Dec/2018 06:25:36] "GET /match?yourname=sk&partnername=sj HTTP/1.1" 500 -
[2018-12-20 06:25:39,893] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.1.30 - - [20/Dec/2018 06:25:39] "GET /match?yourname=sk&partnername=sj HTTP/1.1" 500 -
[2018-12-20 06:25:42,333] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.64 - - [20/Dec/2018 06:25:42] "GET /match?yourname=sk&partnername=sj HTTP/1.1" 500 -
10.240.1.50 - - [20/Dec/2018 06:25:43] "GET / HTTP/1.1" 200 -
[2018-12-20 06:25:46,493] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.64 - - [20/Dec/2018 06:25:46] "GET /match?yourname=dfd&partnername=dfdf HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 06:27:19] "GET / HTTP/1.1" 200 -
[2018-12-20 06:27:20,869] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.64 - - [20/Dec/2018 06:27:20] "GET /match?yourname=dfg&partnername=dfg HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 06:28:02] "GET / HTTP/1.1" 200 -
[2018-12-20 06:28:04,980] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.64 - - [20/Dec/2018 06:28:04] "GET /match?yourname=fgh&partnername=ghf HTTP/1.1" 500 -
10.240.0.64 - - [20/Dec/2018 06:28:10] "GET / HTTP/1.1" 200 -
[2018-12-20 06:28:12,146] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.64 - - [20/Dec/2018 06:28:12] "GET /match?yourname=ghjgj&partnername=ghjg HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 06:28:22] "GET / HTTP/1.1" 200 -
[2018-12-20 06:28:25,023] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.1.30 - - [20/Dec/2018 06:28:25] "GET /match?yourname=fg&partnername=fg HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 06:29:55] "GET / HTTP/1.1" 200 -
[2018-12-20 06:29:58,328] ERROR in app: Exception on /match [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/ubuntu/workspace/vonvon/app.py", line 46, in match
    return render_template('match.html',yourname=yourname, partnername=partnername, percent=percent)
  File "/usr/local/lib/python3.4/dist-packages/flask/templating.py", line 134, in render_template
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 869, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 830, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 804, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/loaders.py", line 125, in load
    code = environment.compile(source, name, filename)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 591, in compile
    self.handle_exception(exc_info, source_hint=source_hint)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "/home/ubuntu/workspace/vonvon/templates/match.html", line 11, in template
    <p>{{  }}%입니다!</p>
  File "/usr/local/lib/python3.4/dist-packages/jinja2/environment.py", line 497, in _parse
    return Parser(self, source, name, encode_filename(filename)).parse()
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 901, in parse
    result = nodes.Template(self.subparse(), lineno=1)
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 875, in subparse
    add_data(self.parse_tuple(with_condexpr=True))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 637, in parse_tuple
    describe_token(self.stream.current))
  File "/usr/local/lib/python3.4/dist-packages/jinja2/parser.py", line 59, in fail
    raise exc(msg, lineno, self.name, self.filename)
jinja2.exceptions.TemplateSyntaxError: Expected an expression, got 'end of print statement'
10.240.0.213 - - [20/Dec/2018 06:29:58] "GET /match?yourname=werw&partnername=werwer HTTP/1.1" 500 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.213 - - [20/Dec/2018 06:30:47] "GET / HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 06:30:49] "GET /match?yourname=dfgdfg&partnername=dfg HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 11, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 894, in main
    cli.main(args=args, prog_name=name)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 557, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 717, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 1137, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 956, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/decorators.py", line 64, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/click/core.py", line 555, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 767, in run_command
    app = DispatchingApp(info.load_app, use_eager_loading=eager_loading)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 293, in __init__
    self._load_unlocked()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 317, in _load_unlocked
    self._app = rv = self.loader()
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 377, in load_app
    raise_if_not_found=False)
  File "/usr/local/lib/python3.4/dist-packages/flask/cli.py", line 235, in locate_app
    __import__(module_name)
  File "/home/ubuntu/workspace/vonvon/app.py", line 51, in <module>
    @app.route('admin')
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1250, in decorator
    self.add_url_rule(rule, endpoint, f, **options)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 66, in wrapper_func
    return f(self, *args, **kwargs)
  File "/usr/local/lib/python3.4/dist-packages/flask/app.py", line 1213, in add_url_rule
    rule = self.url_rule_class(rule, methods=methods, **options)
  File "/usr/local/lib/python3.4/dist-packages/werkzeug/routing.py", line 603, in __init__
    raise ValueError('urls must start with a leading slash')
ValueError: urls must start with a leading slash
soowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.0.64 - - [20/Dec/2018 06:40:09] "GET /match?yourname=dgh&partnername=gh HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 06:40:15] "GET /match?yourname=ff&partnername=ggg HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 06:40:20] "GET /match?yourname=fgd&partnername=gggf HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 06:40:26] "GET /admin HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
^Csoowon:~/workspace/vonvon (master) $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.191 - - [20/Dec/2018 08:48:36] "GET / HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 08:48:56] "GET /match?yourname=dg&partnername=dfg HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 08:49:39] "GET /match?yourname=%EB%82%98&partnername=%EB%84%88 HTTP/1.1" 200 -
10.240.1.50 - - [20/Dec/2018 09:00:50] "GET /match?yourname=me&partnername=you HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon (master) $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.30 - - [20/Dec/2018 09:02:37] "GET /match?yourname=me&partnername=you HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 09:02:39] "GET /match?yourname=me&partnername=you HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 09:02:42] "GET /match?yourname=dg&partnername=dfg HTTP/1.1" 200 -
10.240.0.64 - - [20/Dec/2018 09:02:51] "GET /match?yourname=d&partnername=f HTTP/1.1" 200 -
10.240.1.191 - - [20/Dec/2018 09:03:24] "GET /match?yourname=%EB%82%98&partnername=%EB%84%88 HTTP/1.1" 200 -
10.240.1.30 - - [20/Dec/2018 09:05:30] "GET / HTTP/1.1" 200 -
^Csoowon:~/workspace/vonvon (master) $ cd ..
soowon:~/workspace $ ls
__pycache__/  etcapp/  fakesearch/  vonvon/
soowon:~/workspace $ cd fakesearch
soowon:~/workspace/fakesearch $ flask run --host=0.0.0.0 --port=8080
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.240.1.50 - - [20/Dec/2018 09:06:08] "GET / HTTP/1.1" 200 -
10.240.0.213 - - [20/Dec/2018 09:06:14] "GET /sendmsg?msg=sfsddh HTTP/1.1" 200 -
10.240.0.231 - - [20/Dec/2018 13:47:30] "GET /favicon.ico HTTP/1.1" 404 -

```

``` flask terminal
soowon:~/workspace $ ls
__pycache__/  etcapp/  fakesearch/  vonvon/
soowon:~/workspace $ cd vonvon
soowon:~/workspace/vonvon $ python fish.cv
python: can't open file 'fish.cv': [Errno 2] No such file or directory
soowon:~/workspace/vonvon $ python fish.csv
python: can't open file 'fish.csv': [Errno 2] No such file or directory
soowon:~/workspace/vonvon $ ls
__pycache__/  app.py  templates/
soowon:~/workspace/vonvon (master) $ python fish.csv
python: can't open file 'fish.csv': [Errno 2] No such file or directory
soowon:~/workspace/vonvon (master) $ python fish.csv
python: can't open file 'fish.csv': [Errno 2] No such file or directory
soowon:~/workspace/vonvopython fish.csv
soowon:~/workspace/vonvon (master) $ python fish.csv                                                              
python: can't open file 'fish.csv': [Errno 2] No such file or directory
soowon:~/workspace/vonvon (master) $ ^C
soowon:~/workspace/vonvon (master) $ 
```

