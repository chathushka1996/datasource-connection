from pydantic import BaseModel


class Credentials(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str
    
class SourceCreateRequest(BaseModel):
    sourceId: str
    credentials: Credentials

