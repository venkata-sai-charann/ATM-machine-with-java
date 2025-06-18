CREATE TABLE buses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route VARCHAR(100),
    date DATE,
    time TIME,
    seats_available INT
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100),
    bus_id INT,
    seat_no INT,
    payment_status VARCHAR(20),
    payment_id VARCHAR(100),
    FOREIGN KEY (bus_id) REFERENCES buses(id)
);
