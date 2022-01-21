## GIT 명령어

- **GIT** : add > commit > push



##### * 내 컴퓨터에서 최초로 `깃-깃허브` 매핑시켜줄때

* username, pw
* chrome
  * git / django, javascript, vue 

1. `git_config_--global_user.username_'<username>'` : username 등록

   * 확인하고싶을때 잘 들어갔는지?

     * `git config --global user.username`

       * ```
         window8397
         ```

2. `git config --global user.email '<email>'` : email등록

   * 확인하고 싶을때 잘 들어갔는지?

     * `git config --global user.email`

       * ```
         window8397@gmail.com
         ```



##### * Working Directory (내 로컬에서 폴더 만들었을 때만 ***1회***) 

* `git init` : git 시작
* `git remote add origin <git repo url>` : repo 연결

​	

##### Staging Area(.git) ***N회***

* `git remote`  : remote 별명확인
* `git remote -v` : remote 주소 확인

* `git add .` : `.` 전부다!!!! 
* `git add 파일명.확장자` : 특정 파일만 올려
* `git status` :  `add`가 잘 됐는지 확인
* `git commit -m '<commit message>'` :  why ? 에 대한 메시지
* `git push origin master` : github에 올려줘 !



### pull/clone

* `git clone origin master <git url>` : clone 은 당겨올때 사용



- `git log --oneline` : commit + 고유번호 7개 확인가능

- `git config --global core.autocrlf true` 

  : Mac이랑 안드로이드 중에 어떤걸 쓸거니 ? 둘다 !

  

---



### GIT BRANCH

- HOTFIX : 업로드 후 수정
- PUBLISH : 배포
- MASTER 
- DEVELOP
- FEATURE





---

