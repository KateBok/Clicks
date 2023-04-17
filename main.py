from dotenv import load_dotenv
from urllib.parse import urlparse
import requests
import os


def shorten_link(token, url):
    address = "https://api-ssl.bitly.com/v4/shorten"
    params = {"long_url": url}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(address, json=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["link"]


def count_clicks(token, bitlink):
    address_click = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    params = {"unit": "month", "units": "-1"}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(address_click, params=params, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()
    return clicks_count["total_clicks"]


def is_bitlink(token, url):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(bit_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
    parsed_url = urlparse(link)
    parsed_url = f"{parsed_url.netloc}{parsed_url.path}"
    try:
        if is_bitlink(token, parsed_url):
            print(count_clicks(token, parsed_url))
        else:
            print(shorten_link(token, link))
    except requests.exceptions.HTTPError as error:
        print("У вас возникла ошибка", error)


if __name__ == "__main__":
    link = input("Введите ссылку: ")
    main()
