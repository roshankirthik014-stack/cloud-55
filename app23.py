from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():

   return """
   <html>  
  <body>  
  <h1>paas engine</h1>  
  <p>python,flask</p>  
  </body>  
  </html>  
  """  
if ___name__ == "___main__":  
 app.run()
