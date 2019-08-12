## SQL Database Assignment
## IT412
## 08/10/2019
## BROHL, STEVEN

from classes.database_access import DB_Connect

db_connection = DB_Connect("it412_sbrohl2", "*********", "it412_sbrohl2")

#db_connection.executeQuery("INSERT INTO dbo.Course_Info (course_discipline, course_number, course_title) VALUES ('IT', '410', 'Software Engineering'); COMMIT")

#db_connection.executeQuery("UPDATE dbo.Course_Info SET letter_grade='A-', course_gpa='3.7' WHERE course_id='1'; COMMIT")

my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.course_info")

for row in my_query_result:
    print(row.course_discipline)
    print(row.course_number)
    print(row.course_title)
    print(row.letter_grade)
    print(row.course_gpa)