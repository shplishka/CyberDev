from config import configuration
from typing import List
from app.schemes import Domain
from fastapi import FastAPI,APIRouter
from app.client import VirustotalClient,WappalyzerClient

setting = configuration
router = APIRouter()
vt_client = VirustotalClient(setting.virustotal_base_url,setting.virustotal_api_key)
wp_client = WappalyzerClient(setting.wappalyzer_base_url,setting.wappalyzer_api_key)

@router.get("/")
async def root():
    return {"message": "Hello Cyber!"}

@router.get("/scan",response_model=List[Domain])
def scan_subdomains_technologies(domain_name:str)->List[Domain]:
    sub_domain_list: List[str] = vt_client.get_sub_domains(domain_name)
    domain_info_list: List[Domain] = []
    for sub_domain in sub_domain_list:
        technologies_list = wp_client.get_technologies(sub_domain)
        for technology in technologies_list:
            domain_info = Domain(name=sub_domain, technology=technology)
            domain_info_list.append(domain_info)
    return domain_info_list

def create_app():
    app = FastAPI()
    app.include_router(router)
    return app