from bottle import put, request, response,redirect
import x

##############################
@put("/users/<id>")
def _(id):
    print("XXXXXXXXXXXXXXX  Update of user HER1   XXXXXXXXXXXXXXX")

    try:
        user_name = request.forms.get('user_name')
        user_lastname = request.forms.get('user_lastname')
        db = x.db()
        q = db.execute("UPDATE users SET user_name = ?, user_lastname = ? WHERE user_pk = ?", (user_name, user_lastname, id,))
        db.commit()
        redirect("/users")
    
    except Exception as ex:
        print(ex)
        print("XXXXXXXXXXXXXXX  Update EX",ex,"    XXXXXXXXXXXXXXX")
    finally:
        if "db" in locals(): db.close()