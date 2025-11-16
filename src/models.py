from typing import List
from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    status: str


class AnalyseArticleRequest(BaseModel):
    article: str


class BiasAnalysisResponse(BaseModel):
    summary: str
    entities: List[str]


class Entity(BaseModel):
    """Person, group, or institution mentioned in the article. Contains information and evidence about bias presented."""

    name: str = Field(description="Name of person, group, institution, or organization mentioned")
    tone: str = Field(
        description="Sentiment within the article towards the entity mentioned: MUST be one of the following: 'very positive', 'positive', 'neutral', 'negative', 'very negative'"
    )
    evidence_sentences: List[str] = Field(
        description="Phrases or sentences pulled directly from the provided article that demonstrate the sentiment of the article toward this entity"
    )
    loaded_phrases: List[str] = Field(
        description="Emotionally charged or manipulative wording or phrases used in the article pertaining to the entity"
    )


class EntityAnalysisResponse(BaseModel):
    """Analysis of the entities discussed in the article and how the sentiment presented toward them."""

    entities: List[Entity] = Field(
        description="A person, group, or institution mentioned in the article, and information about how it is presented. Each entity contains a name; tone - Sentiment within the article towards the entity mentioned: MUST be one of the following: 'very positive', 'positive', 'neutral', 'negative', 'very negative'; evidence_sentences - Phrases or sentences pulled directly from the provided article that demonstrate the sentiment of the article toward this entity; loaded_phrases - Emotionally charged or manipulative wording or phrases used in the article pertaining to the entity"
    )


# Define output schema
class Claim(BaseModel):
    """Important factual or opinion claims from the article"""

    claim: str = Field(description="Direct text of the claim from article")
    type: str = Field(
        description="Whether the claim is 'factual': can be checked (dates, numbers, verifiable events) or 'opinion': framing, emotional language, generalizations, or value judgments. MUST be one of 'factual' OR 'opinion'"
    )
    reasoning: str = Field(description="Why is this claim categorized as factual or opinion")


class ClaimsAnalysisResponse(BaseModel):
    """Analysis of the claims made in the article and whether they are factual or opinion-based."""

    claims: List[Claim] = Field(description="List of the most important claims in the article.")


class Statement(BaseModel):
    """A statement made during online research about a specific claim."""

    supporting: bool = Field(description="Whether the statement supports or refutes the claim.")
    statement: str = Field(description="The statement related to the claim")
    source: str = Field(description="Source of the statement (e.g., website, article title)")


class ResearchResponse(BaseModel):
    """Results from online research about a specific claim."""

    opinion_statements: List[Statement] = Field(
        description="Statements gathered during research about the claim. Each statement must contain three fields: 'supporting' - a bool of whether the statement supports or refutes the original claim, 'statement' - the text of the statement itself, and 'source' - a url of the source of this statement"
    )
    factual_context: List[Statement] = Field(
        description="Factual context gathered from online research about the claim. Each statement must contain three fields: 'supporting' - a bool of whether the statement supports or refutes the original claim, 'statement' - the text of the statement itself, and 'source' - a url of the source of this statement"
    )


class MediaSummary(BaseModel):
    """Media Summary object to display in the UI."""

    content: str = Field(description="The content of analysis from user input.")
    summary: str = Field(description="A summary of the media analysis.")
    entities: List[Entity] = Field(description="Entities found in content and locations.")
    claims: List[Claim] = Field(description="Claims identified in the content.")
    related_findings: List[ResearchResponse] = Field(description="Related findings from research on claims.")
