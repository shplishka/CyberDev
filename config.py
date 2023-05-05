from pydantic import BaseSettings

class Config(BaseSettings):
    virustotal_base_url:str = 'https://www.virustotal.com'
    virustotal_api_key:str = '2d546dfdc96873970d71eb76f81e463d084321f44ce1016629ec3773667cdfd8'
    wappalyzer_base_url:str = 'https://api.wappalyzer.com'
    wappalyzer_api_key:str = 'TWLNY1MK1KmMZvh1dS9H6WGfyZLLBGx2lDBsqHz8'

configuration = Config()