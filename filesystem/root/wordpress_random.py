import os
import sqlite3
from sqlite3 import Error


update = {
    "blogname": os.environ.get("BLOGNAME", "Company Intranet"),
    "blogdescription": os.environ.get("BLOGDESCRIPTION", "Internal Coroporate Intranet"),
    "admin_email": os.environ.get("[[ADMINEMAIL]]", "info@wordpress.com")
}



def main():
    try:
        db_file = "/var/www/localhost/htdocs/wp-content/database/.ht.sqlite"
    except:
        db_file = "testing.ht.sqlite"

    # create a database connection
    conn = sqlite3.connect(db_file)
    with conn:
        # Update some fields
        # I dont care about SQLInjection here as you can get full shell easier than this

        cur = conn.cursor()
        for key, value in update.items():
            query = "UPDATE wp_options SET option_value = ? WHERE option_name = ?"
            cur.execute(query, (value, key))
        conn.commit()

if __name__ == '__main__':
    main()
