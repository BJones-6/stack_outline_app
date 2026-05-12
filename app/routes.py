from flask import Blueprint, render_template, request, redirect, url_for, flash
from .extensions import db
from datetime import datetime

from .functions import update_trade_account

from .models import Trader, Account, Asset, Trade

from decimal import Decimal

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

        new_trader = Trader(
            TraderID=request.form["TraderID"],
            FirstName=request.form["FirstName"],
            LastName=request.form["LastName"],
            Email=request.form["Email"],
            CreationDate=datetime.today().date()
        )

        db.session.add(new_trader)
        db.session.commit()

        



        return redirect(url_for("main.index"))
    
    return render_template("/forms/create_trader_form.html")


@main.route("/trader/delete/<id>", methods=["POST"])
def delete_trader(id):


    trader = Trader.query.get_or_404(id)
    db.session.delete(trader)
    db.session.commit()

    flash("Trader Deleted Sucessfully", "success")


    return redirect(url_for("main.index"))


@main.route("/trader/update/<id>", methods=["POST"])
def update_trader(id):



    trader = Trader.query.get_or_404(id)

    trader.FirstName = request.form["FirstName"]
    trader.LastName = request.form["LastName"]
    trader.Email = request.form["Email"]

    db.session.commit()

    return "Updated"



@main.route("/trader/<id>")
def trader_detail(id):
    trader = Trader.query.get_or_404(id)
    return render_template("trader.html", trader=trader)














# Account Table CRUD operations and form route

@main.route("/account/create", methods=["GET", "POST"])
def create_account():

    if request.method == "POST":


        new_account = Account(
            AccountID=request.form["AccountID"],
            TraderID=request.form["TraderID"],
            Balance=request.form["Balance"],
            Status=request.form["Status"],
            OpenDate=datetime.today().date(),
            LastUpdated=datetime.today().date()
        )
    
        



        db.session.add(new_account)
        db.session.commit()


        return redirect(url_for("main.index"))
    
    return render_template("/forms/create_account_form.html")

@main.route("/account/delete/<id>", methods=["POST"])
def delete_account(id):
    account = Account.query.get_or_404(id)

    db.session.delete(account)
    db.session.commit()

    flash("Account Sucessfully Deleted", "success")

    return redirect(url_for("main.index"))


@main.route("/account/update/<id>", methods=["POST"])
def update_account(id):
    account = Account.query.get_or_404(id)

    account.Status = request.form["Status"]

    db.session.commit()

    return "Updated"



@main.route("/account/<id>")
def account_detail(id):
    account = Account.query.get_or_404(id)

    return render_template("account.html", account=account)











# Asset CRUD operations and form route

@main.route("/asset/create", methods=["GET", "POST"])
def create_asset():

    if request.method == "POST":

        new_asset = Asset(
            AssetID = request.form["AssetID"],
            Symbol = request.form["Symbol"],
            CurrentPrice = request.form["CurrentPrice"],
            AssetName = request.form["AssetName"],
            CreationDate = datetime.today().date(),
            LastUpdated = datetime.today().date()
        )


        db.session.add(new_asset)
        db.session.commit()

        return redirect(url_for("main.index"))
    
    return render_template("/forms/create_asset_form.html")




@main.route("/asset/delete/<id>", methods=["POST"])
def delete_asset(id):
    asset = Asset.query.get_or_404(id)

    db.session.delete(asset)
    db.session.commit()

    flash("Asset Deleted Sucessfully", "success")

    return redirect(url_for("main.index"))



@main.route("/asset/update/<id>", methods=["POST"])
def update_asset(id):
    asset = Asset.query.get_or_404(id)

    asset.Symbol = request.form["Symbol"]

    asset.CurrentPrice = request.form["CurrentPrice"]

    asset.AssetName = request.form["AssetName"]

    asset.LastUpdated = datetime.today().date()

    db.session.commit()

    return "Updated"


@main.route("/asset/<id>")
def detail_asset(id):
    asset = Asset.query.get_or_404(id)

    return render_template("asset.html", asset=asset)








# CRUD operations for Trade table

@main.route("/trade/create", methods=["GET", "POST"])
def create_trade():
    if request.method == "POST":

        new_trade = Trade(
            TradeID = request.form["TradeID"],
            AccountID = request.form["AccountID"],
            AssetID = request.form["AssetID"],
            TradeType = request.form["TradeType"],
            Quantity = request.form["Quantity"],
            EntryPrice = Decimal(request.form.get("EntryPrice")),
            # ExitPrice = request.form["ExitPrice"],
            EntryDate = datetime.today().date(),
            # ExitDate = request.form["ExitDate"],
            Status = "Open",
            LastUpdated = datetime.today().date()
        )

        db.session.add(new_trade)

        db.session.commit()

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

        
        exitprice = request.form.get("ExitPrice")

        if exitprice:
            trade.ExitPrice = Decimal(exitprice)
            trade.Status = "Closed"
            update_trade_account(trade)


        trade.LastUpdated = datetime.today().date()

        db.session.commit()

        flash("Sucessfully Updated Trades Table and Account Balance", "success")



        return redirect(url_for("main.index"))
    
    return render_template("/forms/update_trade_form.html", trade=trade)




@main.route("/trade/<id>")
def detail_trade(id):
    trade = Trade.query.get_or_404(id)

    return render_template("trade.html", trade=trade)









