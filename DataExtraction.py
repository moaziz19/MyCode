#import libraries
import cx_oracle
import pandas as pd
#create connection
conn = cx_oracle.connect('HR/HR@//localhost:1521/orcl')
#run the sql database query
sql_query = pd.read_sql_query("select * from employees", conn)
#write the dataframe to a csv file
sql_query.to_csv (r'E:\output\employees_data.csv', index = False)