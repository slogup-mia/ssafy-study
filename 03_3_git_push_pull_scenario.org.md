#  GIthub_Bitbucket_PC_sync

####  참고

Vue.js - 자바스크립트만 알아도 건드리기가 쉽다. 플라스크에 가깝다. 

react - 자유도가 매우 높다. 원하는대로 만들 수 있어. 플라스크에 가깝다. 

Angular - 구글 등 엔터프라이즈 레벨에서 선호, 상대적으로 프레임워크의 룰을 잘 지키면 많은 것을 할 수 있다. 장고에 가깝다.



udacity.com - self driving car  : 100만원인데 들을 가치가 있음.싼거임 

subline text - 설치하면 경량 파이썬 구동에 좋음 



##  Push / Pull 시나리오

#### * udacity.com - how to use git and github 아주 잘 디테일되어있는 강의 

###  Bitbucket.org

new repository 생성 후 

주소 : https://JungSWon@bitbucket.org/JungSWon/bitbucket_test.git

```
student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~ (master)
$ mkdir git_practice

student@M7012 MINGW64 ~ (master)
$ cd git_practice/

student@M7012 MINGW64 ~/git_practice (master)
$ git clone https://JungSWon@bitbucket.org/JungSWon/bitbucket_test.git
Cloning into 'bitbucket_test'...
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.

student@M7012 MINGW64 ~/git_practice (master)
$ ls
bitbucket_test/

student@M7012 MINGW64 ~/git_practice (master)
$ cd bitbucket_test/

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ ls
README.md

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ code .

```

README 수정후 

git log -> status -> add -> commit ->  push -> status 

```
student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git log
commit 8be3b8e3a27ac6eba98464ff0c8ec3560d32352b (HEAD -> master, origin/master, origin/HEAD)
Author: SoowonJung <flowerneco@gmail.com>
Date:   Mon Jan 7 00:45:03 2019 +0000

    Initial commit

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git add README.md

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git commit -m "modify README.md"
[master c6ba520] modify README.md
 1 file changed, 3 insertions(+), 45 deletions(-)
 rewrite README.md (99%)

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 317 bytes | 317.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://bitbucket.org/JungSWon/bitbucket_test.git
   8be3b8e..c6ba520  master -> master

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

지금 어디에 올릴수 있는지, 로그되어있는지 확인 

```
student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git remote -v
origin  https://JungSWon@bitbucket.org/JungSWon/bitbucket_test.git (fetch)
origin  https://JungSWon@bitbucket.org/JungSWon/bitbucket_test.git (push)
```



###  github

practice repasitory 주소 https://github.com/JungSWon/git_practice.git



origin : 원격저장소의 별명으로서 기본적으로 이름 지어진 것. 

  git remote add  +'원격저장소 별명' 



second라는 원격저장소에 깃헙과 연결하여 올리기   

(= origin 원격저장소는 지금 bitbucket과 연결되어 있기 때문에 새로운 원격저장소 생성)

```
student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git remote add second  https://github.com/JungSWon/git_practice.git

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git remote -v
origin  https://JungSWon@bitbucket.org/JungSWon/bitbucket_test.git (fetch)
origin  https://JungSWon@bitbucket.org/JungSWon/bitbucket_test.git (push)
second  https://github.com/JungSWon/git_practice.git (fetch)
second  https://github.com/JungSWon/git_practice.git (push)

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git push -u second master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 1.59 KiB | 1.59 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/JungSWon/git_practice.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'second'.

```

=> bitbucket_test 내용이 깃헙에도 올라갔다. 





###  집 컴퓨터에서 git 다루기, SSAFY컴과 씽크 맞추기 

~ -> mkdir -> cd 

clone 'git주소 '-> ls (git 에 올라온 폴더가 들어왔다) ->  cd '들어온 폴더명'  -> 내용 수정 -> add . (수정된 내용 동기화) ->  commit -m "나름의 커밋" -> push 

```
student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~ (master)
$ mkdir home_computer

student@M7012 MINGW64 ~ (master)
$ cd home_computer

student@M7012 MINGW64 ~/home_computer (master)
$ git clone https://github.com/JungSWon/git_practice.git
Cloning into 'git_practice'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), done.

student@M7012 MINGW64 ~/home_computer (master)
$ ls
git_practice/

student@M7012 MINGW64 ~/home_computer (master)
$ cd git_practice

student@M7012 MINGW64 ~/home_computer/git_practice (master)
$ git add .

student@M7012 MINGW64 ~/home_computer/git_practice (master)
$ git commit -m "add content"
[master 0042087] add content
 1 file changed, 7 insertions(+), 1 deletion(-)

student@M7012 MINGW64 ~/home_computer/git_practice (master)
$ git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 451 bytes | 451.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/JungSWon/git_practice.git
   c6ba520..0042087  master -> master

```



###  다시 싸피로 와서 동기화 

`$ pull origin master` 

```
student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git pull origin master
From https://bitbucket.org/JungSWon/bitbucket_test
 * branch            master     -> FETCH_HEAD
Already up to date.

student@M7012 MINGW64 ~/git_practice/bitbucket_test (master)
$ git log
commit c6ba520433466d66570129b308c109c035aeba7c (HEAD -> master, second/master, origin/master, origin/HEAD)
Author: Soowon Jung <flowerneco@gmail.com>
Date:   Mon Jan 7 10:03:34 2019 +0900

    modify README.md

