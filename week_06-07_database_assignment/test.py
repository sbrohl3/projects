
from classes.database_access import DB_Connect
db_connection = DB_Connect("it412_sbrohl2", "Pr0grammingRul3s!", "it412_sbrohl2")

number = "1234567891"
number3 = "978-124513"
number2 = "1234567791"

## A query that selects all records in the library table
my_query_result = db_connection.executeSelectQuery("SELECT isbn FROM dbo.library_catalogue")
## Looping through all of the records in the library table

print(my_query_result)
for num in my_query_result:
    ## Checking to ensure a duplicate book is not added based on ISBN
    if number2 in num.isbn:
        print("You are attempting to add a duplicate entry! Discarding changes and returning to the main menu.")
        duplicates = True
        break

    else:
        duplicates = False

if duplicates == False:
    print("I think this will work ")
