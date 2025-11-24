import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# simulate IO bound task
def fetch_status(url: str, timeout: int = 5) -> dict:
    try:
        response = requests.get(url, timeout=timeout)
        return {"url": url, "status": response.status_code, "error": None}
    except Exception as e:
        return {"url": url, "status": None, "error": str(e)}

# URL list
urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://example.com",
    "https://invalid.url.that.does.not.exist",
    "https://httpbin.org/status/404"
]

# leverage ThreadPoolExecutor
def main():
    start = time.time()
    
    # create thread pool（with statement ensures the pool is properly closed when done）
    with ThreadPoolExecutor(max_workers=3) as executor:
        # submit tasks, return a dict of future to url
        future_to_url = {
            executor.submit(fetch_status, url): url for url in urls
        }

        # process results in the order they complete（first completed first processed）
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result(timeout=10)  # wait for result at most 10 seconds
                if result["error"]:
                    print(f"{url} failed: {result['error']}")
                else:
                    print(f"{url} return status code: {result['status']}")
            except Exception as exc:
                print(f"{url} raise exception: {exc}")

    print(f"\nAll tasks are done, total time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()