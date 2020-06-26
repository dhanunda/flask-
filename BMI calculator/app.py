from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def welcome():
	bmi=''
	if request.method=='POST' and 'weight' in  request.form:
		height=float(request.form.get('height'))
		weight=float(request.form.get('weight'))
		bmi=cal_bmi(height,weight)
	return render_template('index.html',bmi=bmi)
def cal_bmi(height, weight):
	return round(weight/((height/100) **2),2)
app.run()