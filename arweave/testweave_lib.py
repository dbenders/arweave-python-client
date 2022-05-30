import json
import logging
import requests


logger = logging.getLogger(__name__)


API_URL = "https://arweave.net"
NETWORK = None

def mine(api_url=API_URL, network=NETWORK):
    headers = {}
    if network is not None:
        headers["X-Network"] = network

    url = "{}/mine".format(api_url)

    resp = requests.post(url, headers=headers)
    return resp.status_code == 200


def ready_for_mining(txid, api_url=API_URL, network=NETWORK):
    headers = {}
    if network is not None:
        headers["X-Network"] = network

    url = "{}/tx/ready_for_mining".format(api_url)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        txids = json.loads(response.text)
        return txid in txids
    else:
        logger.error(response.text)
        return False
