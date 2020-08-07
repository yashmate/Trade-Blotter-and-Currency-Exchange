
import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/home')
def homepage():
   return render_template('home.html')
@app.route('/')
def inputform():
   return render_template('countryinput.html')

@app.route('/currencytable',methods = ['POST', 'GET'])
def currencyconvert():
    if request.method == 'POST' or request.method == 'GET':
        result = request.form
    print(result)
    code=list(result.values())[0]
    url = 'https://api.exchangerate-api.com/v4/latest/'+str(code)
    response = requests.get(url)
    data = response.json()
    rates_dictionary=data['rates']
    return render_template('new.html',rates = rates_dictionary,base=code)
@app.route('/convert')
def amountconvert():
        return render_template('currencyconvert.html')
@app.route('/conversionresult',methods=['POST','GET'])
def conversion():
    if request.method == 'POST' or request.method == 'GET':
        result=request.form
        print(result)
        import requests
        url = 'https://api.exchangerate-api.com/v4/latest/{}'.format(result['fromcountry'])
        response = requests.get(url)
        res=result['tocountry']
        data = response.json()
        rate=data['rates'][res]
        amount=int(result['amount'])*rate
        return render_template('conversionresult.html',fromcountry=result['fromcountry'],tocountry=result['tocountry'],rate=rate,amount=amount)

@app.route("/sign-up")
def sign_up():
    return render_template("signup.html")
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      if result['email'] == "2017.yash.mate@ves.ac.in" and result['password'] == 'abcxyz12':
          string='CONGRATULATIONS YOU ARE LOGGED IN SUCCESSFULLY'
          return render_template("result.html",result = string)
      else:
          string='INCORRECT USERNAME OR PASSWORD'
          return render_template("errorpage.html",result=string)



@app.route('/news')
def newscrape():
    res=requests.get('https://economictimes.indiatimes.com/topic/Indian-currency/news')
    soup = BeautifulSoup(res.text,'lxml')
    news=soup.find('li',{'class':'active'})
    all_news=news.find_all('p')
    news_list=[]
    for news in all_news:
        news_list.append(news.text)
    return render_template('news.html',news_list=news_list,length=len(news_list))
@app.route('/graphs')
def graph():
    return render_template('traderplot.html')
@app.route('/exchange')
def exchange():
    return render_template('graphplot.html')
@app.route('/currencyconvert',methods = ['POST', 'GET'])
def convert2():
   if request.method == 'POST' or request.method == 'GET':
      result = request.form
      print(result)
      import requests
      url = 'https://api.exchangerate-api.com/v4/latest/{}'.format(result['fromcountry'])
      response = requests.get(url)
      data = response.json()
      country_dict=data['rates']
      exchange=country_dict[result['tocountry']]
      return render_template("currencyconvert.html",result = exchange)
@app.route("/portal")
def portal():
    return render_template("portal.html")

if __name__ == '__main__':
   app.run(port=8054)
