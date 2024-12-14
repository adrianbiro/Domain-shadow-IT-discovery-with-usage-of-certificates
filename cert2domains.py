import pathlib
import time

import requests


def fetch(domain: str, timeout: int | float, path: pathlib.Path) -> None:
    p = path.joinpath(f"{domain}.json")
    try:
        response = requests.get(
            url="https://crt.sh/json", params={"q": domain}, timeout=timeout
        )
        with open(str(p), mode="wb") as f:
            f.write(response.content)

    except requests.exceptions.ReadTimeout as e:
        print(e)
        with open(str(p), mode="w", encoding="utf-8") as f:
            f.write(str(e))


def domain_wil_all_tld(domain:str, tld_file_path: str) -> list[str]:
    with open(tld_file_path, "r", encoding="utf-8") as f:
        tlds = [i for i in f.readlines() if not i.startswith("#")]
    return [f"{domain}.{tld.strip('\n')}" for tld in tlds]


DOMAIN = "<REPLACE_ME>"
CERT_INFO_FOLDER = f"cert_info_{DOMAIN}"
TIMEOUT_REQUEST = 30
SLEEP_BETWEEN_BATCHES = 30
BATCH_SIZE = 25
SLEEP_TIME_AFTER_REQUEST = 1.5
TLD_FILE_PATH = "TLD.txt"

def main():
    domains = domain_wil_all_tld(domain=DOMAIN, tld_file_path=TLD_FILE_PATH)
    p = pathlib.Path(CERT_INFO_FOLDER)
    p.mkdir(parents=True, exist_ok=True)

    
    start, stop = 0, BATCH_SIZE
    while True:
        if not (_domains:= domains[start:stop]):
            break
        for d in _domains:
            print(d)
            fetch(domain=d, timeout=TIMEOUT_REQUEST, path=p)
            time.sleep(SLEEP_TIME_AFTER_REQUEST)
        start += BATCH_SIZE + 1
        stop += BATCH_SIZE + 1

        print(f"{SLEEP_BETWEEN_BATCHES=}")
        time.sleep(SLEEP_BETWEEN_BATCHES)


if __name__ == "__main__":
    raise SystemExit(main())
