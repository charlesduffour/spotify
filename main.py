from flask import Flask
import threading
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Collector running OK", 200

# Ton collector en thread
def collector():
    print("Collector started...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    # Lancer le collector dans un thread
    t = threading.Thread(target=collector, daemon=True)
    t.start()

    # Lancer le serveur Flask que Fly attend
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
