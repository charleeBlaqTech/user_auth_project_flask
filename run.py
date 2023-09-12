from waitress import serve
from app import *



if __name__ == "__main__":
    # app.run(debug=True) 
    app.debug = True
    # app.run(host= "0.0.0.0", port= 5050)  this is for developent alone
    serve(app,host= "0.0.0.0", port= 5050) 