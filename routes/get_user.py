from bottle import get, template
import x
##############################  

@get("/user/<uuid>")
def get_user(uuid):
    print("XXXXXXXXXXXX GETTING 1 USER start HER1 XXXX")
    try:
        db = x.db()
        sql = db.execute("SELECT user_pk, user_name, user_lastname FROM users WHERE user_pk=?",(uuid,))
        user = sql.fetchone()
        print("xxxxxxxxxxxx User name is: ", user)
        if user:
            return template("user", user=user) 
        else:
            return "User not found"
        
    except Exception as ex:
        print("XXXXXXXXXXXX GETTING 1 USER  FAil XXXXX")
        print("Error fetching user:", ex)
        print("XXXXXXXXXXXX GETTING 1 USER  FAil XXXXX")
    finally:
        if "db" in locals(): db.close()








