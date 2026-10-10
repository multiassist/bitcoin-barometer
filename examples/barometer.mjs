// Read the current Bitcoin Barometer Heat Score (Node 18+ or any browser).
const res = await fetch('https://nakamotonotes.com/open/barometer.json');
if (!res.ok) throw new Error(`Barometer unavailable: HTTP ${res.status}`);
const data = await res.json();
console.log(`Heat Score ${data.score}/100, ${data.zone} zone (computed ${data.computedAt})`);
