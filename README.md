![ㅍㅅㅌ](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/30f5226f-530f-4e13-b7a9-429faf020041)
## [🛒Go KarT: 창고형매장 자동결제 시스템](http://3.34.120.17:8000/ )
위의 링크를 클릭하시면 저희 서비스를 이용하실 수 있습니다.
>2023.05.29 ~ 2023.07.10 AI 빅프로젝트
-  창고형 매장에서 많은 물건을 결제할때 , 계산대에서 할애하는 시간을 줄이기 위해 고객이 직접 전체 물건을 카메라로 촬영하고 사진에서 보이는 상품을 AI 모델로 인식하고 인식한 상품들의 가격과 총액을 알려주고 고객이 바로 결제를 할 수 있는 프로세스를 제공하는 서비스입니다.
![소개_13조](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/788e79de-616a-4f00-9b92-6af92e553652)

## 목차

1. [조원소개](#조원소개)   

2. [배경 및 기대효과](#배경-및-기대효과)   

3. [주요 서비스 화면](#주요-서비스-화면)   

4. [Service Flow](#Service-Flow) 

5. [주요 서비스 내용](#주요-서비스-내용)

6. [서비스 사용 방법](#서비스-사용-방법)

7. [서비스 설치 방법](#서비스-설치-방법)


## 조원소개
AI 수도권 4반 13조
<details><summary>Backend
</summary>

*신동화, 정광근(조장), 정인환*
</details>
<details><summary>Frontend
</summary>

*조승우, 장지해*
</details>
<details><summary>AI
</summary>

*이영진, 김소망*
</details>

## 배경 및 기대효과
### 매장에서 상품 구매 및 결제
- 창고형 매장은 자주 이용하는 이용객보다는 한번에 많은 상품을 구매하는 이용객 다수 
- 기존의 방식은 계산대에 상품을 올리고 결제하는 시스템으로 장시간 소요되어 매장 혼잡
- 현재 아마존 고는 수백 대의 카메라와 마이크, 압력 센서들이 고객을 실시간으로 추적하여 무인 매장 운영, 고객이 바코드를 스캔하여 상품을 인식하는 카트 서비스(Dash Cart) 제공
- 하지만 사용자가 바코드를 스캔하여 상품을 인식해야 하는 번거로움과 인공지능 판독 이슈로 매장 내 수용 인원100여 명으로 제한
- 사용자의 이동경로를 추적하기 때문에 수집량이 매우 커서 대형 유통망에 확대 적용하기 어려움
- 이러한 한계점을 보완하여 AI 모델을 통한 객체 인식을 활용하므로 별도의 스캔 없이 자동 결제 가능하도록 창고형 매장을 대상으로 자동 결제 시스템 서비스제안

### 기대효과
- 창고형 매장에서 셀프계산대 시스템을 고안하여 고객의 만족도가 올라감. 자동 결제 시스템을 이보다 더 높게 고객의 이용 만족도를 높이고자 함 
- 실제로 일본의 한 매장은 셀프계산대 사용으로 매출이 5%가량 늘었으며 매장 개수 증가 확인 
- 전년 대비 55.8%로 증가한 무인 매장이 확대됨에 따라 이러한 매장에 레퍼런스 확장 가능 
- 최근 대형 마트는 무인 셀프계산대를 확장시키는 추세임. 아날로그 형태의 단순 반복 업무를 최소화해 남은 인력을 탄력적으로 운용하여 인건비 감축 효과 기대 
- 해당 서비스에는 센서가 아닌 이미지 딥러닝을 활용하기 때문에 타 기업과 달리 센서 비용 절감 가능 

## 주요 서비스 화면
-  실사용자들이 모바일에서도 사용하기 편리하도록 만들었습니다.
<details><summary>메인 페이지
</summary>

![메인](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/a59c233e-4bfe-438f-8b09-ce90ff5beea4)
</details>

<details><summary>로그인 페이지
</summary>

![로그인](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/239870db-358b-4762-b7c0-c9b5bd853633)
</details>

<details><summary>회원가입 페이지
</summary>

![회원가입](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/c93c293d-41fb-41ad-96c2-e9c415970a5f)
</details>

<details><summary>비밀번호 초기화 페이지
</summary>

![비밀번호 초기화](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/09407625-623c-42f9-ad67-5d48b5939718)
</details>

<details><summary>비밀번호 재생성 페이지
</summary>

![새로운비밀번호](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/8247bc07-d0dc-4d22-98d9-60e512cc4c20)
</details>

<details><summary>게시판 글쓰기 페이지
</summary>

![새글쓰기](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/d64162e4-1997-4302-8222-88ad20da6760)
</details>

<details><summary>게시판 글목록 페이지
</summary>

![글목록](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/2b5aad34-1d63-499b-9c3e-dbb13208a96a)
</details>

<details><summary>게시판 글세부 페이지
</summary>

![글자세히](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/9c769b60-cb6d-4ca4-87c1-55f53e1aa628)
</details>

<details><summary>상품 인식 페이지
</summary>

![사진찍기](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/91389132-99ea-444a-ad7a-f6d7ad80b257)
![사진 찍기 확인](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/0d5fae57-d6ab-463f-91a4-b30f10864311)
</details>

<details><summary>상품 인식 로딩 페이지
</summary>

![로딩](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/c83c8ef0-86b1-4d28-b4ec-3e44588ac0d9)
</details>

<details><summary>상품 인식 결과 페이지
</summary>

![상품 인식 내역](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/d1a0327d-11bb-491a-a287-18f8e9564e7f)
</details>

<details><summary>상품 인식 결제 완료 페이지
</summary>

![상품 인식 결제 완료](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/6f69ef9f-ea6b-448a-bc21-6eb789090589)
</details>

<details><summary>상품 인식 결제 실패 페이지
</summary>

![상품 인식 결제 실패](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/974faf3c-efe7-4c83-907e-7b27fb96dd75)
</details>

<details><summary>마이페이지
</summary>

![마이페이지](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/4aa3d8ef-904f-430d-9d34-7a00a6322733)
</details>

<details><summary>마이페이지 결제 내역 페이지
</summary>

![마이페이지 결제 내역](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/7d77452b-8d74-4e2d-90c4-e968bd4f9e25)
</details>

<details><summary>마이페이지 결제 내역 세부 페이지
</summary>

![마이페이지 결제 내역 세부](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/ea417e81-5d85-483e-8787-a8b4c860081c)
</details>

## Service Flow
![flow_chart](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/23bb7382-8d5b-47a8-adaa-229208615d3e)
## 주요 서비스 내용

### 회원관리
1. 회원가입 기능 
    - 회원번호, 카드 유효기간, 이메일, 비밀번호, 이름, 영문이름, 닉네임을 DB 상에 저장 
2. 인증/인가 기능 
    - 로그인한 회원만 상품 결제 및 커뮤니티 기능을 사용 가능 
    - 기술: 회원 정보 저장(MySQL) / 웹 서버(Django) 


### 커뮤니티 기능
1. 글쓰기 기능
    - 로그인한 회원만 게시글을 수정, 삭제, 작성 가능 
    - 로그인한 회원만 댓글 작성 및 삭제 가능 
2. 댓글 기능
    - 로그인한 회원만 상품 결제 및 커뮤니티 기능을 사용 가능 
    - 비회원의 경우 작성 불가 
    - 기술: 커뮤니티 정보 저장(MySQL) / 웹 서버(Django) 

### 매장에서 상품 구매 및 결제
1. 물건 구매 후 카메라로 셀프 결제 
    - 상품 가격 / 무게 / 물건의 유형을 인식 
    - 예상무게와 실측무게가 비슷 할 경우 결제 
    -  기술: Object Detection(YOLOv5) / 상품 가격 저장(MySQL)  / 웹 서버(Django)
## 서비스 사용 방법
https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/13422934-5614-453f-a7ab-ef058afa84bb
1. 먼저 회원가입을 하여 로그인을 합니다.(로그인을 하지 않으면 상품인식 페이지에 넘어갈 수 없습니다)
![처음](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/fc813927-ba77-48b4-8b9f-0b717b564ed1)


2. 상품인식 페이지에 들어가서  카트에 있는 상품들을 보이게 사진을 찍습니다.
![찐 사진 찍기](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/8e10fce0-dd3e-4074-84df-99788cdb0733)


3. 사진을 찍은 후 확인 버튼을 누르고 모델이 상품을 인식 할때까지 기다립니다.
![상품인식](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/c745a82d-d40b-4492-852d-8c209d210fe0)


4. 상품을 인식 한 후 해당 상품 내역과 함께 상품의 무게와 사용자의 정보를 넣은 QR을 보여줍니다.
![상품인식 결과](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/d6da19d2-6455-44e3-832a-d89c5bc19572)


5. 결제 라인을 지나가기 전 QR을 찍고 결제 라인을 지나면 결제 버튼을 누릅니다. 


6. 
- QR에서 인식된 무게와 결제 라인의 무게 센서를 통해 인식된 무게가 비슷하면 결제 완료 페이지가 나옵니다.
![결제 완료](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/33ec064a-52a3-494b-b82f-7e6e9715c28d)


-  QR에서 인식된 무게와 결제 라인의 무게 센서를 통해 인식된 무게가 다르다면 결제 실패 페이지가 나옵니다. 
![상품 인식 결제 실패](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/974faf3c-efe7-4c83-907e-7b27fb96dd75)


7. 결제가 성공한 후 , 마이페이지에 들어가 구매내역을 볼 수가 있습니다. 
![마이페이지](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/33bc245e-88de-4963-8dc3-8d8bbc8f9131)
![마이페이지 결제 내역](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/fd52bd27-6378-417d-ae82-dde0e0e6dd22)
![마이페이지 결제 내역 세부](https://github.com/KrswJo/aivle_ai_3rd_13th_big/assets/50902999/4ff25b55-ffe9-42bc-a293-b741098c1dd3)

## 서비스 설치 방법

1. mysql를 다운로드 받은 후 test라는 이름을 가진 DB를 생성합니다.

2. conda 환경설정 하신 후, git bash에 레포지토리를 Clone 하고 IDE에서 애플리케이션을 실행합니다.

```git
git clone https://github.com/AIVLE-School-Third-Big-Project/AI_4_13.git
```
3. conda 환경설정 터미널에서 애플리케이션 관련 라이브러리를 다운받습니다.

```cmd
pip install -r requirements.txt --no-cache-dir
```
4. conda 환경설정 터미널에서 마이그레이션을 만듭니다.

```cmd
python manage.py makemigrations
python manage.py makemigrations member
python manage.py makemigrations board
python manage.py makemigrations payment
```
5. conda 환경설정 터미널에서 3에서 만든 마이그레이션 파일을 기반으로 DB를 만듭니다.

```cmd
python manage.py migrate
```
6. 프로젝트 내의 products_price 폴더로 이동합니다.

```cmd
cd products_price
```
7. csv_to_mysql.py를 실행하여 상품정보가 있는 costco_price.csv파일을 DB에 추가합니다.

```cmd
python csv_to_mysql.py
```
8. 다시 프로젝트 폴더로 돌아가서 서버를 돌리기 위한 명령어를 입력합니다.

```cmd
cd ..
python manage.py runserver
```
