from modules import whois_lookup, dns_lookup, ping_check, tech_detect, email_harvest, report

MODULES = {
    "1": ("Domain Registration Info", whois_lookup),
    "2": ("Domain Server Records", dns_lookup),
    "3": ("Website Connectivity Check", ping_check),
    "4": ("Public Email Address Finder", email_harvest),
    "5": ("Website Technology Detection", tech_detect),
}

def show_menu():
    print("\nSelect modules to run:")
    for key, (name, _) in MODULES.items():
        print(f"[{key}] {name}")
    print("[0] All")

def get_selection():
    show_menu()
    choice = input("Enter numbers (separated by comma) or 0 for all: ").strip()
    if choice == "0":
        return list(MODULES.keys())
    return [c.strip() for c in choice.split(",") if c.strip() in MODULES]

def run_modules(target, selected_keys):
    results = []
    for key in selected_keys:
        name, module = MODULES[key]
        print(f"\nRunning {name}...")
        result = module.run(target)
        results.append(result)
        print(result)

    print("\n--- Summary ---")
    for r in results:
        print(f"{r['module']}: {r['status']}")

    report.generate(target, results)

def main():
    target = input("Enter target (domain or IP): ").strip()

    while True:
        selected_keys = get_selection()

        if not selected_keys:
            print("No valid modules selected. Try again.")
            continue

        run_modules(target, selected_keys)

        print("\nWhat would you like to do next?")
        print("[m] Back to module menu (same target)")
        print("[n] Enter a new target")
        print("[q] Quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "m":
            continue
        elif choice == "n":
            target = input("Enter target (domain or IP): ").strip()
            continue
        else:
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
