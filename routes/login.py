from bottle import post, response,template, get, request
import x

@post("/login")
def _():
    print("XXXXXXXXXXXXXXX  get data from login input   XXXXXXXXXXXXXXX")

    try:
        db = x.db()
        user_email = request.forms.get('user_email')
        user_password = request.forms.get('user_password')
        print("XXXXXXXXXXXXXXX  get data from login input   XXXXXXXXXXXXXXX")

        q = db.execute("SELECT * FROM users WHERE user_email = ? AND user_password = ?", (user_email, user_password))
        user = q.fetchone()
        print("XXXXXXXXXXXXXXX  User row in DB:  ",user,"  XXXXXXXXXXXXXXX")

        response.set_cookie("name",user['user_name'], secret="my_secret", httponly=True)
        # response.set_cookie("name",user['user_name'], secret="my_secret", httponly=True)
        return """
        <template mix-redirect="/admin">
        </template>
        """
        # return template("user", user=user)

    except Exception as ex:
        print(ex)
        print(type(ex))
        print(ex.args[0])
        print(ex.args[1]) # user_password xxxxx  user_email xxxxx

        if "user_password" in ex.args[1]:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">User password invalid</div>
            </template>
            """
        
        if "user_email" in ex.args[1]:
            return """
            <template mix-target="#error" mix-replace>
                <div id="error">User email invalid</div>
            </template>
            """
        
        return """
        <template mix-target="#error" mix-replace>
            <div id="error">System under maintainance</div>
        </template>
        """
    finally:
        if "db" in locals(): db.close()


    # try:
    #     # TODO: validate the email and password
    #     # validate password
    #     x.validate_user_email()
    #     x.validate_user_password()
    #     # TODO: Connect to the db and check that the email and password are correct
    #     # db.exceute(SELECT * FROM users WHERE user_email = ? AND user_password = ?, (email, password))
        
    #     response.set_cookie("name", "Santiago", secret="my_secret", httponly=True)
    #     return """
    #     <template mix-redirect="/admin">
    #     </template>
    #     """
    # except Exception as ex:
    #     print(ex)
    #     print(type(ex))
    #     print(ex.args[0])
    #     print(ex.args[1]) # user_password xxxxx  user_email xxxxx

    #     if "user_password" in ex.args[1]:
    #         return """
    #         <template mix-target="#error" mix-replace>
    #             <div id="error">User password invalid</div>
    #         </template>
    #         """
        
    #     if "user_email" in ex.args[1]:
    #         return """
    #         <template mix-target="#error" mix-replace>
    #             <div id="error">User email invalid</div>
    #         </template>
    #         """
        
    #     return """
    #     <template mix-target="#error" mix-replace>
    #         <div id="error">System under maintainance</div>
    #     </template>
    #     """

    # finally:
    #     pass





