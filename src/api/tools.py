from datetime import datetime
import logging
from langchain_valyu import ValyuSearchTool
from langgraph.prebuilt import create_react_agent
from src.config import settings
from valyu import Valyu

from models.core.react_agent.holistic_ai_bedrock import get_chat_model
from src.models import (
    ClaimsAnalysisResponse,
    Content,
    ContentExtractionRequest,
    EntityAnalysisResponse,
    ResearchResponse,
)

logger = logging.getLogger(__name__)

# Create search tool with configuration
search_tool = ValyuSearchTool(valyu_api_key=settings.VALYU_API_KEY)
valyu_client = Valyu(api_key=settings.VALYU_API_KEY)

llm = get_chat_model("claude-3-5-sonnet")
research_agent = create_react_agent(
    llm,
    tools=[search_tool],  # Add the search tool!
    response_format=ResearchResponse,
)


async def get_entities(prompt: str) -> EntityAnalysisResponse:
    llm = get_chat_model("claude-3-5-sonnet")

    # Create LLM with structured output
    llm_structured = llm.with_structured_output(EntityAnalysisResponse)

    start_time = datetime.now()
    result = llm_structured.invoke(prompt)
    elapsed = datetime.now() - start_time
    logging.info(f"Entity Analysis Result (took {elapsed.total_seconds():.2f} seconds)\n")

    return result


async def extract_claims(prompt: str) -> ClaimsAnalysisResponse:
    logger.info("Starting claim extraction...\n")
    llm = get_chat_model("claude-3-5-sonnet")
    llm_structured_claims = llm.with_structured_output(ClaimsAnalysisResponse)

    result = llm_structured_claims.invoke(prompt)
    logger.info("Claim Extraction complete\n")
    return result


async def research(prompt: str) -> ResearchResponse:
    logger.info("Starting research...\n")
    result = research_agent.invoke({"messages": [prompt]})

    message = result["structured_response"]

    logger.info("Research complete\n")

    return ResearchResponse.model_validate(message)


async def content_extractor(url: str) -> Content:
    """Extract content from a given URL using Valyu tool."""
    logger.info(f"Extracting content from URL: {url}")
    query = ContentExtractionRequest(urls=[url])
    response = valyu_client.contents(**query)

    results = response.results[0]

    content = Content(
        title=results.title,
        url=results.url,
        content=results.content,
        summary=results.summary,
    )

    logger.info("Content extraction complete.")
    return content
