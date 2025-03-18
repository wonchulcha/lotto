### 1. 사전 준비

##### 필요한 계정 및 도구
- [Git 설치](https://git-scm.com/downloads) 
- [GitHub](https://github.com/) 계정 (이메일, 사용자이름 기억)
- [Streamlit Cloud](https://streamlit.io/cloud) 계정


```bash
# git 설치 후 터미널 모드에서 확인
git --version

# git 과 github는 다르다!!
```



### 2. 로컬 git 과 GitHub 연결을 위한 사용자 등록
    도커와 도커허브가 생각나지 않으시나요?
    
##### 내 컴퓨터 터미널 에서 깃허브 사용자 등록 방법

    다른 이메일로 로그인 되어 있는 경우 기존 자격 제거 필수

    - 윈도우 검색창 입력 
    - 자격증명관리자 > windows 자격 증명 탭 > git 을 찾아 제거 




### 3. GitHub 저장소 생성

- GitHub 로그인
- <새 저장소 생성> 클릭
- <저장소 이름> 입력
- 공개(Public) 또는 비공개(Private)로 설정
- README 파일은 생성 X
- <저장소 생성> 클릭
- <코드> 버튼 클릭 후 저장소 주소 복사

### 4. 내 컴퓨터에서 GitHub 사용자 등록 방법

```bash
# 터미널 모드에서 현재 사용자 체크
git config user.name
git config user.email

# 사용자 등록
git config --global user.name "wonchulcha"
git config --global user.email "wonchulcha@gmail.com"
# 로그인창 팝업 후 인증 확인하면 완료 
```

#### 5. 내 컴퓨터(local)에서 git 저장소 만드는 방법

```bash
# Git 처음 시작 
# 현재 디렉토리에서 git 저장소 생성 
git init

# 프로젝트 디렉토리를 생성하고 git 저장소 생성 
git init <directory_name>

# .git 저장소 참고 
dir -force # 혹은 ls -force

# 내 branch 이름 확인
# 잠시 branch 개념: 
# root 와 branch의 branch 느낌보다는 커밋의 포인트임
# 즉 main도 하나의 branch가 될 수 있다.
git branch

# 원격지(remote)와 연결되어 있는지
git remote
git remote -v

# 원격 저장소 연결
git remote add origin <깃 주소>

# 파일 추가 및 커밋
git add .
git commit -m "Initial commit: Streamlit app setup"

# GitHub에 푸시
git push -u origin main  # 첫 push에서 충돌 문제 생기면 --force
```


### 6. 원격지(Github)에 있는 git을 로컬에서 처음 가져 올때

```bash
git clone <깃 주소>
```

## 6. Streamlit Cloud 설정

1. [Streamlit Cloud](https://streamlit.io/cloud)에 로그인합니다.
2. 우측 상단 <Create App> 버튼을 클릭합니다.
3. GitHub 계정을 연결하고 권한을 부여합니다 (이미 연결되어 있다면 이 단계는 건너뜁니다).
4. 방금 생성한 저장소를 선택합니다.
5. 다음 정보를 입력합니다:
   - Main file path: `app.py`
   - Python 버전: 3.9 또는 3.10 (권장)
   - 필요한 경우 "Advanced settings"에서 추가 설정을 구성할 수 있습니다 (환경 변수 등).
6. "Deploy" 버튼을 클릭합니다.

## 7. 앱 업데이트 프로세스

1. 로컬에서 코드를 수정합니다.
2. 변경사항을 커밋합니다:
```bash
git add .
git commit -m "앱 업데이트: 새로운 기능 추가"
git push
```
3. 변경사항은 자동으로 Streamlit Cloud에 배포됩니다.



