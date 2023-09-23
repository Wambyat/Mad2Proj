import sqlite3
from celery import Celery
app = Celery('celSQL', broker = "redis://localhost:6379/0", backend = "redis://localhost:6379/0")

@app.task
def cSQL(query):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query)
    output = c.fetchall()
    conn.commit()
    conn.close()
    return output