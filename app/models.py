from .extensions import db


class Trader(db.Model):
    __tablename__ = "Trader"

    TraderID = db.Column(db.String(8), primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    CreationDate = db.Column(db.Date, nullable=False)
    Email = db.Column(db.String(75), nullable=False, unique=True)


    accounts = db.relationship('Account', backref='trader')



    def __repr__(self):
        return f"<Trader {self.TraderID}>"



class Account(db.Model):
    __tablename__ = "Account"

    AccountID = db.Column(db.String(8), primary_key=True)
    TraderID = db.Column(db.String(8), db.ForeignKey('Trader.TraderID'), nullable=False)
    Balance = db.Column(db.Float, nullable=False)
    Status = db.Column(db.String(10), nullable=False)
    OpenDate = db.Column(db.Date, nullable=False)
    LastUpdated = db.Column(db.Date)


    trades = db.relationship('Trade', backref='account')


    def __repr__(self):
        return f"<Account {self.AccountID}>"
    


class Asset(db.Model):
    __tablename__ = "Asset"

    AssetID = db.Column(db.String(8), primary_key=True)
    Symbol = db.Column(db.String(10), unique=True, nullable=False)
    CurrentPrice = db.Column(db.Float, nullable=False)
    AssetName = db.Column(db.String(50), nullable=False)
    CreationDate = db.Column(db.Date, nullable=False)
    LastUpdated = db.Column(db.Date)



    trades = db.relationship('Trade', backref='asset')

    def __repr__(self):
        return f"<Asset {self.AssetID}>"
    

class Trade(db.Model):
    __tablename__ = "Trade"

    TradeID = db.Column(db.String(10), primary_key=True)
    AccountID = db.Column(db.String(8), db.ForeignKey('Account.AccountID'), nullable=False)
    AssetID = db.Column(db.String(8), db.ForeignKey('Asset.AssetID'), nullable=False)
    TradeType = db.Column(db.String(8), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    EntryPrice = db.Column(db.Float, nullable=False)
    ExitPrice = db.Column(db.Float)
    EntryDate = db.Column(db.Date, nullable=False)
    ExitDate = db.Column(db.Date)
    Status = db.Column(db.String(10), nullable=False)
    LastUpdated = db.Column(db.Date)
    Profit_Loss = db.Column(db.Float)


    def __repr__(self):
        return f"<Trade {self.TradeID}>"

