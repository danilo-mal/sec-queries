import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())

@dataclass(frozen=True)
class KEYS:
    SEC_API_KEY: str = os.getenv("SEC_API_KEY")
