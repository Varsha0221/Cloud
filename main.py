from fastapi import fastAPI
app=fastAPI()
@app.get("/home")
def home():
    return{"success":True,"message":"Hello World!!!"}
@app.get("/about")
def about():
    return{"Name":"Varsha","Loaction":"Mumbai"}