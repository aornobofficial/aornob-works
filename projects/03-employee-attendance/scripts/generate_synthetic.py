from __future__ import annotations
import csv, random
from datetime import date, timedelta
from pathlib import Path

random.seed(20261005)
root = Path(__file__).resolve().parents[1]
out = root / 'data' / 'attendance_2024_2026.csv'
out.parent.mkdir(parents=True, exist_ok=True)
people = []
first = ['Alex','Mia','Noah','Emma','Oliver','Ava','Leo','Ella','Elias','Sofia','Liam','Nora','Milan','Iris','Daniel','Lina','Oskar','Sara','Jonas','Alma','Elliot','Freja','Lucas','Ida','Theo','Clara','Hugo','Aino','Anton','Elsa','Emil','Liv','Felix','Selma','Adam','Ella','Matti','Olivia','Aron','Mila']
last = ['Berg','Niemi','Virtanen','Laine','Saarinen','Koskinen','Heikkinen','Mäkinen','Lehtonen','Korhonen']
departments = ['Operations','Warehouse','Customer Service','Transport']
supervisors = ['S. Bradost','J. Oravasaari','M. Nieminen','A. Virtanen']
shifts = ['Morning','Evening','Night']
for i in range(40):
    people.append((f'E{i+1:03d}', f'{first[i]} {last[i%len(last)]}', departments[i%4], supervisors[i%4], shifts[i%3]))
start, end = date(2024,1,1), date(2026,12,31)
rows=[]
d = start
while d <= end:
    weekday = d.weekday()
    holiday = weekday >= 5 or (d.month == 12 and d.day in (24,25,26,31)) or (d.month == 1 and d.day == 1)
    for eid, name, dept, sup, shift in people:
        scheduled = not holiday
        status = 'Off' if not scheduled else random.choices(['Present','Absent','Leave','Late'], weights=[89,4,5,2])[0]
        if status == 'Present':
            work_hours = round(random.uniform(7.3, 8.3), 2)
            late_min = 0
        elif status == 'Late':
            work_hours = round(random.uniform(6.5, 7.9), 2)
            late_min = random.randint(5, 42)
        else:
            work_hours = 0
            late_min = 0
        rows.append({
            'Date': d.isoformat(), 'Year': d.year, 'Month': d.strftime('%b'), 'Week': d.isocalendar().week,
            'EmployeeID': eid, 'Employee': name, 'Department': dept, 'Supervisor': sup, 'Shift': shift,
            'Scheduled': int(scheduled), 'Status': status, 'Present': int(status in ('Present','Late')),
            'Absent': int(status == 'Absent'), 'Leave': int(status == 'Leave'), 'Late': int(status == 'Late'),
            'WorkHours': work_hours, 'LateMinutes': late_min, 'Holiday': int(holiday)
        })
    d += timedelta(days=1)
with out.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader(); writer.writerows(rows)
print(f'generated {len(rows)} synthetic rows at {out}')
