import os
import psycopg2
from bottle import route, run

@route("/")
def hello_world():
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("SELECT * FROM mytable;")
        data = cur.fetchone()
        name1 = data[1]
        return "Hello World2!" + str(name1);

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
