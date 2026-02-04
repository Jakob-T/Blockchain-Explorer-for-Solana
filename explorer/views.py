from django.shortcuts import render
from django.http import JsonResponse
from .solana_rpc import rpc_call

def home(request):
    slot = rpc_call("getSlot")
    return JsonResponse({"network": "devnet", "current_slot": slot})