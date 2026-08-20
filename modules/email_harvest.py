import re
import requests

def run(target):
    try:
        url = target
        if not url.startswith("http"):
            url = f"http://{target}"

        pages_to_check = [url, f"{url}/contact", f"{url}/about", f"{url}/team"]

        found_emails = set()
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        for page in pages_to_check:
            try:
                response = requests.get(page, timeout=5)
                matches = re.findall(email_pattern, response.text)
                for match in matches:
                    if target in match:
                        found_emails.add(match)
            except requests.exceptions.RequestException:
                continue

        return {"module": "email_harvest", "status": "ok", "data": {"emails_found": list(found_emails)}}

    except Exception as e:
        return {"module": "email_harvest", "status": "error", "error": str(e)}


