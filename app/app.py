from datetime import datetime, timedelta

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now() + timedelta(hours=3)
    current_time = now.strftime("%H:%M:%S")
    return f'''
        <html>
            <head>
                <title>Current Time</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        font-size: 24px;
                        color: #333;
                        background-color: #f8f8f8;
                        margin: 0;
                        padding: 0;
                    }}

                    h1 {{
                        text-align: center;
                        margin-top: 50px;
                    }}

                    p {{
                        text-align: center;
                        font-size: 48px;
                        margin-top: 50px;
                    }}
                </style>
            </head>
            <body>
                <h1>Current Time</h1>
                <p>{current_time}</p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
