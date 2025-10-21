# dbms_mysql_select.py
import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host='localhost',   # MySQL 서버 주소
    user='root', # MySQL 사용자명
    password='1234', # MySQL 비밀번호
    database='exampledb',    # 사용할 데이터베이스 명
    
)

# 커서 생성 => 명령어 작성
cursor = conn.cursor()

# 명령어 실행
sql = "select * from employees"
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees:
    print(employee)

print('데이터 조회 완료')
# 연결 해제
conn.close()
