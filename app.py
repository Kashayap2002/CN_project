from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Store user data in the database (You'll need to implement this)

        return "Registration successful!"  # You can redirect to a success page

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# ... (register route from above)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Implement logic to check username and password against database (You'll need to implement this)

        # For now, let's assume login is successful
        return "Login successful!"  # You can redirect to a success page

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

# ... (register and login routes from previous steps)

@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
    if request.method == 'POST':
        food_name = request.form['food_name']
        amount_left = request.form['amount_left']
        price = request.form['price']
        time = request.form['time']

        # Store food details in the database (You'll need to implement this)

        return "Food details added successfully!"  # You can redirect to a success page

    return render_template('add_food.html')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

# ... (previous routes and configurations)

@app.route('/book_food', methods=['GET', 'POST'])
def book_food():
    if request.method == 'POST':
        # Iterate through form data to get booked food details
        booked_foods = []
        for key, value in request.form.items():
            if key.startswith('quantity_') and int(value) > 0:
                food_id = int(key.split('_')[-1])
                quantity = int(value)
                # Store booked food details in a list or database (you'll need to implement this)

                booked_foods.append({'food_id': food_id, 'quantity': quantity})
        
        # Store the booked food details in the database (you'll need to implement this)

        return "Food coupons booked successfully!"  # Redirect to a success page

    # Fetch food details from the database (You'll need to replace this with your logic)
    foods = [
        {'id': 1, 'name': 'Food 1', 'amount_left': 10, 'price': 50, 'time': '9:00 PM'},
        {'id': 2, 'name': 'Food 2', 'amount_left': 5, 'price': 70, 'time': '9:00 PM'},
        # Add more food details as per your database
    ]

    return render_template('book_food.html', foods=foods)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ... (previous routes and configurations)

@app.route('/book_food', methods=['GET', 'POST'])
def book_food():
    if request.method == 'POST':
        # Process form data and store booked food details in your database (similar to Step 3)
        booked_items = []  # Replace this with the booked food details from the database

        return render_template('confirmation.html', booked_items=booked_items)  # Render confirmation page

    # Fetch food details from the database (similar to Step 3)
    foods = [
        {'id': 1, 'name': 'Food 1', 'amount_left': 10, 'price': 50, 'time': '9:00 PM'},
        {'id': 2, 'name': 'Food 2', 'amount_left': 5, 'price': 70, 'time': '9:00 PM'},
        # Add more food details as per your database
    ]

    return render_template('book_food.html', foods=foods)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ... (previous routes and configurations)

@app.route('/book_food', methods=['GET', 'POST'])
def book_food():
    if request.method == 'POST':
        # Process form data and store booked food details in your database (similar to Step 3)
        booked_items = []  # Replace this with the booked food details from the database

        return render_template('confirmation.html', booked_items=booked_items)  # Render confirmation page

    # Fetch food details from the database (similar to Step 3)
    foods = [
        {'id': 1, 'name': 'Food 1', 'amount_left': 10, 'price': 50, 'time': '9:00 PM'},
        {'id': 2, 'name': 'Food 2', 'amount_left': 5, 'price': 70, 'time': '9:00 PM'},
        # Add more food details as per your database
    ]

    return render_template('book_food.html', foods=foods)

if __name__ == '__main__':
    app.run(debug=True)

