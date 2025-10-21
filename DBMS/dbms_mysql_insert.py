# dbms_mysql_insert.py
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
sql1 = """ 
insert into employees(id,name,deptID,managerID)
values(8,'kenneth',8,101);
"""
cursor.execute(sql1)
conn.commit()
print('데이터 조회 완료')
# 연결 해제
conn.close()


# 이렇게 써도 됨
# sql1 = """ 
# insert into employees(id,name,deptID,managerID)
# values(%s,%s,%s,%s);
# """

# cursor.execute(sql1, (8,'kenneth',8,101))