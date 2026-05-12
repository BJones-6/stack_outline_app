from .models import Trader, Account, Asset, Trade
from .extensions import db
from decimal import Decimal

def update_trade_account(trade):
    account = Account.query.get_or_404(trade.AccountID)

    if trade.ExitPrice is None:
        return
    


    if trade.TradeType == "Long":
        account.Balance += (trade.ExitPrice - trade.EntryPrice) * trade.Quantity
        
        
    
    else:
        account.Balance += (trade.EntryPrice - trade.ExitPrice) * trade.Quantity

    db.session.commit()
        
    
