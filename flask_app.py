from flask import render_template, Flask, jsonify
from botfinal import precios
from localbitcoins import local_arg
from forms import LoginForm
from config import Config
from flask_bootstrap import Bootstrap
from coinmarketcap import prices

app = Flask(__name__)
app.config.from_object(Config)
app.static_folder = 'static'

bootstrap = Bootstrap(app)


@app.route('/',methods=['GET', 'POST'])
@app.route('/index', methods=['POST','GET'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        #flash('Login requested for user {}, remember_me={}'.format(
            #form.username.data, form.remember_me.data))
        bitcoin, ethereum, precio_bitcoin,precio_ethereum = precios(form.username.data,form.password.data)
        argentina,venezuela,tasa = local_arg(precio_bitcoin,precio_ethereum)

        #return render_template('table.html', tabla=[result.to_html(classes='data')], titles=result.columns.values, user=user)
        return render_template('table.html', tabla1=[argentina.to_html()], tabla2=[bitcoin.to_html()], tabla3=[ethereum.to_html()], tasa =tasa, precio_bitcoin = precio_bitcoin, precio_eth = precio_ethereum)

    return render_template('index.html', form=form)

@app.route('/table')
def table():
    pass

@app.route('/_get_data/', methods=['POST'])
def _get_data():
    btc,eth=prices()
    argentina,venezuela,tasa = local_arg(btc,eth)

    return jsonify({'data': render_template('response.html', tabla1=[argentina.to_html()], tasa=tasa)})



