
def read_database():
   db_string = open("database.txt", "r")
   return db_string.read()

print(read_database())