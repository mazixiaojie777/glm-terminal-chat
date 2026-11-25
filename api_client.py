import requests


def send_chat_request(api_key, url, model, messages):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
    }
    return requests.post(url, headers=headers, json=payload, timeout=60)