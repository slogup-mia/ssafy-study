# PythonChatbot_day5

## 환경변수 설정

git bash 상에서 환경변수 설정하기 

환경변수는 git bash에서만 설정 가능 

``` git bash
$ cd ~
$ code .bashrc
```

-> 비쥬얼에서 .bashrc가 켜짐

리눅스 커맨드를 통해 변수설정 

```visual - 
export TELEGRAM_TOKEN=" #챗봇 token키값 복붙 "
export NAME="Soowon Jung"
```

환경변수는 대문자로 하는게 관례



* chatbot 으로 바로 들어가기 설정

``` visual - 
alias d5="cd ~/chatbot/day5"
```

```gitbash terminal
student@M7012 MINGW64 ~ (master)
$ d5
student@M7012 MINGW64 ~/chatbot/day5 (master)
$
```





``` python
import os
import requests

# name = os.getenv('NAME')
# token = os.getenv('TELEGRAM_TOKEN')
# method ="sendMessage"
# chat_id =""

# url = "https://api.telegram.org/bot{token}/{method}"?chat_id={chat_id}&text={name}"

    # string 수술(interpolarion)방법
    # 1. f-string 신형
# print(f"hello,{name}")
#     # 2. format() 구형
# print("hello,{}".format(name))



from pprint import pprint as pp


name = os.getenv('NAME')
token = os.getenv('TELEGRAM_TOKEN')

method ="getUpdates"
url = f"https://api.telegram.org/bot{token}/{method}"

res = requests.get(url)
doc= res.json()
    # json.loads() => 파이선 딕셔너리로 바꿔준다 
#pp(doc['result'][0]['message']['chat']['id'])
    #위의 json을 통한 탐험으로 chat_id를 알아냈다  
chat_id = doc['result'][0]['message']['chat']['id']


method ="sendMessage"
url = f"https://api.telegram.org/bot{token}/{method}"

print (f"{url}?'chat_id'={chat_id}&text={name}")
requests.get(f"{url}?'chat_id'={chat_id}&text={name}")

```

```bash
student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~ (master)
$ code .bashrc

student@M7012 MINGW64 ~ (master)
$ get .bashrc
bash: get: command not found

student@M7012 MINGW64 ~ (master)
$ cat.bashrc
bash: cat.bashrc: command not found

student@M7012 MINGW64 ~ (master)
$ cat. bashrc
bash: cat.: command not found

student@M7012 MINGW64 ~ (master)
$ cat. bashrc
bash: cat.: command not found

student@M7012 MINGW64 ~ (master)
$ cat .gitconfig
[user]
        email = flowerneco@gmail.com

student@M7012 MINGW64 ~ (master)
$ git config --global user.name

student@M7012 MINGW64 ~ (master)
$  git config --global user.name

student@M7012 MINGW64 ~ (master)
$  git config --global user.name "Soowon Jung"

student@M7012 MINGW64 ~ (master)
$ cat .gitconfig
[user]
        email = flowerneco@gmail.com
        name = Soowon Jung

student@M7012 MINGW64 ~ (master)
$ source .bashrc

student@M7012 MINGW64 ~ (master)
$ echo $NAME
Soowon Jung

student@M7012 MINGW64 ~ (master)
$ echo $TELEGRAM_TOKEN
711710557:AAEPxiCUJsErET74kSAmdfsh9rkfR7pzNs4

student@M7012 MINGW64 ~ (master)
$ code .bashrc

student@M7012 MINGW64 ~ (master)
$ source .bashrc

student@M7012 MINGW64 ~ (master)
$ d5
bash: cd: /c/Users/student/shatbot/day5: No such file or directory

student@M7012 MINGW64 ~ (master)
$ source .bashrc

student@M7012 MINGW64 ~ (master)
$ d5

student@M7012 MINGW64 ~/chatbot/day5 (master)
$ code .

student@M7012 MINGW64 ~/chatbot/day5 (master)
$ python get_env.py
hello,Soowon Jung
hello,Soowon Jung

student@M7012 MINGW64 ~/chatbot/day5 (master)
$ cd ..

student@M7012 MINGW64 ~/chatbot (master)
$ d5

student@M7012 MINGW64 ~/chatbot/day5 (master)
$ python get_env.py
<Response [200]>

student@M7012 MINGW64 ~/chatbot/day5 (master)
$ python get_env.py
{'ok': True,
 'result': [{'message': {'chat': {'first_name': 'jsw',
                                  'id': 788311981,
                                  'type': 'private'},
                         'date': 1545273442,
                         'from': {'first_name': 'jsw',
                                  'id': 788311981,
                                  'is_bot': False,
                                  'language_code': 'ko'},
                         'message_id': 19,
                         'text': '내 아이디를 알려줘'},
             'update_id': 116555238},
            {'message': {'chat': {'first_name': '찬미',
                                  'id': 114273033,
                                  'last_name': '정',
                                  'type': 'private'},
                         'date': 1545273773,
                         'entities': [{'length': 6,
                                       'offset': 0,
                                       'type': 'bot_command'}],
                         'from': {'first_name': '찬미',
                                  'id': 114273033,
                                  'is_bot': False,
                                  'last_name': '정'},
                         'message_id': 20,
                         'text': '/start'},
             'update_id': 116555239},
            {'message': {'chat': {'first_name': '찬미',
                                  'id': 114273033,
                                  'last_name': '정',
                                  'type': 'private'},
                         'date': 1545273788,
                         'from': {'first_name': '찬미',
                                  'id': 114273033,
                                  'is_bot': False,
                                  'language_code': 'ko',
                                  'last_name': '정'},
                         'message_id': 21,
                         'text': 'Hi'},
             'update_id': 116555240}]}

```







#### 참고

gitbash 터미널을 비주얼에서 돌리기 : 컨 +쉬 + P  - select default shell - git bash 