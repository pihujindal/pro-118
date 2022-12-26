from flask import Flask , render_template , request , jsonify
import prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# api listening to POST requests and predicting sentiments
@app.route('/predict' , methods = ['POST'])
def predict():

    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Empty Review'}
    
    else:

        # calling the predict method from prediction.py module
        sentiment , path = prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Got it',
                    'sentiment' : sentiment,
                    'path' : path}

    return jsonify(response)


# Creating an API to save the review, user clicks on the Save button
@app.route('/save' , methods = ['POST'])
def save():

    date = request.json.get("date")
    emotion = request.json.get("emotion")
    save_text = request.json.get("text")
    save_text = save_text.replace("\n", " ")
    # CSV Entry 
    entry = f'"{date}","{save_text}","{emotion}"\n'
    with open("C:/Users/Sakshi/Desktop/python/pro-118/static/assets/datafiles/updated_product_dataset.csv", "a") as f:
        f.write(entry)
    return jsonify({'status' : 'success' , 'message' : 'Data Logged'}
)


if __name__  ==  "__main__":
    app.run(debug = True)