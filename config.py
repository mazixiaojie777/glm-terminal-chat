import os
from pathlib import Path

from dotenv import load_dotenv


def load_config():
    load_dotenv(Path(__file__).resolve().with_name(".env"))

    api_key = os.getenv("BIGMODEL_API_KEY")
    url = os.getenv("BIGMODEL_API_URL")
    model = os.getenv("BIGMODEL_MODEL")

    if not api_key:
        raise SystemExit("缺少 BIGMODEL_API_KEY，请检查 .env。")
    if not url:
        raise SystemExit("缺少 BIGMODEL_API_URL，请检查 .env。")
    if not model:
        raise SystemExit("缺少 BIGMODEL_MODEL，请检查 .env。")

    return api_key, url, model