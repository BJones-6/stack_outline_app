# Trade Database App

## Project Description

The Trade Database App is a full-stack trading account management system built with 
Python, Flask, SQLAlchemy, and SQLite.

This application allows users to manage traders, trading accounts, financial assets, 
and individual trades.

Users can:
- Create and manage Traders, Accounts, Assets, and Trades
- Execute multi-table CRUD operations
- View account-level performance summaries
- Track profit and loss (P&L)
- Calculate win rate statistics


The system is designed to simulate a simplified brokerage back-office 
environment where trade data, account balances, and asset information 
must remain consistent and accurate.

## Who Is This App For?

This application is intended for:

- Students learning relational database design and normalization
- Developers practicing full-stack CRUD architecture
- Individuals modeling trading account performance systems
- Anyone interested in financial transaction data modeling

Tables are in 3rd Normal Form.




# Details
- Python 3
- Flask backend
- Relational DB: SQLite
- SQLAlchemy ORM
- HTML5/CSS3 frontend with Bootstrap and Jinja2 templates
- Git version control

## Project Structure

```
Trade_Database_App/
  app/
    __init__.py
    extensions.py
    models.py
    routes.py
    functions.py
    static/css/styles.css
    templates/base.html
    templates/index.html
    templates/account_summary.html
    templates/forms/create_account_form.html
    templates/forms/create_asset_form.html
    templates/forms/create_trade_form.html
    templates/forms/create_trader_form.html
    templates/forms/update_account_form.html
    templates/forms/update_trade_form.html
  config.py
  run.py
  requirements.txt
  .env.example
  .gitignore
```

## Quick Start

1. Create and activate a virtual environment.
   ```
   python -m venv venv   
   venv\Scripts\activate 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python run.py
   ```
4. Open http://127.0.0.1:5000
5. Add records for the different tables by clicking the "add" buttons on the top right
6. Delete records by pressing the red "delete" buttons 
7. Update Trade and Account Records by clicking the blue edit buttons 
8. Click "View Account Summary" blue link under the Accounts part of the webpage to see details about them.
9. Click the text at the top left to go back to the home page. 

 