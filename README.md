# AMDM
💙 ☁️ 👍 🔥 🙌

# IoT
1. RFID 태그
2. 보관함 문이 열림(모터 작동)
3. 보관함 휴대폰 넣음
4. 센서 확인 후 (5초,10초 사이) 
5-1. (O) 문 닫힘
5-2. (X)
6. DB로 TCP 전송 

- 보관함별로 어떤기기가 사용 될 건지(이건 관리자 용)
- 최대한 비용감소 측면으로 발전 가능성 증가된다

# Android
### 화면 리스트
* 로그인 전 메인페이지
* 회원가입 페이지
* 로그인 페이지
* 병사 메인페이지
  * 반납 페이지
  * 통계 페이지
* 간부 메인페이지
* 관리자 메인페이지(많음)



# Server
python으로 이루어진 TCP 소켓 서버입니다.
## IoT장비 데이터 교환
### 데이터 수신 형태 `IoT -> Server`
  * **Type** : 기기의 형태
  * **ID** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **Lock** : 현재 기기의 잠금 유무
  * **PhoneLock** : 기기안의 핸드폰의 잠금 상태
```json
{
        "Type": "IoT",
        "ID": 1234567,
        "Lock": 0,
        "PhoneLock": {
                "19-760730001": 0,
                "19-760730002": 0,
                "19-760730003": 1,
                "19-760730004": 0
        }
}
```
### 데이터 송신 형태 `Server -> IoT` 
  * **ForceLock** : 현재 기기의 강제 잠금 유무
  * **PhoneLock** : 기기안의 핸드폰의 강제 잠금 유무
  * **PhoneUnLock** : 기기안의 핸드폰의 강제 잠금 유무
```json
{
        "ForceLock": 0,
        "PhoneLock": {
                "19-760730003": 1
        },
        "PhoneUnLock": {
                "19-760730004": 0
        }
}
```
## Android 데이터 교환
### 데이터 수신 형태 Type1 `Android -> Server` 
  * **Type** : 기기의 형태
  * **RequestType**: 요청 타입
  * **ID** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **Lock** : 현재 기기의 잠금 유무
  * **Time** : 기기의 잠금 시간
```json
{
        "Type": "Android",
        "RequestType": 1,
        "ID": 1234567,
        "Lock": 1,
        "Time": "2020-10-04 13:49:12"
}
```
### 데이터 수신 형태 Type2 `Android -> Server`
  * **Type** : 기기의 형태
  * **RequestType**: 요청 타입
  * **ID** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **IoTID** : IoT기기의 아이디
  * **Lock** : 잠글지 열지
  * **Time** : 요청 시간
```json
{
        "Type": "Android",
        "RequestType": 2,
        "ID": 1234567,
        "IoTID" : 123,
        "Lock" : 1,
        "Time": "2020-10-04 13:49:12"
}
```
### 데이터 수신 형태 Type3 `Android -> Server`
  * **Type** : 기기의 형태
  * **RequestType**: 요청 타입
  * **ID** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **TurnOnTime** : 기기가 켜진 시간
```json
{
        "Type": "Android",
        "RequestType": 3,
        "ID": 1234567,
        "TurnOnTime": "2020-10-04 13:49:12"
}
```
# DataBase (SQLite)
### User Table
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
USER_PR | INTEGER | PRIMARY | 
USER_ARMYNUMBER | CHAR | X
USER_NAME | CHAR | X
PASSWORD | CHAR | X
USER_DISCHARGEDATE | DATETIME | O 
UPDATEDATE | DATETIME | X
### Phone TableW
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
PHONE_PR | INTEGER | PRIMARY
USER_UNIQUENUM | INTEGER | X | USER.USER_PR
PHONE_IP | CHAR | X
IS_LOCK | INTEGER | X
### PhoneCase Table
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
PHONECASE_PR | INTEGER | PRIMARY
IS_LOCK | INTEGER | X
PHONE1_ID | INTEGER | O | PHONE.PHONE_PR
PHONE2_ID | INTEGER | O | PHONE.PHONE_PR
PHONE3_ID | INTEGER | O | PHONE.PHONE_PR
PHONE4_ID | INTEGER | O | PHONE.PHONE_PR
### LockManage Table
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
LOCKMANAGE_PR | INTEGER | PRIMARY
PHONE_UNIQUENUM | INTEGER | X | PHONE.PHONE_PR
MANAGETIME | DATETIME | X
IS_LOCK | INTEGER | X