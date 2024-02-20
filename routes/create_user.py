from bottle import post, request
import x
import uuid

##############################
@post("/users")
def _():
    try:

        print("xxxxxxxxxxxxx  RETURN HER1")
        user_id = uuid.uuid4().hex
        user_name = request.forms.get("user_name")
        user_last_name = request.forms.get("user_last_name")
        print("xxxxxxxxxxxxx  RETURN HER11")

         # Design by contract between front and back-end
        # VALIDATION
        # x.validate_user_name()
        # x.validate_user_last_name()
        print("xxxxxxxxxxxxx  RETURN HER111")
        db =x.db()
        q = db.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)", (user_id, user_name, user_last_name,"0","0","0"))
        print("xxxxxxxxxxxxx  RETURN HER1111")

        db.commit()

        # Show Hi A Aa
        print("xxxxxxxxxxxxx  RETURN HER2")

        return f"""

      
        <template mix-target="#users" mix-top>
        <div>
            {user_id,user_name,user_last_name}
        </div>
        """
        print("xxxxxxxxxxxxx her test")
    except Exception as ex:
        print(ex)
        print("xxxxxxxxxxxxx her EX")

    finally:
        if "db" in locals(): 
            db.close()
print("xxxxxxxxxxxxx her test2222")






