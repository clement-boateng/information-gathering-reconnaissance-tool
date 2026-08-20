from ping3 import ping

def run(target):
    try:
        response_time = ping(target, timeout=3)
        if response_time is None:
            return {"module": "ping", "status": "error", "error": "No response (timeout or blocked)"}
        return {"module": "ping", "status": "ok", "data": {"response_time_ms": round(response_time * 1000, 2)}}
    except Exception as e:
        return {"module": "ping", "status": "error", "error": str(e)}
