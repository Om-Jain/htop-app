from flask import Flask
import getpass
import time
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name and username
    full_name = "Om Jain"  
    username = getpass.getuser()  

    # Server Time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    
    response = f"""
    <html>
        <head><title>HTop Endpoint</title></head>
        <body>
            <h1>HTop Output</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <pre><strong>TOP output:</strong>\n{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
