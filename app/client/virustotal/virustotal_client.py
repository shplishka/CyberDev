import requests
from fastapi import HTTPException,status
from pydantic import AnyHttpUrl
from requests import Response
from typing import List

DOMAIN_REPORT_END_POINT: str = f'domain/report'

class VirustotalClient:
    def __init__(self,virustotal_url:AnyHttpUrl,api_key):
        self._virustotal_base_url = virustotal_url
        self._api_key = api_key

    def get_sub_domains(self,domain_name:str)->List[str]:
        get_sub_domains_url = self._generate_full_api_v1_url(DOMAIN_REPORT_END_POINT)
        domain_request = {'apikey':self._api_key,'domain':domain_name} #TODO:shit code
        virustotal_api_response: Response = requests.get(get_sub_domains_url,domain_request)
        if virustotal_api_response.json()['response_code'] == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'domain: {domain_name} not found')
        else:
            if len(virustotal_api_response.json()['domain_siblings'])==0:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                                detail=f' sub domains: {domain_name} not found')
            else:
                return virustotal_api_response.json()['domain_siblings']

    def _generate_full_api_v1_url(self,endpoint:str):
        return f'{self._virustotal_base_url}/vtapi/v2/{endpoint}'