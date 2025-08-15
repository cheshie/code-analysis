from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
db_config = {
    'host': 'localhost',
    'user': '<.........>',
    'password': '<.........>',
    'database': '<.........>'
}

@app.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    assert name is not None, "Name parameter is required"
    cursor.execute(f"SELECT * FROM products WHERE name = '{name}'")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    if products:
        return jsonify(products)
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)