from sqlalchemy.orm import Session
from ..schemes import Domain
from ..models import DomainInfo

def save_domain_info(db: Session, info: Domain):
    domain_info_model = DomainInfo(**info.dict())
    db.add(domain_info_model)
    db.commit()
    db.refresh(domain_info_model)
    return domain_info_model