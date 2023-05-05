from .setting import config
from .schemes import Domain
from .client import VirustotalClient,WappalyzerClient
import models
from .database import SessionLocal, engine
from database.database import save_domain_info
from fastapi import FastAPI,APIRouter,Depends
from typing import List

models.Base.metadata.create_all(bind=engine)

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

setting = config
router = APIRouter()
vt_client = VirustotalClient(setting.virustotal_base_url,setting.virustotal_api_key)
wp_client = WappalyzerClient(setting.wappalyzer_base_url,setting.wappalyzer_api_key)

@router.get("/")
async def root():
    return {"message": "Hello Cyber!"}

@router.get("/scan",response_model=List[Domain],db=Depends(db))
def scan_subdomains_technologies(domain_name:str)->List[Domain]:
    sub_domain_list:List[str] = vt_client.get_sub_domains(domain_name)
    save_domain_info(db,**Domain(name='sds',technologies=['a','a']))
    return [Domain(name=subdomain,
                    technologies=wp_client.get_technologies(subdomain)) 
                    for subdomain in sub_domain_list]

app = FastAPI()
app.include_router(router)