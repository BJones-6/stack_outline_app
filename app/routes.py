from flask import Blueprint, render_template

from .models import Trader, Account, Asset, Trade

main = Blueprint("main", __name__)

@main.route("/")
def index():
    traders= Trader.query.all()
    return render_template("index.html", traders=traders)




@main.route("/trader/create", methods=["POST"])
def create_trader():
    from flask import request, redirect, url_for
    from .extensions import db
    from datetime import datetime

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


@main.route("/trader/delete/<id>")
def delete_trader(id):
    from .extensions import db

    trader = Trader.query.get_or_404(id)
    db.session.delete(trader)
    db.session.commit()


    return "Deleted"


@main.route("/trader/update/<id>", methods=["POST"])
def update_trader(id):

    from flask import request
    from .extensions import db

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

    
