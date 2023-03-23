from flask import Flask, request, jsonify, render_template
from func import compile_javascript
from db import *
import datetime
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():
    all_js_files = compile_javascript()
    conn = create_conn('servers.db')
    srvs_asc = get_servers_asc(conn)
    srvs_desc = get_servers_desc(conn)
    return render_template("home.html", srvs_asc=srvs_asc, srvs_desc=srvs_desc, js_files = all_js_files)


@app.route('/set/<ip>', methods=['POST'])
def set_time(ip):
    print(request)
    content = request.json
    print(content)
    time = content['time']
    conn = create_conn('servers.db')
    create_tbl(conn)
    inOrup(conn, ip, time)
    conn.close()
    return jsonify(dict(ip=ip))

@app.route('/get/', methods=['POST'])
def get_time():
    content = request.json
    ip = content['ip']
    conn = create_conn('servers.db')
    time = selectSp(conn, ip)
    conn.close()
    return jsonify(dict(ip=ip, time=time))


@app.route('/getAll/', methods=['GET'])
def get_all():
    conn = create_conn('servers.db')
    # data = select(conn)
    data = get_servers(conn)
    conn.close()
    return jsonify(dict(data=data))


if __name__ =='__main__':  
    app.run(debug = True)
