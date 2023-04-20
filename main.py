from fastapi import FastAPI
import psycopg2

app=FastAPI()
@app.get("/read")
async def read_data():
    con = psycopg2.connect(database="postgres", user="postgres", password="Feb@2018",host="localhost",port=5432)
    cur=con.cursor()
    cur.execute("SELECT a1 FROM public.test")
    w1=cur.fetchall()
    
    cur.close()
    con.close()

    return w1