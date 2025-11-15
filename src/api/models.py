
from typing import List
from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str

class AnalyseArticleRequest(BaseModel):
    article: str

class BiasAnalysisResponse(BaseModel):
    summary: str
    entities: List[str]