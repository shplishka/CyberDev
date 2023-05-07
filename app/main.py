from .setting import config
from .schemes import Domain
from .client import VirustotalClient, WappalyzerClient
from .database import Base, SessionLocal, engine, save_domain_info
from fastapi import FastAPI, APIRouter, Depends
from typing import List

Base.metadata.create_all(bind=engine)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


setting = config
router = APIRouter()
vt_client = VirustotalClient(
    setting.virustotal_base_url, setting.virustotal_api_key)
wp_client = WappalyzerClient(
    setting.wappalyzer_base_url, setting.wappalyzer_api_key)


@router.get("/")
async def root():
    return {"message": "Hello Cyber!"}


@router.get("/scan", response_model=List[Domain])
def scan_subdomains_technologies(domain_name: str, save_mode: bool = True, db=Depends(db)) -> List[Domain]:
    sub_domain_list: List[str] = vt_client.get_sub_domains(domain_name)
    domain_info_list: List[Domain] = []
    for sub_domain in sub_domain_list:
        technologies_list = wp_client.get_technologies(sub_domain)
        for technology in technologies_list:
            domain_info = Domain(name=sub_domain, technology=technology)
            domain_info_list.append(domain_info)
            if save_mode:
                save_domain_info(db, domain_info)
    return domain_info_list


app = FastAPI()
app.include_router(router)
