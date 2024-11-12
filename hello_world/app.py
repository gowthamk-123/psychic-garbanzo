from flask import Flask
import os
import time
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system info
    name = "Gowtham Ganeswaram"  # Replace with your full name
    
    # Attempt to get system username safely
    try:
        username = os.getlogin()  # This might fail in Codespaces
    except OSError:
        username = os.environ.get("USER", "Unknown")  # Fallback to environment variable if os.getlogin() fails
    
    # Handle server time in IST using pytz
    IST = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get top output safely
    top_output = ""
    try:
        top_output = "\n".join([str(proc.info) for proc in psutil.process_iter(['pid', 'name', 'username'])])
    except psutil.Error as e:
        top_output = f"Error retrieving processes: {e}"

    # Return HTML response
    return f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Info</h1>
            <p>Name: {name}</p>
            <p>Username: {username}</p>
            <p>Server Time (IST): {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Run the app on all available interfaces and port 5000
    app.run(host='0.0.0.0', port=8000)
