import os
import random

BLOGNAME = os.environ.get("BLOGNAME", "My first wordpress blog")
BLOGDESCRIPTION = os.environ.get("BLOGDESCRIPTION", "My first wordpress blog description")
ADMINEMAIL = os.environ.get("[[ADMINEMAIL]]", "info@wordpress.com")

print("Editing database file")
with open('database.sql', 'r', encoding="utf-8") as db_file:
    file_data = db_file.read()
    file_data = file_data.replace("[[BLOGNAME]]", BLOGNAME)
    file_data = file_data.replace("[[BLOGDESCRIPTION]]", BLOGDESCRIPTION)
    file_data = file_data.replace("[[ADMINEMAIL]]", ADMINEMAIL)

print("Writing new database file")
with open('database.sql','w', encoding="utf-8") as output_file:
    output_file.write(file_data)