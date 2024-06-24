import psycopg2 
  
conn = psycopg2.connect(database="ECOMMERCE_DATABASE", 
                        user='postgres', password='password',  
                        host='127.0.0.1', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 
  
sql = '''CREATE TABLE PET_SUPPLIES(title varchar(500),
averageStar float,
quantity int NOT NULL,
tradeAmount varchar(30), wishedCount int NOT NULL);'''

# sql = '''DROP TABLE PET_SUPPLIES;'''

cursor.execute(sql) 
  
sql2 = '''COPY PET_SUPPLIES(title,averageStar,
quantity,tradeAmount,wishedCount) 
FROM 'C:/Users/joann/OneDrive/Desktop/projects/js-react/aliexpress_pet_supplies.csv' 
DELIMITER ',' 
CSV HEADER;'''
  
cursor.execute(sql2) 
  
sql3 = '''SELECT * FROM PET_SUPPLIES;'''
cursor.execute(sql3) 
for i in cursor.fetchall(): 
    print(i) 
  
conn.commit() 
conn.close() 