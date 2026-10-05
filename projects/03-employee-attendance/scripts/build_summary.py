from __future__ import annotations
import csv, json
from collections import Counter, defaultdict
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'data/attendance_2024_2026.csv').open(encoding='utf-8')))
def yes(k): return sum(int(r[k]) for r in rows)
scheduled=sum(int(r['Scheduled']) for r in rows)
present=yes('Present')
absent=yes('Absent'); leave=yes('Leave'); late=yes('Late')
monthly=defaultdict(lambda: Counter())
for r in rows:
    key=f"{r['Year']}-{int({'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}[r['Month']]):02d}"
    monthly[key]['present'] += int(r['Present']); monthly[key]['absent'] += int(r['Absent']); monthly[key]['leave'] += int(r['Leave']); monthly[key]['late'] += int(r['Late']); monthly[key]['scheduled'] += int(r['Scheduled'])
dep=defaultdict(lambda: Counter())
for r in rows:
    dep[r['Department']]['present']+=int(r['Present']); dep[r['Department']]['absent']+=int(r['Absent']); dep[r['Department']]['leave']+=int(r['Leave']); dep[r['Department']]['scheduled']+=int(r['Scheduled'])
summary={
 'synthetic':True,'rows':len(rows),'employees':len({r['EmployeeID'] for r in rows}),'scheduled':scheduled,'present':present,'absent':absent,'leave':leave,'late':late,
 'attendance_rate':round(present/scheduled*100,1),'absence_rate':round(absent/scheduled*100,1),'leave_rate':round(leave/scheduled*100,1),
 'monthly':[{'period':k,**v} for k,v in sorted(monthly.items())],
 'departments':[{'name':k,**v,'rate':round(v['present']/v['scheduled']*100,1)} for k,v in sorted(dep.items())]
}
(root/'data/summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({'summary':str(root/'data/summary.json'),'rows':len(rows),'attendance_rate':summary['attendance_rate']}))
