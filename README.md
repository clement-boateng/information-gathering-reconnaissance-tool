# **Information Gathering Tool**

*A modular Python reconnaissance automation tool*

 **Overview**

InfoGather is a command-line reconnaissance tool built in Python. It accepts a domain name or an IP address as the target then gathers publicly available information from a single run rather than running several separate tools one after the order.

The user decides to run all tools or select exactly which ones they want to run from a simple menu.

# **Features**

●       Domain ownership lookup (WHOIS)

●       DNS record lookup (A, MX, NS, TXT)

●       Website connectivity check (ping / response time)

●       Website technology detection

●       Public email address finder (scans the target's own pages)

●       Menu-driven module selection (user can decide to run all / selected modules)

●       Automatic, timestamped, saved text report for every run

●       No paid APIs or API keys required

# **Requirements**

●       Python 3.9 or later

●       pip

●       Administrator / root privileges (for ping module to run)

# **Installation**

1. Clone the repository:

git clone https://github.com/<your-username>/infogather-tool.git cd infogather-tool

2. Create a virtual environment:

python3 -m venv venv

3. Activate the virtual environment:

source venv/bin/activate

4. Install the required packages:

pip install -r requirements.txt

# **Usage**

Run the tool from the project's root folder:

# Linux / macOS (sudo required for the ping module) sudo venv/bin/python3 recon.py

You'll be prompted for a target, then shown a menu of available modules:

Enter target (domain or IP): example.com

Select modules to run:

[1] Domain Registration Info

[2] Domain Server Records

[3] Website Connectivity Check

[4] Public Email Address Finder

[5] Website Technology Detection

[0] All Enter numbers (separated by comma) or 0 for all:

Enter number(s), separated by comma (e.g. 1,3,5), or 0 to run every module. Only the modules selected will run. Once finished, results are saved automatically to recon_report_<target>.txt in the project folder.

# **Project Structure**

#

# **How Each Module Works**

●       whois_lookup.py: Queries WHOIS servers directly to retrieve domain registration details (registrar, creation/expiry dates, name servers).

●       dns_lookup.py: Resolves A, MX, NS, and TXT DNS records for the target.

●       ping_check.py:  Sends a single ping and measures round-trip response time in milliseconds.

●       tech_detect.py: Sends an HTTP request and reads the Server and X-Powered-By response headers to identify the web technology in use.

●       email_harvest.py: Fetches the target's homepage and common inner pages (/contact, /about, /team) and searches the raw HTML for publicly published email addresses belonging to the target's domain.

●       report.py: Collects the results from every module that ran and writes them into a single, timestamped, saved text report.

# **Limitations**

●       The email finder only detects addresses published as plain text in a page's HTML. Addresses shown as images, assembled by JavaScript after the page loads, or hidden behind a contact form are not detected.

●       WHOIS results vary by domain, since many registrars mask contact details behind privacy protection.
