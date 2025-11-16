from typing import List
from src.api.tools import content_extractor, get_entities, extract_claims, research
from src.models import ClaimsAnalysisResponse, EntityAnalysisResponse, MediaSummary, ResearchResponse
import logging
from opentelemetry import trace
from src.utils import get_prompt

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


class MediaAgent:
    """Agent that analyses media articles for bias and factual accuracy."""

    def __init__(self):
        self.tools = {
            "extract_entities": get_entities,
            "extract_claims": extract_claims,
            "research": research,
        }

    @tracer.start_as_current_span("Scanning Media Articles")
    async def scan_media(self, input: str) -> MediaSummary:
        """Scan media articles for bias and factual accuracy on given content."""

        logger.info("Checking input type (URL or text)...")
        content_obj = None
        if await is_url(input):
            logger.info("Content is a URL, extracting content first.")
            with tracer.start_as_current_span("Extracting Content from URL"):
                content_obj = await content_extractor(input)
                content = content_obj.content
                logging.info("Extracted content title.")
        else:
            content = input

        logger.info("Scanning media articles for content")

        with tracer.start_as_current_span("Extracting Entities"):
            entity_prompt = get_prompt("ENTITY_EXTRACTION_PROMPT").format(article=content)

            entityList: EntityAnalysisResponse = await self.tools["extract_entities"](entity_prompt)

        with tracer.start_as_current_span("Extracting Claims"):
            claim_prompt = get_prompt("CLAIM_EXTRACTION_PROMPT").format(article=content)
            claimsList: ClaimsAnalysisResponse = await self.tools["extract_claims"](claim_prompt)

        relatedFindings: List[ResearchResponse] = []

        with tracer.start_as_current_span("Researching Claims"):
            for claim in claimsList.claims:
                if claim.type == "opinion":
                    research_prompt = get_prompt("RESEARCH_PROMPT").format(claim=claim.claim)
                    findings: ResearchResponse = await self.tools["research"](research_prompt)
                    relatedFindings.append(findings)

        logging.info("Completed media analysis.")
        display: MediaSummary = MediaSummary(
            title=content_obj.title if content_obj else "User Input",
            content=content,
            summary=content_obj.summary if content_obj else "Summary not available for direct text input.",
            entities=entityList.entities,
            claims=claimsList.claims,
            related_findings=relatedFindings,
        )

        return display


async def is_url(input_str: str) -> bool:
    """Check if the input string is a URL."""
    return input_str.startswith("http://") or input_str.startswith("https://")