commit 8be3b8e3a27ac6eba98464ff0c8ec3560d32352b
Author: SoowonJung <flowerneco@gmail.com>
Date:   Mon Jan 7 00:45:03 2019 +0000

    Initial commit
```



만약 pull을 안땡기고(까먹고)  레퍼지토리를 수정했다면 branch 사용

branch: 다중세계를 만들어 안정성 확보





###   협업하기

git 대장과 팀원 정하기 

**대장:** 

cd~ -> mkdir 'collabo' (rm -rf '폴더명' : 만든 파일/폴더 지우기 )-> cd -> code . -> md 등 파일 생성하여 편집-> git init 프로젝트 관리를 시작->  ls -a  숨김파일인.git 파일 보기 -> add -> commit ->( - remote add origin (처음만)) -> push

```

student@M7012 MINGW64 /
$ cd ~

student@M7012 MINGW64 ~ (master)
$ mkdir collabo

student@M7012 MINGW64 ~ (master)
$ cd collabo

student@M7012 MINGW64 ~/collabo (master)
$ code .

student@M7012 MINGW64 ~/collabo (master)
$ git init
Initialized empty Git repository in C:/Users/student/collabo/.git/

student@M7012 MINGW64 ~/collabo (master)
$ ls -a
./  ../  .git/  README.md

student@M7012 MINGW64 ~/collabo (master)
$ git add README.md

student@M7012 MINGW64 ~/collabo (master)
$ git commit -m "first commit"
[master (root-commit) dc01c63] first commit
 1 file changed, 13 insertions(+)
 create mode 100644 README.md

student@M7012 MINGW64 ~/collabo (master)
$ git remote add origin https://github.com/JungSWon/collabo.git

student@M7012 MINGW64 ~/collabo (master)
$ git push -u origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 324 bytes | 324.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/JungSWon/collabo.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

초대하기 :  github - collabo repository - Settings - Collaborators - password - member name 



**팀원:** 

clone 으로 받아오기 - code. 로 열기 - 대장이 생성해놓은 파일 수정 - 배포(add-commit-push)

* github- issues : 업데이트, 요청내용 등을 알리는 마크다운 게시판 
* close issue : 해당 이슈를 닫아서 처리된 이슈로 구분한다. 다시 열 수 있다. 



**다시 대장과 팀원사이:**

`$ git pull origin master`

만약 업무가 핑퐁핑퐁이 안되고 중간에 꼬인다면? 

ex) 대장이 요청하기도 전에 팀원이 edit 하고있는데 대장이 새로 push해서 요청한 경우 

ex) 대장이 새로 push해서 요청했는데 pull 하지 않고 edit-push한 경우

git이 판단하기에 상충하는 파일상태가 있다면, conflict 발생

- pull했을때 aborting이 뜬다. 
- edit파일에 오류메세지가 뜬다. 

이때, 네가지 옵션으로 문제 해결 할 수 있다. 

* Accept current change : 내 수정사항으로 적용
* Accrept incoming change : 내가 미처 pull 하지 않은 내용 들여오기 
* Accept both change : 내 내용, 상대 내용 둘다 적용
* Compare change : 뭐가 다른지 비교해보기 
* 또는 : 직접 내용을 삭제하여 해결  

그다음 add -> commit -> push 

* conplict 해결 후 commit할 때에는 commit -m "merge conflict"라고 명시해 주는 것이 보통이다. 



###  동시에 팀플작업하기 : brancing

* 'master'라고 하는 단일 브랜치에서 확장되어 사용한다. 
* git flow(복잡하고, 상업적 큰 서버를 돌릴 때 쓴다) brancing 에서는 'master'는 서버가 궁극적으로 돌아가는 위치이므로 pull push는 가장 가끔 하게 된다. 
* github flow가 덜 복잡하다. 소규모 팀플에 제격 



새폴더 - code . - 새파일  - (init 처음이므로) - add . - commit 



**master branch 말고 second branch 세계에서 작업하기**

 `$ git branch` 지금 현재 존재하는 세계들 보기 

`git branch new_world` 'new_world'라는 세계 만들기 

`git checkout new_world ` 'new_world'로 세계 이동 

- master에서 new_world로 checkout 하기 전(작업 시작 전)엔 반드시 masterd의 state를 확인해야 한다.    

* 각 세계에서 작업한 파일은 해당 세계에서만 볼 수 있다 (존재한다).

**두 세계 합치기** 

`git merge new_world ` 인수하는 곳(master)에서 new_ world를 합치겠다. 

-> new_world에만 존재했던 파일을 master에서도 볼 수 있다. 

**활용법**

원본을 무결하게 유지하기 위해 브랜칭을 쓴다. 

=> 원본은 master에 보관하고 브랜칭 하여 작업하다가, 

 작업물이 어느정도 완성되면 master에 merge하거나 /  

작업물이 맘에 안든다면 날려버리고 master의 무결한 원본을 다시 가져다가 쓴다. 



- `git branch ` 존재하는 브랜치 확인 
- `git branch -d new_world` 브랜치 삭제 
- branch 안에서는 `git push origin new_world` 으로 푸시해야한다. 

---



