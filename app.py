from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Assalamu alaikum DevOps User"

if __name__ == "__main__":
    print("Bismillah: Starting Flask Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)