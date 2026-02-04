import os
import requests

SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.devnet.solana.com")

class SolanaRPCError(Exception):
    pass

def rpc_call(method: str, params=None, timeout: int = 15):
    if params is None:
        params = []
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    r = requests.post(SOLANA_RPC_URL, json=payload, timeout=timeout)
    r.raise_for_status()
    data = r.json()
    if "error" in data:
        raise SolanaRPCError(data["error"])
    return data["result"]
