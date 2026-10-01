# Inventory Health & Replenishment Risk

**Portfolio demo using synthetic data only.**

## Business question
Where are stock levels below a simple replenishment threshold, and where is inventory aging?

## Model
Load `data/inventory_snapshot.csv` as `InventorySnapshot`. In a fuller model, use Date, Warehouse, Product dimensions and a periodic snapshot fact.

## Demo result
Generated sample has 720 SKU-site-month records, 169 rows below the illustrative reorder point, and €15,180,693 in stock aged over 120 days. These are simulated outputs, not actual business performance.

## Workflow extension
A production version could refresh from an approved inventory source, flag gaps above a chosen materiality threshold, and route a review task to an inventory owner. No real integration or alert is included in this demo.

DAX, Power Query, and a visual concept are included.
