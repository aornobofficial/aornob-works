// Replace the file path with the folder where you save warehouse_orders.csv.
let
    Source = Csv.Document(File.Contents("C:\Users\Aornob\PowerBI-Portfolio\projects\01-warehouse-operations\data\warehouse_orders.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {{"OrderID", type text}, {"OrderDate", type date}, {"Warehouse", type text}, {"Region", type text}, {"Carrier", type text}, {"SKU", type text}, {"OrderedQty", Int64.Type}, {"PickedQty", Int64.Type}, {"PromisedDate", type date}, {"ActualDeliveryDate", type date}, {"PickMinutes", Int64.Type}, {"DockWaitMinutes", Int64.Type}, {"OrderValueEUR", Currency.Type}, {"Status", type text}})
in Types