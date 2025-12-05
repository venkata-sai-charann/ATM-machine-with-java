ATM Machine (Java, OOP-Based)

This is a simple Object-Oriented ATM Machine program written in Java.
It simulates ATM operations such as:

✔ User authentication

✔ Checking balance

✔ Depositing money

✔ Withdrawing money

✔ Managing multiple accounts (via Bank class)

All logic is built using OOP concepts like encapsulation, classes, and objects.
Everything runs through the console.

🚀 Features

Fully Object-Oriented Design

Account class → handles balance & PIN

Bank class → stores multiple accounts

ATMEngine class → handles login + operations

ATM (main class) → entry point

User Authentication

Enter account number

Enter correct PIN to continue

ATM Operations

Check balance

Deposit money

Withdraw money

Exit session

Simple, Extendable Structure

Easily add new features such as:

Account creation menu

Saving user data to files

Support for multiple users

GUI version (JavaFX/Swing)

📂 Project Structure
ATM.java


This single file contains all classes:

Account

Bank

ATMEngine

ATM (with main method)

🔧 How to Run
1. Compile:
javac ATM.java

2. Run:
java ATM

🔑 Default Accounts

You can log in using any of these sample accounts:

Account Number	PIN	Balance
1001	1234	5000.00
2002	4321	3000.00
🧩 Example Workflow
===== Welcome to OOP ATM =====
Enter Account Number: 1001
Enter PIN: 1234

===== ATM Menu =====
1. Check Balance
2. Deposit
3. Withdraw
4. Exit

🛠️ Technologies Used

Java (Core)

OOP Principles

Console-based I/O

📘 Future Enhancements

Save account data to files (persistence)

Add an account creation system

Add transaction history

Build a graphical interface (JavaFX/Swing)

📄 License

This project is free to use, modify, and share.
