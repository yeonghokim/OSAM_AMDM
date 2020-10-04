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

# AMDMServer
### IoT장비 데이터 교환
* 데이터 수신 형태 `IoT -> Server`
  * **type** : 기기의 형태
  * **id** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **Lock** : 현재 기기의 잠금 유무
  * **PhoneLock** : 기기안의 핸드폰의 잠금 상태
```json
{
        "type": "IoT",
        "id": 1234567,
        "Lock": 0,
        "PhoneLock": {
                "19-760730001": 0,
                "19-760730002": 0,
                "19-760730003": 1,
                "19-760730004": 0
        }
}
```
* 데이터 송신 형태 `Server -> IoT` 
  * **ForceLock** : 현재 기기의 강제 잠금 유무
  * **PhoneLock** : 기기안의 핸드폰의 강제 잠금 유무
  * **PhoneUnLock** : 기기안의 핸드폰의 강제 잠금 유무
```json
{
        "ForceLock": 0,
        "PhoneLock": {
                "19-760730003": 1
        }
        "PhoneUnLock": {
                "19-760730004": 0,
        }
}
```
### Android 데이터 교환
* 데이터 수신 형태 Type1 `Android -> Server` 
  * **type** : 기기의 형태
  * **requestType**: 요청 타입
  * **id** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **lock** : 현재 기기의 잠금 유무
  * **lockTime** : 기기의 잠금 시간
```json
{
        "type": "Android",
        "requestType": 1,
        "id": 1234567,
        "Lock": 1,
        "Time": "20201004_13:49:12"
}
```
* 데이터 수신 형태 Type2 `Android -> Server`
  * **type** : 기기의 형태
  * **requestType**: 요청 타입
  * **id** : 기기의 아이디(초기 설정때 서버에서 지급)
  * **turnOnTime** : 기기가 켜진 시간
```json
{
        "type": "Android",
        "requestType": 2,
        "id": 1234567,
        "turnOnTime": "20201004_13:49:12"
}
```
사이클
1. 서버 대기상태

- 데이터를 받음 
 (1) DB 처리를 함
 (2) 다시 기기로 데이터 전송

- 데이터 요청
 (1) DB 처리를 함
 (2) 다시 기기로 데이터 전송

2. 다시 대기 상태

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
### Phone Table
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
PHONE_PR | INTEGER | PRIMARY
USER_UNIQUENUM | INTEGER | X
PHONE_IP | CHAR | X
IS_LOCK | INTEGER | X
### PhoneCase Table
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
PHONECASE_PR | INTEGER | PRIMARY
IS_LOCK | INTEGER | X
PHONE1_ID | INTEGER | O
PHONE2_ID | INTEGER | O
PHONE3_ID | INTEGER | O 
PHONE4_ID | INTEGER | O
### LockManage Table
칼럼이름 | 타입 | 널 유무  | 외래키 유무
-------- | -------- | ---------- | ----------
LOCKMANAGE_PR | INTEGER | PRIMARY
PHONE_UNIQUENUM | INTEGER | X
MANAGETIME | DATETIME | X
IS_LOCK | INTEGER | X