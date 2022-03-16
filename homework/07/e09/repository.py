""" 
Module that has functions related to reading
and saving to database.txt
"""

def read_database():
   """ 
   Makes database.txt readable string

   Parameters
   ----------
   db_string : `string`
      database.txt in string form

   Returns
   -------
   return : `string`
      returns database.txt in string form
   """
   db_string = open("database.txt", "r")
   return db_string.read()

def save_to_database(fname, lname):
   """ 
   Saves firstname(fname) and lastname(lname) to database.txt

   Parameters
   ----------
   f : `string`
      database.txt in string form
   x : `string`
      last line in database.txt
   id_number : `int`
      id number for the new saved name
   db_string : `string`
      database.txt in string form
   """
   f = open("database.txt", "r")
   for x in f:
      last_line=(x)
   id_number= int(last_line[0])+1
   db_string = open("database.txt", "a")
   db_string.write(f"\n{id_number},{fname},{lname}")