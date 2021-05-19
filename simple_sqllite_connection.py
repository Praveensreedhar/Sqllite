import sqlite
try:
  conn = sqlite3.connect('test1')
  print "Opened SQL DB";
except Exception as e:
  print("Error during connection :",str(e))
results = conn.execute("SELECT * FROM COMPANY")

for row in results:
  print row
  
conn.close()
  
