import requests
from pydantic import AnyHttpUrl
from requests import Response
from fastapi import HTTPException,status
from typing import List

TECHNOLOGIES_LOOKUP_END_POINT: str = f'lookup'

class WappalyzerClient:
    def __init__(self,wappalyzer_url:AnyHttpUrl,api_key):
        self._wappalyzer_base_url = wappalyzer_url
        self._api_key = api_key

    def get_technologies(self,domain_name:str)->List[str]:
          get_technologies_url = self._generate_full_api_v1_url(TECHNOLOGIES_LOOKUP_END_POINT)
          headers = {'x-api-key': self._api_key,'urls' : domain_name}
          # wappalyzer_api_response: Response = requests.get(get_technologies_url,headers=headers,)
          wappalyzer_api_response = response_mock
          return wappalyzer_api_response['technologies']

        
    def _generate_full_api_v1_url(self,endpoint:str):
        return f'{self._wappalyzer_base_url}/v2/{endpoint}'
    



response_mock = {
  "url": "https://www.wappalyzer.com",
  "technologies": ['azure','vue','node'],
  "email": [ "hello@wappalyzer.com", "elbert@wappalyzer.com" ],
  "verifiedEmail": [ "hello@wappalyzer.com", "elbert@wappalyzer.com" ],
  "safeEmail": [ "elbert@wappalyzer.com" ],
  "phone": [ "+974" ],
  "linkedin": [ "company/wappalyzer", "in/elbertalias" ],
  "twitter": [ "Wappalyzer" ],
  "facebook": [ "wappalyzer" ],
  "title": "Find out what websites are built with",
  "description": "Find out the technology stack of any website.",
  "companyName": "Wappalyzer",
  "inferredCompanyName": "WAPPALYZER",
  "industry": "Internet",
  "about": "Wappalyzer uncovers the technologies used on websites.",
  "locations": [ "Melbourne, VIC 3000, AU" ],
  "companySize": "2-10 employees",
  "companyType": "Privately Held",
  "companyFounded": 2008,
  "employees": [
    {
      "name": "Elbert Alias",
      "title": "Founder of Wappalyzer"
    }
  ],
  "keywords": [ "WAPPALYZER", "TECHNOLOGY", "WEBSITES" ],
  "technologySpend": "Medium",
  "schemaOrgTypes": [ "WebPage", "Organization" ],
  "certInfo.issuer": "Amazon",
  "certInfo.validTo": 1633737600,
  "certInfo.protocol": "TLS 1.3",
  "dns.spf": "true",
  "dns.dmarc": "true",
  "ipCountry": "US",
  "ipRegion": "WA",
  "language": "en",
  "responsive": "true"
}