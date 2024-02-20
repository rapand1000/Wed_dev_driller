from bottle import get, response, delete, request
import x
print("xxxxxxxxxxxxx  start delete user her 1")

##############################  
@delete("/user/<uuid>")
def _(uuid):
    
    try:

        user_name = request.query.get('user_name')

        db = x.db()
        sql = db.execute("DELETE FROM users WHERE user_pk = ?",(uuid,))
        
        
        db.commit()
        response.status = 303
        response.set_header("Location", "/users")
        # return f"""
        #     <template mix-target="#item_{uuid}" mix-replace>
        #         <div
        #             class="flex items-center justify-center bg-red-600 rounded-md text-white"
        #             mix-ttl="2000"
        #         >
        #             Item {user_name} was deleted
        #         </div>
        #     </template>  
        # """
       

    except Exception as ex:
        print(ex)
        print("error xxxxxxxxx Delete user exception xxxxxxxxxxxxxxxxxxxxx")
    finally:
        if "db" in locals(): db.close()
print("Delete user completed her")