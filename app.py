from flask import Flask,render_template,request

from utils import flipkartScrap,log
from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)

@app.route("/",methods=['POST','GET'])
@cross_origin()
def main():
    try:
        # URL="https://www.flipkart.com/"
        
        # flipkartScrap.FlipkartScrap.get_data(URL)
        return render_template('index.html')

    
    except Exception as e:
        return render_template('index.html')

@app.route("/review",methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")
            print(searchString)
        except Exception as e:
            log.get_log(str(e))
    else:
        return render_template('index.html')


if __name__=="__main__":
    # main()
    app.run(port=8000,debug=True,host="0.0.0.0")