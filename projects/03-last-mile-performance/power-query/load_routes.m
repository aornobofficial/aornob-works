let
    Source = Csv.Document(File.Contents("C:\Users\Aornob\PowerBI-Portfolio\projects\03-last-mile-performance\data\delivery_routes.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {{"TripID", type text}, {"ShipDate", type date}, {"Route", type text}, {"Carrier", type text}, {"VehicleType", type text}, {"PlannedMinutes", Int64.Type}, {"ActualMinutes", Int64.Type}, {"DistanceKm", type number}, {"Stops", Int64.Type}, {"FailedDeliveries", Int64.Type}, {"FuelLitres", type number}, {"TripCostEUR", Currency.Type}})
in Types