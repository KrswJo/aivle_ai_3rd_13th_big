import pandas as pd
import mysql.connector


csv_data = pd.read_csv('costco_price.csv', na_values=[''])  # 엑셀 파일 읽기

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='aivle',
    database='test'
)

# Cursor 생성
cursor = cnx.cursor()

# 테이블 삭제
cursor.execute("DROP TABLE IF EXISTS costco_price;")

create_table_sql = '''
CREATE TABLE costco_price (
    idx INT AUTO_INCREMENT PRIMARY KEY,
    names VARCHAR(255),
    price INT
);
'''


cursor.execute(create_table_sql)

# 데이터 삽입 SQL 및 실행
insert_data_sql = '''
INSERT INTO costco_price (names, price)
VALUES (%s, %s);
'''


for index, row in csv_data.iterrows():
    if pd.notna(row['names']) and pd.notna(row['price']):
        data = (row['names'], row['price'])
        cursor.execute(insert_data_sql, data)
    
    
# 변경 사항 저장
cnx.commit()

# 연결 및 커서 닫기
cursor.close()
cnx.close()