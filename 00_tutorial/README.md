### 헤딩 (Heading)

* `#` 개수에 따라서 제목의 중요도가 달라진다
* h1~ h6

# h1

## h2

### h3

#### h4

##### h5

###### h6

---



### 리스트(List)

#### 순서가 있는 리스트

* `1.` 후에 `스페이스 바` 를 하면 자동적으로 생성이된다.
  * 

1. 리스트1
2. 리스트2
3. 리스트3

#### 순서가 없는 리스트

* 리스트A
  * 리스트 A-1
    * 리스트 A-1-가
* 리스트B

1. 리스트a
2. 리스트b
   1. 리스트b-1
      1. 리스트b-1-가


---

### 코드블럭(code block)

1. 코드박스

   * "`" (백킷) 세번 입력 후 엔터

     * ```
       
       ```

   * 내가 원하는 언어로 설정이 가능하다!!

   ```python
   lang = 'python'
   ```

   

2. 인라인코드

   * "`" (백킷) 안에 코드/문서 내용을 작성해준다
     * `printf('이승현')` -> `print('이승현')`

---

### 링크(link)

* `[string](url)` : string을 클릭하면 url로간다!
  * 해당 링크로 건너가기 위해서는 `ctrl`누른 상태로 `url`을 클릭한다
    * [google](https://google.com)
    * [삼성](https://samsung.com)

---

### 이미지(image)

* `![string](url)` : string이름의 url 경로 이미지가 나타난다!!
  * 

![아이유(IU) 공식 트위터 (@_IUofficial) | Twitter](https://pbs.twimg.com/profile_images/1374979417915547648/vKspl9Et_400x400.jpg)



![이지금](../../../How_To_GIt/이지금.jpg)

![이지금](../../../How_To_GIt/README.assets/이지금.jpg)

---



### 텍스트 강조(Text Emphasis)

* 굵게:
  * `*`/`_`를 텍스트 앞뒤에 2개씩 씌어준다
    * **이승현**

* 기울임 
  * `*`/`_`를 텍스트 앞뒤에 1개씩 씌어준다
    * *이승현*
    * **이승현*
* 취소선
  * ~~이승현~~

​	***이승현***



---



### 수평선 (horizontal line)

* `-`/`_`  을 3개 입력한다
* `<hr>` 을 입력한다.



---



### 인용문 (Blockquotes)

* `>` 하고 `enter`
  * 1개 입력하면 인용 인덴트 1칸
  * 2개 입력하면 인용 인덴트 2칸



---



### 표 (Table)

|      |      |
| ---- | ---- |

- `| | |`

---





## CLI 기초

`_` : 스페이스바

`<string>`: 내용 적기

`폴더/파일 이름을 입력할때는 대소문자 구분x`

* `pwd` : 현재 경로 확인
* `ls` : 내 경로에 어떤 파일, 폴더가 있는지 확인
* `cd_<path>` :  `<path>`로 이동
  * `/` 경로를 구분해준다.
    * A/B/C
* `cd_..` : 상위폴더로 이동
* `mkdir_<folder_name>` : 폴더 생성
* `touch_<file_name>` : 파일 생성
* `vi_<file_name>` :  파일 수정
  * 존재하는 파일 이름 - > 수정
  * 존재하지 않는 파일 이름 -> 생성 + 수정
    * 문서를 작성하고 싶으면 `i` 
    * 문서를 저장하고 싶으면 `esc` + `:` + `wq`
* `rm_<filename>` : 파일 삭제
* `rm_-r_<foldername>`: 폴더삭제 
* `mv <file_name_1> <file_name_2>` : 파일 이름 변경
* `mv <file_name> <folder_name>` : 폴더로 이동



---



## GIT 명령어.ZIP

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
* `git commit -m '<commit message>'` :  why 를 적어주
* `git push origin master` : github에 올려줘~~~



### pull/clone

* `git clone origin master <git url>` : clone 은 당겨올때 사용



- `git log --oneline` : commit + 고유번호 7개 확인가능



---



### GIT BRANCH



#### HOTFIX

: 업로드 후 수정

#### PUBLISH

 : 배포

#### MASTER 

#### DEVELOP

#### FEATURE



---





