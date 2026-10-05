let
    Source = Csv.Document(
        File.Contents("attendance_2024_2026.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(PromotedHeaders, {
        {"Date", type date}, {"Year", Int64.Type}, {"Month", type text}, {"Week", Int64.Type},
        {"EmployeeID", type text}, {"Employee", type text}, {"Department", type text},
        {"Supervisor", type text}, {"Shift", type text}, {"Scheduled", Int64.Type},
        {"Status", type text}, {"Present", Int64.Type}, {"Absent", Int64.Type},
        {"Leave", Int64.Type}, {"Late", Int64.Type}, {"WorkHours", type number},
        {"LateMinutes", Int64.Type}, {"Holiday", Int64.Type}
    })
in
    Typed
