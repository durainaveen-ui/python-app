from flask import Flask, jsonify
import datetime
import socket
	
# Create an instance of the Flask class
app = Flask(__name__)

# Use the route() decorator to tell Flask what URL should trigger the function
@app.route("/")
def hello_world():
    return jsonify({
   	'time':datetime.datetime.now().strftime("%I:%M:%S %p on %B %d, %Y"),
	'hostname':socket.gethostname()
	'message':"hello naveen 8"
    
    })

# This part allows running the script directly
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
