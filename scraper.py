import requests

def scrape_remoteok(keyword="python"):
    url = "https://remoteok.com/api"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        jobs = []
        for job in data[1:]:  # First item is metadata
            if keyword.lower() in job['position'].lower():
                jobs.append({
                    "Title": job["position"],
                    "Company": job["company"],
                    "Location": job.get("location", "Not specified")
                })

        return jobs

    except Exception as e:
        print(f"Scraping error: {e}")
        return []
