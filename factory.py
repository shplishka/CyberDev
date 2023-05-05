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
    sub_domain_list:List[str] = vt_client.get_sub_domains(domain_name)
    return [Domain(name=subdomain,
                    technologies=wp_client.get_technologies(subdomain)) 
                    for subdomain in sub_domain_list]

def create_app():
    app = FastAPI()
    app.include_router(router)
    return app