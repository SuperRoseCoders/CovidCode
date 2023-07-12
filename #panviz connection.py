#panviz connection
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    database="panviz", user= 'panviz_readonly', password= 'T3u&c7U58V9H', host='pixel.ourcloud.ou.edu', port='5432'
)

conn.autocommit = True

cursor = conn.cursor()

cursor.execute('''SELECT * from public.country_death_positive_cases''')

colnames = [desc[0] for desc in cursor.description]

result = cursor.fetchall()

df=pd.DataFrame(result)
df.columns=colnames
print(df)
#testing1
conn.close()