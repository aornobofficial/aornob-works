# Warehouse Service & Pick Productivity

**Portfolio demo.** All records are synthetic. No employer, customer, or operational data is used.

## Business question
Which sites combine late delivery, incomplete picks, and long pick or dock times?

## Model
Import `data/warehouse_orders.csv` as `WarehouseOrders`. For a production model, split Date, Warehouse, Carrier, and Product dimensions from the order fact table and relate each dimension one-to-many.

## Demo measures and result
DAX is in `dax/measures.dax`; Power Query M is in `power-query/load_orders.m`. The preview reports 240 generated orders, average pick time 27.2 minutes, and sample order value €181,869. These are generated values, not real-world results.

## Suggested visuals
KPI cards for Orders, OTIF %, Average Pick Minutes; warehouse bar chart; daily OTIF trend; matrix by warehouse and carrier; slicers for date and region.

Open `dashboard-preview.html` for a visual concept.
