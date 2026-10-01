# Carrier & Route Reliability

**Portfolio demo using synthetic data only.**

## Business question
How do carrier punctuality, failed deliveries, fuel, and trip cost vary across routes?

## Model
Load `data/delivery_routes.csv` as `DeliveryRoutes`. For a fuller star schema, separate Calendar, Route, Carrier, and Vehicle dimensions.

## Demo result
Generated sample contains 300 trips, on-time trip rate 37.3%, and €9.79 cost per stop. Simulated values are not a real company result.

## Suggested visuals
Carrier on-time bars, route-level scatter plot of cost vs on-time rate, monthly delay trend, exception table, and slicers for carrier, route, and vehicle.

DAX, Power Query, and an HTML preview are included.
