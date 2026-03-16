from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

@app.get("/signals")
def signals():
    # Return mock trading signals
    sample_signals = [
        {"symbol": "BTCUSD", "action": random.choice(["buy", "sell"]), "confidence": round(random.uniform(0.6, 0.99), 2), "time": datetime.utcnow().isoformat()},
        {"symbol": "ETHUSD", "action": random.choice(["buy", "sell"]), "confidence": round(random.uniform(0.6, 0.99), 2), "time": datetime.utcnow().isoformat()}
    ]
    return {"signals": sample_signals}
