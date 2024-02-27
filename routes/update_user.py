from bottle import put, request, response
import x

##############################
@put("/user/<id>")
def _(id):
    try:
        user_name = request.forms.get('user_name')
        db = x.db()
        q = db.execute("UPDATE FROM users WHERE item_id = ?", (id,))
        db.commit()
        return f"""
        <template mix-target="#item_{id}" mix-replace>
            <div class="bg-red-500" mix-ttl="2000">
                user  update
            </div>
        </template>
        """
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()