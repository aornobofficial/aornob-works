# Workforce Attendance Control Center

A Power BI-ready, glassmorphism-style attendance portfolio dashboard built entirely from **synthetic demonstration data**. The user-provided `Employee_Attendance_Report.xlsx` was not used as a data source and is not included in this project.

## What is included

- `data/attendance_2024_2026.csv`: 43,840 synthetic employee-day rows covering January 1, 2024 through December 31, 2026.
- `data/summary.json`: verified summary values used by the public preview.
- `index.html`: responsive public dashboard preview with dark glass UI.
- `power-query/load_attendance.m`: Power Query import script for Power BI Desktop.
- `dax/measures.dax`: core attendance measures.
- `scripts/`: deterministic synthetic data generator and summary builder.

## Dashboard pages / navigation plan

- Overview
- Attendance Analytics
- Employees
- Leave & Absence
- Shift Analytics
- Reports
- Filters / Settings

## Main KPIs

Attendance Rate, Active Employees, Present (including late) Records, Absent Records, Leave Records, Late Records, Working Days, Average Work Hours, Absence Rate, Leave Rate, and Supervisor/Department attendance comparison.

## Power BI note

Power BI Desktop was not detected on the build machine, so this repository contains a validated Power BI-ready data/model pack and a live static preview, not a native `.pbix` file. Open `power-query/load_attendance.m` in Power BI Desktop and point it at the CSV in the same `data` folder. The HTML preview is not a substitute for a native `.pbix` report.

## Privacy

This demo is synthetic. It contains no real employee names, attendance records, company data, or values from the user's private workbook. Do not describe the metrics as real operational results.
