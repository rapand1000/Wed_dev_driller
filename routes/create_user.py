from bottle import post, request
import x
import uuid

##############################
@post("/users")
def _():
    try:

        print("XXXXXXXXXXXXXXX create user start her")
        user_id =str(uuid.uuid4())
        user_name = request.forms.get("user_name")
        user_lastname = request.forms.get("user_lastname")
        # print("xxxxxxxxxxxxx  RETURN HER11")

         # Design by contract between front and back-end
        # VALIDATION
        # x.validate_user_name()
        # x.validate_user_last_name()
        # print("xxxxxxxxxxxxx  RETURN HER111")
        db =x.db()
        q = db.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)", (user_id, user_name, user_lastname,"0","0","0"))
        # print("xxxxxxxxxxxxx  RETURN HER1111")

        db.commit()

        # Show Hi A Aa
        # print("xxxxxxxxxxxxx  RETURN HER2")

        return f"""

      
        <template mix-target="#users" mix-top>
        <div>
            {user_id,user_name,user_lastname}
        </div>
        """
        # print("xxxxxxxxxxxxx her test")
    except Exception as ex:
        print(ex)
        print("xxxxxxxxxxxxx create user her EXception")

    finally:
        if "db" in locals(): 
            db.close()
# print("xxxxxxxxxxxxx her test2222")






