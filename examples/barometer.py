"""Read the current Bitcoin Barometer Heat Score (stdlib only)."""
import json
import urllib.request

URL = "https://nakamotonotes.com/open/barometer.json"

with urllib.request.urlopen(URL, timeout=10) as resp:
    # A 503 raises HTTPError: no reading is better than a stale one.
    data = json.load(resp)

print(f"Heat Score {data['score']}/100, {data['zone']} zone (computed {data['computedAt']})")
