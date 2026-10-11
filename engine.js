(function (root) {
  "use strict";
  function r0(x) { return Math.round(x); }
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function lifePlan(barG, gPerWash, washesPerDay) {
    if (!(barG > 0) || !(gPerWash > 0) || !(washesPerDay > 0)) return { error: "bar, wash and washes must be positive" };
    var washes = r0(barG / gPerWash);
    var days = r0(barG / gPerWash / washesPerDay);
    return { washes: washes, days: days };
  }

  function yearPlan(daysPerBar, priceBar) {
    if (!(daysPerBar > 0) || !(priceBar > 0)) return { error: "days and price must be positive" };
    var barsYear = r1(365 / daysPerBar);
    var costYear = r2(365 / daysPerBar * priceBar);
    return { barsYear: barsYear, costYear: costYear };
  }

  function bottlePlan(bottleMl, mlPerPump, pumpsPerDay) {
    if (!(bottleMl > 0) || !(mlPerPump > 0) || !(pumpsPerDay > 0)) return { error: "bottle, pump and pumps must be positive" };
    var pumps = r0(bottleMl / mlPerPump);
    var days = r0(bottleMl / mlPerPump / pumpsPerDay);
    return { pumps: pumps, days: days };
  }

  function renderLife(r, barG, gPerWash, washesPerDay) {
    return "A " + barG + " g bar at a labeled " + gPerWash + " g a wash, " + plural(washesPerDay, "wash", "washes") + " a day, lasts about " + plural(r.days, "day") + " - " + plural(r.washes, "wash", "washes") + " in all.";
  }

  function renderYear(r, daysPerBar, priceBar) {
    return "At " + plural(daysPerBar, "day") + " a bar that is " + r.barsYear + " bars a year - " + r.costYear + " at " + priceBar + " each.";
  }

  function renderBottle(r, bottleMl, mlPerPump, pumpsPerDay) {
    return "A " + bottleMl + " ml bottle at a labeled " + mlPerPump + " ml a pump, " + plural(pumpsPerDay, "pump") + " a day, lasts about " + plural(r.days, "day") + " - " + plural(r.pumps, "pump") + " in all.";
  }

  var api = { lifePlan: lifePlan, yearPlan: yearPlan, bottlePlan: bottlePlan, renderLife: renderLife, renderYear: renderYear, renderBottle: renderBottle };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SoapDishMath = api;
})(this);
