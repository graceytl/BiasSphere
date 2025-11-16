from fastapi.routing import APIRouter

from src.api.models import BiasAnalysisResponse

router = APIRouter(prefix="/api")


@router.get("/")
def get_root():
    return {"message": "Hello from BiasSphere API."}


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/analyse")
def analyse_article(article: str) -> BiasAnalysisResponse:
    # Placeholder for analysis logic
    result = {"analysis": "This is a placeholder analysis result."}
    return result
