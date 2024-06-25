import psycopg2 

# provide database details for connection
conn = psycopg2.connect(database="ECOMMERCE_DATABASE", 
                        user='postgres', password='password',  
                        host='127.0.0.1', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 

# table creation using csv column headers
sql = '''CREATE TABLE PET_SUPPLIES(title varchar(500),
averageStar float,
quantity int NOT NULL,
tradeAmount varchar(30), wishedCount int NOT NULL);'''

# sql = '''DROP TABLE PET_SUPPLIES;'''

cursor.execute(sql) 

# copy csv into table  
sql2 = '''COPY PET_SUPPLIES(title,averageStar,
quantity,tradeAmount,wishedCount) 
FROM 'C:/Users/joann/OneDrive/Desktop/projects/js-react/aliexpress_pet_supplies.csv' 
DELIMITER ',' 
CSV HEADER;'''
  
cursor.execute(sql2) 

# add new column "animal" as text array 
sql3 = '''ALTER TABLE PET_SUPPLIES
ADD COLUMN animal text[];'''
  
cursor.execute(sql3)

# update animal column based on the keywords in title
sql4 = '''UPDATE PET_SUPPLIES
SET animal = CASE
    WHEN title ILIKE '%dog%' AND title ILIKE '%cat%' THEN ARRAY['cat', 'dog']
    WHEN title ILIKE '%dog%' THEN ARRAY['dog']
    WHEN title ILIKE '%cat%' THEN ARRAY['cat']
    ELSE ARRAY['other']
END;'''
  
cursor.execute(sql4)

# display table details once complete  
sql5 = '''SELECT * FROM PET_SUPPLIES;'''
cursor.execute(sql5) 
for i in cursor.fetchall(): 
    print(i) 
  
conn.commit() 
conn.close() 