# Threat Recon

A passive reconnaissance + MITRE ATT&CK mapping tool for Cyber Threat Intelligence.

## Usage

python main.py --domain example.com --output report.json

## Example Output

```json
{
    "domain": "example.com",
    "findings": [
        {
            "type": "dns_a",
            "value": "93.184.216.34",
            "mitre": "T1590 - Gather Victim Network Information"
        }
    ]
}
```