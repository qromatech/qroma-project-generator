import requests
import json


def check_file_contains_string(file_location, expected_str):
    with open(file_location) as f:
        return expected_str in f.read()


def check_url_content_has_strings(url, expected_strs):
    response = requests.get(url)
    content = response.text

    missing_strings = []
    for s in expected_strs:
        if s not in content:
            missing_strings.append(s)

    if len(missing_strings) > 0:
        print(f"Missing strings for check_url_content_has_strings() at URL {url}")
        print(missing_strings)
        return False

    return True


def check_url_content_exists_with_size(url, size_minimum):
    response = requests.get(url)
    content = response.content

    assert content is not None

    if len(content) < size_minimum:
        print(url, len(content))
        return False

    return True


def check_url_json_matches_dict(url, expected_dict):
    response = requests.get(url)
    content_json = response.json()

    # expected_json = json.loads(expected_json_str)

    if content_json == expected_dict:
        return True

    print(content_json)
    print(expected_dict)

    return False


