def read_database():
   db_string = open("database.txt", "r")
   content = db_string.read()
   db_string.close()
   return content

def save_to_database(fname, lname):
   f = open("database.txt", "r")
   for x in f:
      last_line=(x)
   id_number= int(last_line[0])+1
   db_string = open("database.txt", "a")
   db_string.write(f"\n{id_number},{fname},{lname}")
   db_string.close()