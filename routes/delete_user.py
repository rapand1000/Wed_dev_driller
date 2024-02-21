from bottle import get, response, delete, request
import x


##############################  
@delete("/users/<uuid>")
def _(uuid):
    print("xxxxxx file loaded - delete user HER1 xxxxxx ")
    try:

        user_name = request.query.get('user_name')

        db = x.db()
        sql = db.execute("DELETE FROM users WHERE user_pk = ?",(uuid,))
        
        
        db.commit()
        print("xxxxxx Start delete user COMMITED HER2 xxxxxx ")
        # response.status = 303
        # response.set_header("Location", "/users")
        return f"""
            <template mix-target="#user_{uuid}" mix-replace>
                <div
                    class="flex items-center justify-center bg-red-600 rounded-md text-white"
                    mix-ttl="2000"
                >
                    User {user_name} was deleted
                </div>
            </template>  
        """
       

    except Exception as ex:
        print(ex)
        print("error xxxxxxxxx Delete user exception xxxxxxxxxxxxxxxxxxxxx")
    finally:
        if "db" in locals(): db.close()
        print("xxxxxx Delete user completed HER3")