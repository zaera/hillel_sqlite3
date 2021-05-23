from flask import Flask, request, Response
import re

app = Flask("CRUD_punishman")

@app.route('/create')
def create_phones():
    query_params = request.args
    phone_number = query_params.get('phone') or ''
    import sqlite3
    con = sqlite3.connect("./db.db")
    cur = con.cursor()
    sql = f"INSERT INTO phones values(null, '{phone_number}')"
    cur.execute(sql)
    con.commit()
    con.close()
    return "Phone number is added"

@app.route('/read')
def read_phones():
    import sqlite3
    con = sqlite3.connect("./db.db")
    cur = con.cursor()
    cur.execute("select value from 'phones'")
    all_phones = ""
    phone_list = cur.fetchall()
    for phone in phone_list:
        all_phones += "+" + str(phone) + '<br>'
    con.close()
    all_phones = re.sub('[()\',]', '', all_phones)
    return Response(all_phones)

@app.route('/update')
def update_phones():
    query_params = request.args
    phone_number1 = query_params.get('phone') or ''
    phone_number2 = query_params.get('to') or ''
    import sqlite3
    con = sqlite3.connect("./db.db")
    cur = con.cursor()
    sql = f"UPDATE phones SET value = '{phone_number2}' WHERE value = '{phone_number1}';"
    cur.execute(sql)
    con.commit()
    con.close()
    return "Old phone(s) were updated"

@app.route('/deleteall')
def deleteall_phones():
    import sqlite3
    con = sqlite3.connect("./db.db")
    cur = con.cursor()
    sql = "DELETE FROM phones"
    cur.execute(sql)
    con.commit()
    con.close()
    return "All phones were deleted"

@app.route('/deletesingle')
def deletesingle_phones():
    query_params = request.args
    phone_number = query_params.get('phone') or ''
    import sqlite3
    con = sqlite3.connect("./db.db")
    cur = con.cursor()
    sql = f"DELETE FROM phones WHERE value='{phone_number}';"
    cur.execute(sql)
    con.commit()
    con.close()
    return f"Phone {phone_number} was deleted"

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port='5000', debug=True)