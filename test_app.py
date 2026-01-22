from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
return "<h1>Platform as a Service using Azure App Service</h1><p>App deployed successfully!</p>"
if __name__ == "__main__":
app.run()