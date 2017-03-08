import media
import fresh_tomatoes
from flask import Flask, request

app = Flask(__name__)

# Check the user input is appropriate
# Maybe I can use HTML error code to indicate something wrong
# All four rows are required
@app.route('/getTest', methods=['POST'])
def getTest():
	print ("I got it")
	print (request.form)
	return request.form['MovieTitle']

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost', port=5004)