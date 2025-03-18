### 깃허브 사용자 등록



### 내 컴퓨터 cmd나 powershell에서 깃허브 원격 사용자 등록 방법

혹시 이미 다른 이메일로 로그인 되어 있는 경우는 기존 자격을 제거해야 한다.

- 윈도우 검색창 입력 : 자격증명관리자 > windows 자격 증명 탭 > git 을 찾아 제거 
- 처음 등록 하는 경우는 아래 처럼 바로 등록하면 된다.

### 등록 방법
```shell
git config user.name
git config user.email
# 위 명령어로 현재 사용자를 알수 있다.

git config --global user.name "wonchulcha"
git config --global user.email "wonchulcha@gmail.com"
```

두번째 명령 후 팝업 로그인창이 뜨고 클릭하면 등록된다.





