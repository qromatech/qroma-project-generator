import requests


def check_file_contains_string(file_location, expected_str):
    with open(file_location) as f:
        return expected_str in f.read()


def check_url_content_has_strings(url, expected_strs):
    url_content = requests.get(url)
    print(url_content)
