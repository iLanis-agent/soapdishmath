import json, math

def r0(x): return math.floor(x + 0.5)
def r1(x): return math.floor(x * 10 + 0.5) / 10
def r2(x): return math.floor(x * 100 + 0.5) / 100
def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(n) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))

def life_plan(barG, gPerWash, washesPerDay):
    if not (barG > 0) or not (gPerWash > 0) or not (washesPerDay > 0):
        return {"error": "bar, wash and washes must be positive"}
    return {"washes": r0(barG / gPerWash), "days": r0(barG / gPerWash / washesPerDay)}

def year_plan(daysPerBar, priceBar):
    if not (daysPerBar > 0) or not (priceBar > 0):
        return {"error": "days and price must be positive"}
    return {"barsYear": jsnum(r1(365 / daysPerBar)), "costYear": jsnum(r2(365 / daysPerBar * priceBar))}

def bottle_plan(bottleMl, mlPerPump, pumpsPerDay):
    if not (bottleMl > 0) or not (mlPerPump > 0) or not (pumpsPerDay > 0):
        return {"error": "bottle, pump and pumps must be positive"}
    return {"pumps": r0(bottleMl / mlPerPump), "days": r0(bottleMl / mlPerPump / pumpsPerDay)}

def render_life(r, barG, gPerWash, washesPerDay):
    return ("A " + fmt(barG) + " g bar at a labeled " + fmt(gPerWash) + " g a wash, "
            + plural(washesPerDay, "wash", "washes") + " a day, lasts about " + plural(r["days"], "day")
            + " - " + plural(r["washes"], "wash", "washes") + " in all.")

def render_year(r, daysPerBar, priceBar):
    return ("At " + plural(daysPerBar, "day") + " a bar that is " + fmt(r["barsYear"])
            + " bars a year - " + fmt(r["costYear"]) + " at " + fmt(priceBar) + " each.")

def render_bottle(r, bottleMl, mlPerPump, pumpsPerDay):
    return ("A " + fmt(bottleMl) + " ml bottle at a labeled " + fmt(mlPerPump) + " ml a pump, "
            + plural(pumpsPerDay, "pump") + " a day, lasts about " + plural(r["days"], "day")
            + " - " + plural(r["pumps"], "pump") + " in all.")

cases = []
for barG, gPerWash, washesPerDay in [(100, 0.5, 6), (150, 0.6, 4), (75, 0.4, 8), (0, 0.5, 6)]:
    r = life_plan(barG, gPerWash, washesPerDay)
    cases.append({"fn": "lifePlan", "args": [barG, gPerWash, washesPerDay], "result": r,
                  "render": None if "error" in r else render_life(r, barG, gPerWash, washesPerDay)})
for daysPerBar, priceBar in [(33, 3.99), (62, 4.5), (23, 2.75), (0, 3.99)]:
    r = year_plan(daysPerBar, priceBar)
    cases.append({"fn": "yearPlan", "args": [daysPerBar, priceBar], "result": r,
                  "render": None if "error" in r else render_year(r, daysPerBar, priceBar)})
for bottleMl, mlPerPump, pumpsPerDay in [(500, 2, 6), (300, 1.5, 10), (1000, 2.5, 4), (0, 2, 6)]:
    r = bottle_plan(bottleMl, mlPerPump, pumpsPerDay)
    cases.append({"fn": "bottlePlan", "args": [bottleMl, mlPerPump, pumpsPerDay], "result": r,
                  "render": None if "error" in r else render_bottle(r, bottleMl, mlPerPump, pumpsPerDay)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
