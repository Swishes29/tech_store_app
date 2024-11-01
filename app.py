from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://store_user:admin@localhost/tech_store_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo para los productos
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

# Modelo para los clientes
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    imagen_url = db.Column(db.String(255))

# Filtro para truncar palabras en Jinja
def truncatewords(value, words=20):
    word_list = value.split()
    truncated = ' '.join(word_list[:words])
    if len(word_list) > words:
        truncated += '…'
    return Markup(truncated)

# Registra el filtro en Jinja
app.jinja_env.filters['truncatewords'] = truncatewords

# Página principal (Home) con clientes y producto destacado
@app.route('/')
def index():
    customers = Customer.query.all()
    featured_product = Product.query.first()  # Selecciona el primer producto como destacado
    return render_template('index.html', customers=customers, featured_product=featured_product)

# Página de productos
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Función de búsqueda de productos
@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '')
    if query:
        products = Product.query.filter(
            Product.name.ilike(f"%{query}%") |
            Product.description.ilike(f"%{query}%")
        ).all()
    else:
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
