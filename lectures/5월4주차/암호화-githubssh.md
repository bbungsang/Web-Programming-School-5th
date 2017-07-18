## 공개키 암호 방식
- 각 사용자는 두 개의 키를 부여 받는다. 그 하나는 공개되고(공개키), 다른 하나는 사용자에 의해 비밀리에 관리되어야 한다(비밀키).
- 암호화/복호화 시스템은 두 키가 짝으로 동작하기 때문에, 비밀키로 암호화 하고 공개키로 복호화 할 수도 있다. 반대로 공개키로 암호화 했을 경우, 비밀키로 복호화 할 수도 있다.

## SSH Key가 동작하는 방식
- 공개키는 리모트 머신에 위치해야 한다. (로컬 머신은 SSH Client, 원격 머신은 SSH Server가 설치된 컴퓨터를 의미)
- SSH 접속을 시도하면 SSH Client가 로컬 머신의 비공개키와 원격 머신의 비공개키를 비교해서 둘이 일치하는 지를 확인한다.

## SSH Key 만들기
[터미널] <br>
1. 홈 디렉토리에서 `.ssh` 폴더로 이동 (없다면 생성하자 : `mkdir -p ~/.ssh`) <br>
2. .ssh/ 에서 `ssh-keygen -t rsa -b 4096 -C "bbungsang@gmail.com"` ➜ id_rsa 와 id_rsa.pub 의 두 파일이 생성된 것을 확인할 수 있다. <br>
3. `cat id_rsa.pub` 을 입력하면, ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC5hzEJVVCi3g9O91Ft95ipV2HA5fWkuUvz [...] 형태의 공개키를 확인하자.
<br>
[깃헙] <br>
1. GitHub settings ➜ [Personal settings]SSH and GPG keys ➜ New SSH Key 버튼을 클릭한다. <br>
2. 임의의 title 을 입력하고 터미널을 통해 얻은 공개키를 Key 입력란에 기입한다. <br>
3. 이제 https 프로토콜이 아닌 ssh 프로토콜을 이용하여 remote add 를 하면된다. <br>
4. git remote -v 를 입력하면 ssh 형태의 remote 주소를 확인할 수 있다. <br> 
origin git@github.com:\[...] (fetch) <br>
origin git@github.com:\[...] (push)