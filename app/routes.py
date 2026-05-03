from flask import Blueprint, render_template

from .models import Trader, Account, Asset, Trade

main = Blueprint("main", __name__)


@main.route("/")
def index():
    traders = Trader.query.all()
    return render_template("index.html", traders=traders)
