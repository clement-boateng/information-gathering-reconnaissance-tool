from datetime import datetime

def generate(target, results):
    lines = []
    lines.append(f"Recon Report for: {target}")
    lines.append(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 40)

    for r in results:
        lines.append(f"\nModule: {r['module']}")
        lines.append(f"Status: {r['status']}")
        if r['status'] == "ok":
            lines.append(f"Data: {r['data']}")
        else:
            lines.append(f"Error: {r['error']}")

    report_text = "\n".join(lines)
    filename = f"recon_report_{target}.txt"

    with open(filename, "w") as f:
        f.write(report_text)

    print(f"\nReport saved to {filename}")
