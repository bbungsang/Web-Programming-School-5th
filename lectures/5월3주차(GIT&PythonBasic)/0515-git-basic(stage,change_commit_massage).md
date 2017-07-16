## Git Stage

#### Tracked & Untrackde

- 워킹 디렉토리의 모든 파일은 `Tracked(관리 대상)`와 `Untracked(관리 대상이 아님)`로 나눈다.
- Untracked 파일은 워킹 디렉토리에 있는 파일 중 `Staging Area`에도 포함되지 않은 파일이다.

> 새로 생성된 파일: create.md <br>
수정된 파일 : modify.md

`git add -A` : 한 stage 안에 모두 tracking 된다.
```
git status
Initial commit
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file: create.md
    modified file: modify.md

```

`git rm --cached create.md` : 'create.md'가 해당 stage에서 분리
```
git status
Initial commit
Changes to be committed:
  new file: modify.md

Untracked files:
  create.md
```

#### Git 영역의 모든 파일을 stage 에 추가하기
- git add -A
- git add --all
- git add .

#### stage 에서 제외시키기(unstage)
- git reset HEAD <file-name>
- git rm --cached <file-name>

#### stage 영역의 파일 내용 확인하기
- `git diff --staged` commit 파일과 staged 파일의 변경된 내역을 알 수 있다.
- 단지 `git diff` 의 경우, staged 와 unstaged 된 영역의 파일만 비교하여 modified 된 부분을 보여준다.
- 초록색의 + 는 추가된 부분, 빨간색의 - 는 삭제된 부분이다.

#### commit 된 체크썸과 메세지 확인하기
- git log

#### 파일 무시하기 .gitignore 파일 설정법
- 프로젝트 관리시, 특정파일은 깃으로 관리할 필요가 없는 것들이 있다. 그런 파일들은 `git status`로 스테이지를 조회할 때 마다 매번 untracked 되어있거나 modified 되어있어서 진짜 필요한 정보를 보기 힘들게 될 수 있다.
- 이런 파일들을 git 시스템에서 무시하여 없는 파일처럼 만들 수 있다.

> 먼저 .gitignore을 만든다. <br>
편집기를 통해 무시할 확장명 또는 폴더명 등을 입력한다.

```txt
[터미널]
vim .gitignore

[vim]
*.log
*.class
.ipynb_checkpoints/
```

#### git add -A + commit -m "abc" 의 단축 명령어
- git commit -a -m "abc"

<br>
## Git Commit Message 수정
#### HEAD 커밋 메세지만 수정할 때
- `git commit --amend`

#### HEAD 이전 커밋 메세지 수정할 때(예: 3번째 전까지)
- `git rebase -i HEAD~3`
- 변경을 원하는 커밋을 pick 에서 edit 으로 수정

<br>
> **막간 Tip (ㆁωㆁ*)** <br><br>
echo 'show me the money' > abc.txt
- show me the money 의 문구가 담긴 abc 텍스트 파일을 생성한다.

> alias <단축 명령어 지정> <원래 실행 가능한 명령어>
- vi ~/.zshrc 에 등록하면 z-shell 에서 간단한 단어로 명령어를 실행할 수 있다.

> mv abc.txt cba.txt
- 파일 이름 변경하기, abc.txt 를 cba.txt 로 변경

> mv cba.txt ../
- cba.txt 가 상위폴더로 이동
