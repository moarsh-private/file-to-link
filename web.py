from flask import Flask,send_file
import os
app = Flask(__name__)

if not os.path.exists("files"):
    os.mkdir("files")
mime_type = {
    "png":"image/png",
    "jpg":"image/jpg",
    "jpeg":"image/jpeg",
}



@app.route("/<file>")
def home(file):
    if os.path.exists(f"files/{file}"):
        return send_file(f"files/{file}")
    else:
        return "File Not Found"

if __name__ == "__main__":
    port = os.environ.get("PORT",5000)
    app.run(host="0.0.0.0",port=port)





