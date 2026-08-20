import whois

def run(target):
    try:
        data = whois.whois(target)
        return {"module": "whois", "status": "ok", "data": data}
    except Exception as e:
        return {"module": "whois", "status": "error", "error": str(e)}


