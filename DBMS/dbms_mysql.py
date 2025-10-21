import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host='localhost',   # MySQL 서버 주소
    user='root', # MySQL 사용자명
    password='1234', # MySQL 비밀번호
    database='exampledb',    # 사용할 데이터베이스 명
    charset='utf8mb4',   # utf-8의 확장 버전
    cursorclass=pymysql.cursors.DictCursor
)

# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("select database()")
# 한번 호출에 하나의 Row(행)를 가져올 때 사용
print("현재 데이터베이스: ", cursor.fetchone())
# print("현재 데이터베이스: ", cursor.fetchall())
# print("현재 데이터베이스: ", cursor.fetchmany(2))

# 연결 해제
conn.close()