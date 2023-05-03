from src.api_keys import KEYS
from sec_api import FullTextSearchApi

fullTextSearchApi = FullTextSearchApi(api_key=KEYS.SEC_API_KEY)

query = {
  "query": '"LPCN 1154"',
  "formTypes": ['8-K', '10-Q'],
  "startDate": '2021-01-01',
  "endDate": '2021-06-14',
}

filings = fullTextSearchApi.get_filings(query)

print(filings)
