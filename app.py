from flask import Flask,render_template,request
from predict import *
app=Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/' , methods=['GET' , 'POST'])
def index():
    if request.method=='POST':
        wav_b64=request.get_data(as_text=True)
        result=predict(wav_b64[22:])

        print(result)
        print(MMD_scores)



    return render_template('index.html')

@app.route('/evaluate')
def evaluate():
    result=final_evaluate()
    return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)