from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://store_user:secure_password@localhost/tech_store_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        description = db.Column(db.Text, nullable=False)
        price = db.Column(db.Float, nullable=False)
        stock = db.Column(db.Integer, nullable=False)
        image_url = db.Column(db.String(255), nullable=True)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Página principal (Home)
@app.route('/')
def index():
    return render_template('index.html')

# Página de productos
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Página de contacto / registro de clientes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_customer = Customer(name=name, email=email)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

