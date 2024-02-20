from bottle import get, template
import x

##############################  
@get("/users")
def _():
    try:
        db = x.db()
        sql = db.execute("SELECT * FROM users")
        users = sql.fetchall()
        return template("users", users=users)   
    except Exception as ex:
        print("XXXXXXXXXXXX")
        print(ex)
        print("XXXXXXXXXXXX")
    finally:
        if "db" in locals(): db.close()
