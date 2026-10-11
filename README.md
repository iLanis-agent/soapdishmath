# Soap dish math

How many days a bar of soap really lasts, what a year of handwashing costs in bars, and how long the pump bottle runs - so the bar-versus-bottle argument gets numbers. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/soapdishmath/

## The three tools

- **Life plan** - `lifePlan(barG, gPerWash, washesPerDay)`: washes and days per bar.
- **Year plan** - `yearPlan(daysPerBar, priceBar)`: bars and cost per year.
- **Bottle plan** - `bottlePlan(bottleMl, mlPerPump, pumpsPerDay)`: pumps and days per bottle.

## Labeled norms (illustrative references, not rules)

- Bar: 100 g. Wash: 0.5 g of soap. Pump: 2 ml. Household: 6 washes a day. Your soap, hands and household decide the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 51 checks)

Regenerate the oracle expectations: `python3 oracle.py`
