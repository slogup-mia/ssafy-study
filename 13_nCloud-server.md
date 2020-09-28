# nCloud-server

서버구성 : https://youtu.be/TdLU504n3GA?t=608

## 공인 IP로 접속

- 공인 IP 생성
- 기본 루트 계정으로 접속 : `ssh root@49.50.173.134` 
  - 이때는 인증키 비밀번호가 필요하다

### 유저 추가

- 접속 후 유저( `swon`) 추가 : `adduser swon` , 패스워드 설정, 풀네임 설정
-  `ssh swon@49.50.173.134` 
  - 해당 유저의 비밀번호로 접속 가능 

### 유저에게 `sudo` 권한 부여

-  루트 계정으로 접속 : `ssh root@49.50.173.134` 

- `sudo vi /etc/sudoers`  권한 추가 , 비밀번호 인증 없이  sudo 명령 하도록 하기 `ALL=(ALL) NOPASSWD ALL`

  - ```bash
    root    ALL=(ALL:ALL) ALL
    swon    ALL=(ALL) NOPASSWD:ALL
    ```

  - 편집모드 벗어나서 저장 후 종료 : `exit` → `:w!` → `exit` → `:q!` 

## SSH키를 생성해서 접속하기

> - 공개키 - 비밀키가 쌍으로 만들어진다.
> - 비밀키는 내 PC에, 공개키는 서버에 저장
> - 패스워드보다 안전 

- `ssh-keygen` 후 엔터 

  - <img src='https://user-images.githubusercontent.com/45927473/93062896-7bce0e00-f6b0-11ea-8f16-e898f4fdc5df.png' width='500px'>

- ssh로 이동하면 공개키 `id_rsa.pub` 를 확인할 수 있다.

  - ```bash
    ➜  ~ cd .ssh
    ➜  .ssh ls
    id_rsa      id_rsa.pub  known_hosts 
    ```

-  `scp`라는 명령어로 공개키를 서버 원격지로 복사 

  - `scp id_rsa.pub swon@49.50.173.134:/home/swon`

  - ``` bash
    ➜  .ssh scp id_rsa.pub swon@49.50.173.134:/home/swon
    swon@49.50.173.134's password:
    id_rsa.pub                                                 100%  593   166.4KB/s   00:00
    ```

- 서버 접속 `ssh swon@49.50.173.134` 후 파일 확인하면 공인키 복사가 되어있다.

  - ``` bash
    swon@swon-todo:~$ ls
    id_rsa.pub
    swon@swon-todo:~$ cat id_rsa.pub
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQ... 
    ```

- `.ssh` 디렉토리 생성 후 공개키를 이동한다. `cat id_rsa.pub >> .ssh/authorized_keys`

  - ``` bash
    swon@swon-todo:~$ mkdir .ssh
    swon@swon-todo:~$ ls -al
    total 32
    drwxr-xr-x 4 swon swon 4096 Sep 14 17:57 .
    drwxr-xr-x 3 root root 4096 Sep 14 17:13 ..
    -rw-r--r-- 1 swon swon  220 Sep 14 17:13 .bash_logout
    -rw-r--r-- 1 swon swon 3771 Sep 14 17:13 .bashrc
    drwx------ 2 swon swon 4096 Sep 14 17:14 .cache
    -rw-r--r-- 1 swon swon  593 Sep 14 17:50 id_rsa.pub
    -rw-r--r-- 1 swon swon  655 Sep 14 17:13 .profile
    drwxrwxr-x 2 swon swon 4096 Sep 14 17:57 .ssh
    swon@swon-todo:~$ cat id_rsa.pub >> .ssh/authorized_keys
    ```

  - 서버를 나와서( `exit`) 다시 접속 할 때는 패스워드 없이 접속이 가능하다!

  

  

