# ============================================
# Technic Parse
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 1/29/23
# License: MIT
# ============================================

import argparse
import requests

def parse_args():
    parser = argparse.ArgumentParser(
        description='Technic Parser')
    parser.add_argument('-s', '--search', type=str, required=True, metavar="search", help='Parse Technic Search and give download URL.')
    args = parser.parse_args()
    return args

def download_manifest(search):
    url = "https://api.technicpack.net/search?q=" + search
    params = {
    'build': 'build',
    }
    responce = requests.get(url, params=params)
    json = responce.json()
    for pack in json["modpacks"]:
        url2 = "https://api.technicpack.net/modpack/" + pack["slug"]
        params2 = {
        'build': 'build',
        }
        responce = requests.get(url2, params=params)
        json2 = responce.json()
        finalURL = json2["url"]
        if finalURL == None:
            finalURL = "SOLDER MODPACK"
        print("{}: {}".format(pack["slug"], finalURL))
    if json["modpacks"] == []:
        print("No Results")
if __name__ == "__main__":
    download_manifest(parse_args().search)