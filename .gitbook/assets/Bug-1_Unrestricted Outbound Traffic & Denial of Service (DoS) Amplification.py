import requests

def execute_requests(input_url):
    if input_url and isinstance(input_url, str) and len(input_url.strip()) > 0:
        target = input_url.strip()
    else:
        target = "https://webhook.site/0698b39e-c6ca-4f08-a02b-14ceb53b4b63"

    success_count = 0
    total_requests = 10
    logs = []
    results = {
        "status": "Starting",
        "target": target
    }

    for i in range(1, total_requests + 1):
        try:
            response = requests.get(target, timeout=2)

            if response.status_code == 200:
                success_count += 1

            if i > (total_requests - 5):
                logs.append(f"Req {i}: {response.status_code}")

        except Exception as e:
            if i > (total_requests - 5):
                logs.append(f"Req {i}: Failed")

    summary_msg = f"Sent: {total_requests} | Success (200 OK): {success_count}"

    return {
        "scan_results": summary_msg + "\nDetails:\n" + "\n".join(logs)
    }


# this is our script we will be using for testing