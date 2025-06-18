from flask import Flask, render_template, request, jsonify
import mysql.connector
import stripe  # or razorpay

app = Flask(__name__)

# Configure Stripe
stripe.api_key = 'your_stripe_secret_key'

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="bus_ticket_db"
)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM buses WHERE seats_available > 0")
    buses = cursor.fetchall()
    return render_template('index.html', buses=buses)

@app.route('/book', methods=['POST'])
def book_ticket():
    data = request.get_json()
    user_name = data['user_name']
    bus_id = data['bus_id']
    amount = 500  # in INR paise for Stripe (i.e. ₹5.00)

    # Create Stripe payment intent
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency='inr',
        metadata={'integration_check': 'accept_a_payment'}
    )

    return jsonify({'clientSecret': intent.client_secret})

@app.route('/confirm', methods=['POST'])
def confirm_booking():
    data = request.get_json()
    name = data['user_name']
    bus_id = data['bus_id']
    seat_no = data['seat_no']
    payment_id = data['payment_id']

    cursor.execute("INSERT INTO bookings (user_name, bus_id, seat_no, payment_status, payment_id) VALUES (%s, %s, %s, %s, %s)", 
                   (name, bus_id, seat_no, "paid", payment_id))
    cursor.execute("UPDATE buses SET seats_available = seats_available - 1 WHERE id = %s", (bus_id,))
    conn.commit()

    return jsonify({'status': 'success'})
