from app import app

@app.route('/')
def home():
    return "Deploying Flask App at Vercel"
