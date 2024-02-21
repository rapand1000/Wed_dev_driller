from bottle import get, template
import x

##############################  
@get("/users")
def _():
    print("XXXXXXXXXXXX GET USERS start HER1 XXXX")
    try:
        db = x.db()
        sql = db.execute("SELECT * FROM users")
        users = sql.fetchall()
        return template("users", users=users)   
    except Exception as ex:
        print("XXXXXXXXXXXX GET USERS FAil XXXXX")
        print(ex)
        print("XXXXXXXXXXXX")
    finally:
        if "db" in locals(): db.close()
