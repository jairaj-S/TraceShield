from fastapi import FastAPI

app = FastAPI(title="SupplyChain Sentinel")

@app.get("/health")
def health():
    return {"status": "ok"}
