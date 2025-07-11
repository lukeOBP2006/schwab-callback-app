from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Schwab API Auth Callback Server is Running'

@app.route('/callback')
def callback():
    # Schwab will redirect the user here with ?code=...&state=...
    code = request.args.get('code')
    state = request.args.get('state')
    
    # Log the authorization code (you'd exchange this for a token next)
    return f"Authorization Code: {code}<br>State: {state}<br>You can now close this window."