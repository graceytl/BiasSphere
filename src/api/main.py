from fastapi.routing import APIRouter

from src.api.agent import MediaAgent
from src.api.tools import research
from src.models import Claim, ClaimsAnalysisResponse, EntityAnalysisResponse, MediaSummary, ResearchResponse
from src.utils import get_prompt

router = APIRouter(prefix="/api")


@router.get("/")
def get_root():
    return {"message": "Hello from BiasSphere API."}


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/extract/entities")
async def extract_entities(article: str) -> EntityAnalysisResponse:
    search_prompt = get_prompt("ENTITY_EXTRACTION_PROMPT").format(article=article)

    agent_response = await extract_entities(search_prompt)
    return agent_response


@router.post("/extract/claims")
async def extract_claims(article: str) -> ClaimsAnalysisResponse:
    search_prompt = get_prompt("CLAIM_EXTRACTION_PROMPT").format(article=article)

    agent_response = await extract_claims(search_prompt)
    return agent_response


@router.post("/research")
async def valyu_search(claim: Claim) -> ResearchResponse:
    search_prompt = get_prompt("RESEARCH_PROMPT").format(claim=claim.claim)

    agent_response = await research(search_prompt)
    return agent_response


@router.post("/analyse")
async def analyse_article(article: str) -> MediaSummary:
    agent = MediaAgent()
    response = await agent.scan_media(article)
    return response
