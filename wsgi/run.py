from app import app
if __name__ == "__main__":
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(debug = True) #We will set debug false in production
