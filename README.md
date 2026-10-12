# Bitcoin Barometer: free Heat Score API and widget

The [NakamotoNotes Bitcoin Barometer](https://nakamotonotes.com/bitcoin-barometer) combines 8 Bitcoin indicators into one **Heat Score from 0 to 100** and a zone (Chill, Neutral, Heated, Euphoric). It shows where today's readings sit against their own history. It does not forecast price.

The on-chain inputs (MVRV-Z, NUPL, Puell Multiple) are computed from our own Bitcoin full node, with no on-chain data vendor involved. Method: [nakamotonotes.com/methodology](https://nakamotonotes.com/methodology).

Free to use. No key, no sign-up, HTTPS, CORS open.

## Endpoints

| Endpoint | Returns |
|---|---|
| `GET https://nakamotonotes.com/open/barometer.json` | current score, zone, time computed, indicator readings, `degraded` list |
| `GET https://nakamotonotes.com/open/barometer-history.csv` | daily `date,score,zone` since 2014-01-01 (one row per day, zone written like `Neutral Zone`) |

- Limit: 10 requests per minute per IP. Answers are cached for 5 minutes.
- If a reading cannot be produced, the API answers **503** instead of a number. It never sends a stale or made-up value.
- The history CSV is live and covers every day from 2014-01-01. A few days are carried forward from adjacent readings where an input was missing.

Example response:

```json
{
  "score": 26,
  "heatScore": 0.261,
  "zone": "Neutral",
  "computedAt": "2026-10-12T12:10:18.341Z",
  "degraded": [],
  "indicators": { "monthlyRSI": 53.08, "mayerMultiple": "1.16", "piCycleProximity": 46.3, "mvrvZScore": 0.95, "nupl": 35.61, "puellMultiple": 1.15, "searchInterestHeat": 13 },
  "methodology": "https://nakamotonotes.com/methodology",
  "license": "CC BY 4.0 — attribute NakamotoNotes"
}
```

## Quick start

```bash
curl -s https://nakamotonotes.com/open/barometer.json
```

OpenAPI spec: [`openapi.yaml`](openapi.yaml). More in [`examples/`](examples): [curl](examples/curl.sh), [Python](examples/barometer.py), [JavaScript](examples/barometer.mjs).

## Embed the widget

Paste one line where the widget should appear:

```html
<script src="https://nakamotonotes.com/open/embed.js"></script>
```

Two sizes: card (380 x 470) and compact (340 x 185). Options are documented at [nakamotonotes.com/open](https://nakamotonotes.com/open).

![Bitcoin Barometer widget](widget.png)

## License

- **Data** (feed and CSV): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribute "NakamotoNotes" and link to https://nakamotonotes.com/bitcoin-barometer.
- **Code in this repository**: MIT, see [LICENSE](LICENSE).

## Not financial advice

The Barometer is educational information. It is not a recommendation to buy, sell or hold anything. Bitcoin is volatile; you can lose money.

Daily readings and push alerts when the zone changes are in the free [NakamotoNotes app](https://nakamotonotes.com/mobile-app?utm_source=github).
