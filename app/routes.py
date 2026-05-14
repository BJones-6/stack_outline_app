from flask import Blueprint, render_template, request, redirect, url_for, flash
from .extensions import db
from datetime import datetime
from .functions import update_trade_account
from .models import Trader, Account, Asset, Trade
from decimal import Decimal
from sqlalchemy import func, case, and_, or_
from sqlalchemy.exc import IntegrityError

main = Blueprint("main", __name__)

@main.route("/")
def index():
    traders = Trader.query.all()
    accounts = Account.query.all()
    assets = Asset.query.all()
    trades = Trade.query.all()
    return render_template("index.html", traders=traders, accounts=accounts, assets=assets, trades=trades)




# @main.route("/trader/create")
# def create_trader_form():
    # return render_template("/forms/create_trader_form.html")



# Trader Form Route/CRUD Operations
@main.route("/trader/create", methods=["GET", "POST"])
def create_trader():
    
    if request.method == "POST":

        trader_id = request.form.get("TraderID")


        first = request.form.get("FirstName")
        last = request.form.get("LastName")
        email = request.form.get("Email")

        if not all([trader_id, first, last, email]):
            flash("All fields are required.", "danger")
            return redirect(url_for("main.create_trader"))

        new_trader = Trader(
            TraderID=trader_id,
            FirstName=first,
            LastName=last,
            Email=email,
            CreationDate=datetime.today().date()
        )

        try:
            db.session.add(new_trader)
            db.session.commit()
            flash("Trader Created Successfully", "success")
        except IntegrityError:
            db.session.rollback()
            flash("TraderID or Email must be unique.", "danger")
            return redirect(url_for("main.create_trader"))

        return redirect(url_for("main.index"))
    
    return render_template("/forms/create_trader_form.html")


@main.route("/trader/delete/<id>", methods=["POST"])
def delete_trader(id):


    trader = Trader.query.get_or_404(id)
    db.session.delete(trader)
    db.session.commit()

    flash("Trader Deleted Sucessfully", "success")


    return redirect(url_for("main.index"))

"""
@main.route("/trader/update/<id>", methods=["POST"])
def update_trader(id):



    trader = Trader.query.get_or_404(id)

    trader.FirstName = request.form["FirstName"]
    trader.LastName = request.form["LastName"]
    trader.Email = request.form["Email"]

    db.session.commit()

    return "Updated"
"""


# @main.route("/trader/<id>")
# def trader_detail(id):
    # trader = Trader.query.get_or_404(id)
    # return render_template("trader.html", trader=trader)














# Account Table CRUD operations and form route

@main.route("/account/create", methods=["GET", "POST"])
def create_account():

    if request.method == "POST":

        account_id = request.form.get("AccountID")
        trader_id = request.form.get("TraderID")
        balance_raw = request.form.get("Balance")
        status = request.form.get("Status")

        if not all([account_id, trader_id, balance_raw, status]):
            flash("All fields are required.", "danger")
            return redirect(url_for("main.create_account"))

        try:
            balance = Decimal(balance_raw)
        except:
            flash("Balance must be a valid number.", "danger")
            return redirect(url_for("main.create_account"))

        if balance < 0:
            flash("Balance cannot be negative.", "danger")
            return redirect(url_for("main.create_account"))

        
        trader = Trader.query.get(trader_id)
        if not trader:
            flash("Trader does not exist.", "danger")
            return redirect(url_for("main.create_account"))

        new_account = Account(
            AccountID=account_id,
            TraderID=trader_id,
            Balance=balance,
            Status=status,
            OpenDate=datetime.today().date(),
            LastUpdated=datetime.today().date()
        )

        try:
            db.session.add(new_account)
            db.session.commit()
            flash("Account Created Successfully", "success")
        except IntegrityError:
            db.session.rollback()
            flash("AccountID must be unique.", "danger")
            return redirect(url_for("main.create_account"))

        return redirect(url_for("main.index"))

    
    return render_template("/forms/create_account_form.html")

@main.route("/account/delete/<id>", methods=["POST"])
def delete_account(id):
    account = Account.query.get_or_404(id)

    db.session.delete(account)
    db.session.commit()

    flash("Account Sucessfully Deleted", "success")

    return redirect(url_for("main.index"))


