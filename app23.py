from flask import Flask
app = Flask(___name___)
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
