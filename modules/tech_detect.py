import requests

def run(target):
    try:
        url = target
        if not url.startswith("http"):
            url = f"http://{target}"

        response = requests.get(url, timeout=5)

        tech_info = {
            "server": response.headers.get("Server", "unknown"),
            "powered_by": response.headers.get("X-Powered-By", "unknown"),
            "status_code": response.status_code,
        }

        return {"module": "tech_detect", "status": "ok", "data": tech_info}
    except Exception as e:
        return {"module": "tech_detect", "status": "error", "error": str(e)}


