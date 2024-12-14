# Domain shadow IT discovery with usage of certificates

Shadow IT discovery, not all corporate sites with domain maines are govern properly and track in CMDB, this is a method how to discover at least some of them.

## Links

<https://data.iana.org/TLD/tlds-alpha-by-domain.txt>

<https://crt.sh/>

## Usage

* Download TLD with `get_TLD.sh`
* Collect cert data with `cert2domains.py`
* Get list of rate limited attempts with `get_rate_limited_TLDS.sh > TLD.txt`
* Collect cert data with `cert2domains.py`
* Get uniq domains `get_uniq_hostnames.py > hostnames.txt`

Note: Adjust `CERT_INFO_FOLDER` and `DOMAIN` constants in the scripts.
