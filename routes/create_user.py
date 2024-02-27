from bottle import post, request
import x
import uuid

##############################
@post("/users")
def _():
    try:
        print("xxxxxx create user start HER1")
        user_id =str(uuid.uuid4())
        user_name = request.forms.get("user_name")
        user_lastname = request.forms.get("user_lastname")
        # print("xxxxxx  RETURN HER11")


        # print("xxxxxx  RETURN HER111")
        db =x.db()
        q = db.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)", (user_id, user_name, user_lastname,"0","0","0"))
        # print("xxxxxx  RETURN HER1111")
         # Design by contract between front and back-end
        # VALIDATION
        # x.validate_user_name()
        # x.validate_user_lastname()
        db.commit()

        # Show Hi A Aa
        print("xxxxxx user commited HER2")

        return f"""
        <template mix-target="#users" mix-top>
            <a href=user/{user_id}
            class="relative flex flex-col items-center justify-center border border-black h-24 bg-white rounded-md mix-ttl="2"
            >
                <p class="text-center">
                    {user_name} {user_lastname}
                </p>
                <button class="delete-btn absolute bottom-1 right-1" mix-delete="/users/{user_id}?user_name={user_name}">🗑️</button>
            </a>
        </template>


        
        """
        # print("xxxxxxxxxxxxx her test")
    except Exception as ex:
        print("xxxxxxxxxxxxx create user her EXception")
        print(ex)
        print("xxxxxxxxxxxxx create user her EXception")

    finally:
        if "db" in locals(): 
            db.close()
            print("xxxxxx create user completed HER3")






