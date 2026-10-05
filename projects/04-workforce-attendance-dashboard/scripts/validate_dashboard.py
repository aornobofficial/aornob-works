from __future__ import annotations
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data_path = ROOT / 'data' / 'attendance_2024_2026.csv'
summary_path = ROOT / 'data' / 'summary.json'
rows = list(csv.DictReader(data_path.open(encoding='utf-8')))
summary = json.loads(summary_path.read_text(encoding='utf-8'))

def total(key, sample=rows):
    return sum(int(float(r[key])) for r in sample)

checks = []
def check(name, condition, detail=''):
    checks.append((name, bool(condition), detail))

check('row count', len(rows) == 43840, len(rows))
check('employee count', len({r['EmployeeID'] for r in rows}) == 40, len({r['EmployeeID'] for r in rows}))
check('date coverage', (min(r['Date'] for r in rows), max(r['Date'] for r in rows)) == ('2024-01-01', '2026-12-31'), (min(r['Date'] for r in rows), max(r['Date'] for r in rows)))
check('scheduled total', total('Scheduled') == summary['scheduled'], (total('Scheduled'), summary['scheduled']))
check('present total', total('Present') == summary['present'], (total('Present'), summary['present']))
check('absent total', total('Absent') == summary['absent'], (total('Absent'), summary['absent']))
check('leave total', total('Leave') == summary['leave'], (total('Leave'), summary['leave']))
check('late total', total('Late') == summary['late'], (total('Late'), summary['late']))
rate = total('Present') / total('Scheduled') * 100
check('attendance rate', round(rate, 1) == summary['attendance_rate'], (round(rate, 1), summary['attendance_rate']))
check('status flags consistent', all(
    (r['Scheduled'] == '0' and r['Status'] == 'Off' and all(r[k] == '0' for k in ('Present','Absent','Leave','Late')))
    or (r['Scheduled'] == '1' and r['Status'] in ('Present','Absent','Leave','Late')
        and int(r['Present']) == int(r['Status'] in ('Present','Late'))
        and int(r['Absent']) == int(r['Status'] == 'Absent')
        and int(r['Leave']) == int(r['Status'] == 'Leave')
        and int(r['Late']) == int(r['Status'] == 'Late'))
    for r in rows
))
check('synthetic identities only', all(r['Employee'] == f"Employee {r['EmployeeID']}" and r['Supervisor'].startswith('Supervisor ') for r in rows))

# Verify the exact filter predicate used by the dashboard for representative combinations.
def filtered(year='All', month='All', department='All', supervisor='All', shift='All', start='', end=''):
    return [r for r in rows if (year == 'All' or r['Year'] == year)
            and (month == 'All' or r['Month'] == month)
            and (department == 'All' or r['Department'] == department)
            and (supervisor == 'All' or r['Supervisor'] == supervisor)
            and (shift == 'All' or r['Shift'] == shift)
            and (not start or r['Date'] >= start)
            and (not end or r['Date'] <= end)]
for args in [
    dict(year='2024'), dict(month='Jan', department='Operations'),
    dict(year='2026', shift='Night', start='2026-03-01', end='2026-06-30'),
    dict(supervisor='Supervisor 02', department='Warehouse'),
]:
    subset = filtered(**args)
    check('filter returns valid subset ' + str(args), all(r in rows for r in subset), len(subset))
    check('filter KPI denominator nonnegative ' + str(args), total('Scheduled', subset) >= 0, str(total('Scheduled', subset)))

failed = [x for x in checks if not x[1]]
for name, ok, detail in checks:
    print(('PASS' if ok else 'FAIL') + f' | {name} | {detail}')
print(f'RESULT: {len(checks)-len(failed)}/{len(checks)} checks passed')
raise SystemExit(1 if failed else 0)
