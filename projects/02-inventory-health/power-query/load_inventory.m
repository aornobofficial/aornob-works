let
    Source = Csv.Document(File.Contents("C:\Users\Aornob\PowerBI-Portfolio\projects\02-inventory-health\data\inventory_snapshot.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {{"SnapshotDate", type date}, {"Warehouse", type text}, {"SKU", type text}, {"Category", type text}, {"OnHandUnits", Int64.Type}, {"AvgDailyDemand", type number}, {"LeadTimeDays", Int64.Type}, {"InventoryAgeDays", Int64.Type}, {"UnitCostEUR", Currency.Type}, {"ReorderPointUnits", Int64.Type}})
in Types