**Original Functional Dependencies:**



**Trader Table Dependencies:**

* { TraderID } -> { FirstName, LastName, CreationDate, Email }





**Account Table Dependencies:**

* { AccountID } -> { TraderID, Balance, Status, OpenDate, LastUpdated }





**Asset Table Dependencies:**

* { AssetID } -> { Symbol, CurrentPrice, AssetName, CreationDate, LastUpdated }



**Trade Table Dependencies:**

* { TradeID } -> { AccountID, AssetID, TradeType, Quantity, EntryPrice, ExitPrice, EntryDate, ExitDate, Status, LastUpdated }





**Anomaly Identification:**



**Update Anomalies:**

No update anomalies as the same data is not stored across multiple tables. 


**Insertion Anomalies:**

Cannot insert a trade without an AccountID.
Cannot insert a trade without an AssetID.

Cannot insert an account without a TraderID



**Deletion Anomalies:**

If you delete a row in the Asset table that asset won't exist in the database anymore so you lose that data. Can say the same for the other tables. 



**Decomposition Steps:**

The schema was designed directly in 3NF. No decomposition was required because all non-key attributes depend only on their primary key and there are no transitive dependencies.




**Final Relational Schema:**



**Trader Table:**



|PK|TraderID|
|-|-|
||FirstName|
||LastName|
||Email|
||CreationDate|





**Account Table:**



|PK|AccountID|
|-|-|
|FK|TraderID|
||Balance|
||Status|
||OpenDate|
||LastUpdated|





**Asset Table:**



|PK|AssetID|
|-|-|
||Symbol|
||CurrentPrice|
||AssetName|
||CreationDate|
||LastUpdated|





**Trade Table:**



|PK|TradeID|
|-|-|
|FK|AccountID|
|FK|AssetID|
||TradeType|
||Quantity|
||EntryPrice|
||ExitPrice|
||EntryDate|
||ExitDate|
||Status|
||LastUpdated|



