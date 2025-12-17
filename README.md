# Threat Recon Tool

A **passive reconnaissance tool** for Cyber Threat Intelligence (CTI) that collects publicly available information about a domain and maps findings to **MITRE ATT&CK techniques**.  
Perfect for threat intelligence, reconnaissance, and portfolio demonstration.

---

## ⚡ Features

- DNS enumeration (A, AAAA, MX, TXT, NS records)
- WHOIS lookup (registrar, domain owner emails)
- Subdomain discovery (crt.sh certificate transparency)
- SSL certificate inspection (issuer, expiration, SANs)
- HTTP technology fingerprinting (Server, X-Powered-By, CMS detection)
- Automatic mapping of findings to MITRE ATT&CK techniques
- JSON output for easy reporting and integration
- Fully passive (no intrusive scanning)

---

## 💻 Installation

```bash
git clone https://github.com/yourusername/threat-recon.git
cd threat-recon
pip install -r requirements.txt
```
## 🏁 Usage

```bash 
python main.py --domain example.com --output report.json
```
Optional: omit --output to print JSON to console.

## 📦 Example Output

```json
{
  "domain": "example.com",
  "findings": [
    {
      "type": "dns_a",
      "value": "93.184.216.34",
      "mitre": "T1590 - Gather Victim Network Information"
    },
    {
      "type": "subdomain_enum",
      "value": "mail.example.com",
      "mitre": "T1590.002 - Gather Victim Network Information"
    },
    {
      "type": "ssl_certificate",
      "issuer": {"organizationName": "DigiCert Inc"},
      "subject": {"commonName": "example.com"},
      "notBefore": "Jan 1 00:00:00 2025 GMT",
      "notAfter": "Dec 31 23:59:59 2025 GMT",
      "san": ["example.com", "www.example.com"],
      "mitre": "T1590 - Gather Victim Network Information"
    },
    {
      "type": "http_fingerprint",
      "status": 200,
      "tech": ["Server: nginx", "WordPress detected"],
      "mitre": "T1592 - Gather Victim Host Information"
    }
  ]
}
```

## 🛡️ Legal & Ethics Disclaimer

This tool only performs passive reconnaissance using publicly available information:

DNS queries

WHOIS lookups

Public certificate data

HTTP headers

Do not use it for unauthorized access, active scanning, or exploitation.
Always respect local laws and privacy regulations.

## 🔧 MITRE ATT&CK Mapping

| Finding Type          | MITRE Technique |
| --------------------- | --------------- |
| DNS Lookup            | T1590           |
| Subdomain Enumeration | T1590.002       |
| WHOIS Information     | T1589           |
| SSL Certificate Info  | T1590           |
| HTTP Fingerprinting   | T1592           |

## 🛠️ Future Improvements

Configurable recon modules (enable/disable per run)

Additional fingerprinting heuristics (CMS, JS frameworks)

Optional breach/exposure checks (API-based, authorized)

PDF/HTML report generation

Logging & timestamped findings