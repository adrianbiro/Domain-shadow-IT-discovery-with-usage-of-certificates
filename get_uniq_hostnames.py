import json
import pathlib

DOMAIN = "<REPLACE_ME>"
CERT_INFO_FOLDER = f"cert_info_{DOMAIN}"


def main():
    input_files = [i for i in pathlib.Path(CERT_INFO_FOLDER).glob("*.json")]
    hostnames = set()
    for f in input_files:
        with open(f, encoding="utf-8") as f:
            try:
                data = json.load(f)
                for i in data:
                    if not i["common_name"].startswith("*."):
                        hostnames.add(i["common_name"])
            except json.JSONDecodeError:
                ...

    for h in hostnames:
        print(h)



if __name__ == "__main__":
    raise SystemExit(main())    
