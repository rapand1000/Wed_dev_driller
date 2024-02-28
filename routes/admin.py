from bottle import get, request, template, response
import x

@get("/admin")
def _():
    x.disable_cache() # browser do not remember this page < >
    name = request.get_cookie("name", secret="my_secret") ## her decoder den cookie secret
    if name:
        print("XXXXX  User acctepted by cookie  XXXXX")
        return template("admin", name=name)
    else:
        print("XXXXX  User not logged in  XXXXX")
        response.status = 303
        response.set_header("Location", "/login")
