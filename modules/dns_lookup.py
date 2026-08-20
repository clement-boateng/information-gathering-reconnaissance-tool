import dns.resolver

def run(target):
    try:
        records = {}
        for rtype in ["A", "MX", "NS", "TXT"]:
            try:
                answers = dns.resolver.resolve(target, rtype)
                records[rtype] = [str(r) for r in answers]
            except dns.resolver.NoAnswer:
                records[rtype] = []
            except dns.resolver.NXDOMAIN:
                return {"module": "dns", "status": "error", "error": "Domain does not exist"}
        return {"module": "dns", "status": "ok", "data": records}
    except Exception as e:
        return {"module": "dns", "status": "error", "error": str(e)}
        