@main.route("/account/update/<id>", methods=["GET", "POST"])
def update_account(id):
    account = Account.query.get_or_404(id)

    if request.method == "POST":


        account.Status = request.form.get("Status")

        db.session.commit()

        return redirect(url_for("main.index"))
    
    return render_template("/forms/update_account_form.html", account=account)


@main.route ("/account/summary/<id>", methods=["GET"])
def account_summary(id):
    account = Account.query.get_or_404(id)

    total_trades = db.session.query(func.count(Trade.TradeID)).filter(Trade.AccountID == id, Trade.Status == "Closed").scalar() or 0

    winning_trades = db.session.query(
        func.count(Trade.TradeID)
    ).filter(
        Trade.AccountID == id,
        Trade.Status == "Closed",
        or_(
            and_(Trade.TradeType == "Long",
                 Trade.ExitPrice > Trade.EntryPrice),
            and_(Trade.TradeType == "Short", 
                Trade.ExitPrice < Trade.EntryPrice)
        )
    ).scalar() or 0

    total_pnl = db.session.query(
        func.sum(
            case(
                (
                    Trade.TradeType == "Long",
                    (Trade.ExitPrice - Trade.EntryPrice) * Trade.Quantity
                ),
                else_=(Trade.EntryPrice - Trade.ExitPrice) * Trade.Quantity
            )
        )
    ).filter(
        Trade.AccountID == id,
        Trade.Status == "Closed"
    ).scalar() or 0

    win_rate = (winning_trades / total_trades * 100) if total_trades else 0

    trades = Trade.query.filter_by(
        AccountID=id,
        Status="Closed"
    ).all()



    return render_template(
        "account_summary.html",
        account=account,
        trades=trades,
        total_pnl=total_pnl,
        total_trades=total_trades,
        winning_trades=winning_trades,
        win_rate=win_rate
    )

# @main.route("/account/<id>")
# def account_detail(id):
    # account = Account.query.get_or_404(id)

    # return render_template("account.html", account=account)











# Asset CRUD operations and form route

@main.route("/asset/create", methods=["GET", "POST"])
def create_asset():

    if request.method == "POST":

        asset_id = request.form.get("AssetID")
        symbol = request.form.get("Symbol")
        name = request.form.get("AssetName")
        price_raw = request.form.get("CurrentPrice")

        if not all([asset_id, symbol, name, price_raw]):
            flash("All fields are required.", "danger")
            return redirect(url_for("main.create_asset"))

        try:
            price = Decimal(price_raw)
        except:
            flash("Price must be a valid number.", "danger")
            return redirect(url_for("main.create_asset"))

        if price <= 0:
            flash("Price must be positive.", "danger")
            return redirect(url_for("main.create_asset"))

        new_asset = Asset(
            AssetID=asset_id,
            Symbol=symbol,
            AssetName=name,
            CurrentPrice=price,
            CreationDate=datetime.today().date(),
            LastUpdated=datetime.today().date()
        )

        try:
            db.session.add(new_asset)
            db.session.commit()
            flash("Asset Created Successfully", "success")
        except IntegrityError:
            db.session.rollback()
            flash("AssetID or Symbol must be unique.", "danger")
            return redirect(url_for("main.create_asset"))

        return redirect(url_for("main.index"))
    
    return render_template("/forms/create_asset_form.html")




@main.route("/asset/delete/<id>", methods=["POST"])
def delete_asset(id):
    asset = Asset.query.get_or_404(id)

    db.session.delete(asset)
    db.session.commit()

    flash("Asset Deleted Sucessfully", "success")

    return redirect(url_for("main.index"))


"""
@main.route("/asset/update/<id>", methods=["POST"])
def update_asset(id):
    asset = Asset.query.get_or_404(id)

    asset.Symbol = request.form["Symbol"]

    asset.CurrentPrice = request.form["CurrentPrice"]

    asset.AssetName = request.form["AssetName"]

    asset.LastUpdated = datetime.today().date()

    db.session.commit()

    return "Updated"
"""

# @main.route("/asset/<id>")
# def detail_asset(id):
    # asset = Asset.query.get_or_404(id)

    
    # return render_template("asset.html", asset=asset)








# CRUD operations for Trade table

@main.route("/trade/create", methods=["GET", "POST"])
def create_trade():
    if request.method == "POST":



        trade_id = request.form.get("TradeID")
        account_id = request.form.get("AccountID")
        asset_id = request.form.get("AssetID")
        trade_type = request.form.get("TradeType")
        quantity_raw = request.form.get("Quantity")
        entry_price_raw = request.form.get("EntryPrice")

        if not all([trade_id, account_id, asset_id, trade_type, quantity_raw, entry_price_raw]):
            flash("All fields are required.", "danger")
            return redirect(url_for("main.create_trade"))

        try:
            quantity = int(quantity_raw)
            entry_price = Decimal(entry_price_raw)
        except:
            flash("Quantity and Entry Price must be valid numbers.", "danger")
            return redirect(url_for("main.create_trade"))

        if quantity <= 0:
            flash("Quantity must be positive.", "danger")
            return redirect(url_for("main.create_trade"))

        if entry_price <= 0:
            flash("Entry price must be positive.", "danger")
            return redirect(url_for("main.create_trade"))

        if trade_type not in ["Long", "Short"]:
            flash("Invalid trade type.", "danger")
            return redirect(url_for("main.create_trade"))

        # Foreign key checks
        account = Account.query.get(account_id)

        if not account:
            flash("Account does not exist.", "danger")
            return redirect(url_for("main.create_trade"))
        
        if account.Status == "Suspended":
            flash("Suspended Accounts cannot place trades", "danger")
            return redirect(url_for("main.create_trade"))
        


        if not Asset.query.get(asset_id):
            flash("Asset does not exist.", "danger")
            return redirect(url_for("main.create_trade"))
        



        new_trade = Trade(
            TradeID=trade_id,
            AccountID=account_id,
            AssetID=asset_id,
            TradeType=trade_type,
            Quantity=quantity,
            EntryPrice=entry_price,
            EntryDate=datetime.today().date(),
            Status="Open",
            LastUpdated=datetime.today().date()
        )

        try:
            db.session.add(new_trade)
            db.session.commit()
            flash("Trade Created Successfully", "success")
        except IntegrityError:
            db.session.rollback()
            flash("TradeID must be unique.", "danger")
            return redirect(url_for("main.create_trade"))
        
        return redirect(url_for("main.index"))

    
    return render_template("/forms/create_trade_form.html")




@main.route("/trade/delete/<id>", methods=["POST"])
def delete_trade(id):

    trade = Trade.query.get_or_404(id)

    db.session.delete(trade)
    db.session.commit()

    flash("Trade Deleted Sucessfully", "success")

    return redirect(url_for("main.index"))





@main.route("/trade/update/<id>", methods=["GET", "POST"])
def update_trade(id):

    trade = Trade.query.get_or_404(id)

    if request.method == "POST":

        
        exitprice_raw = request.form.get("ExitPrice")

        if exitprice_raw:
            
            try:
                exitprice = Decimal(exitprice_raw)
            except:
                flash("Exit Price must be a valid number", "danger")
                return redirect(url_for("main.update_trade", id=id))
            
            if exitprice < 0:
                flash("Exit Price cannot be negative", "danger")
                return redirect(url_for("main.update_trade", id=id))
            
            trade.ExitPrice = exitprice
            trade.Status = "Closed"
            update_trade_account(trade)

            account = Account.query.get(trade.AccountID)

            if account.Balance <= 0:
                account.Status = "Suspended"
            

        
        
        

            if not trade.ExitDate:
                trade.ExitDate = datetime.today().date()

        trade.LastUpdated = datetime.today().date()

        try:

            db.session.commit()
            flash("Sucessfully Updated Trades Table and Account Balance", "success")
        except:
            db.session.rollback()
            flash("Something went wrong", "danger")
            return redirect(url_for("main.update_trade"))



        return redirect(url_for("main.index"))
    
    return render_template("/forms/update_trade_form.html", trade=trade)




# @main.route("/trade/<id>")
# def detail_trade(id):
    # trade = Trade.query.get_or_404(id)

    # return render_template("trade.html", trade=trade)








