ENTITY_EXTRACTION_PROMPT: str = "You are an entity-level bias detector.\n\nIdentify all people, groups, or institutions discussed in the article.\nFor each entity, determine the tone:\n'very_positive', 'positive', 'neutral', 'negative', 'very_negative'\n\nExtract:\n- 1–3 evidence sentences that reflect this tone\n- any \"loaded phrases\" (emotionally charged or manipulative wording)\n\nArticle:{article}"

CLAIM_EXTRACTION_PROMPT: str = (
    "You are a claim extraction engine.\n"
    "Extract the 3–7 most important claims from the article below.\n"
    "Each claim MUST be labeled as either:\n\n"
    '- "factual": can be checked (dates, numbers, verifiable events)\n'
    '- "opinion": framing, emotional language, generalizations, or value judgments\n\n'
    "For each claim, indicate how you decide whether it's factual or opinion-based.\n\n"
    'Article:\n"{article}"'
)

RESEARCH_PROMPT: str = 'The following statement is an opinion-based claim from a news article. Search reputable news sources to find other statements of facts or opinions in support of this claim, and some that disagree with this claim, and give that information here, with citations. YOU MUST INCLUDE CITATION OF EACH STATEMENT TO THE SOURCE WHERE IT WAS FOUND IN THE FORM OF A URL. Return a list of opinion statements, each with the statement itself, the url of the source, and whether or not it supports the original claim. If there are factual statements that either support or disprove this claim, include those as well in a list of factual context WITH DIRECT CITATIONS IN THE FORM OF A URL. Each fact statement must contain the statement itself, the url of the source, and whether it supports, refutes, or is neutral to the original claim in question. Claim: "{claim}"'


TEST_ARTICLE: str = (
    "The Strategic Uncoupling of Zohran Mamdani and Brad Lander\n\n"
    "Mr. Lander, the New York City comptroller, campaigned with Mr. Mamdani and once hoped to join him in City Hall. "
    "Now he is eyeing a congressional seat. Zohran Mamdani was in the final, chaotic sprint to Election Day in the "
    "New York City mayor's race, when he stepped off the campaign trail for an important meeting.\n\n"
    "Sitting with him was Brad Lander, the city comptroller who had become one of his closest allies. "
    'Their "progressive bromance" during the Democratic primary in June had helped cinch Mr. Mamdani\'s victory and '
    "left Mr. Lander gunning for City Hall, too, hopefully as his top deputy.\n\n"
    "But when they met on a chaotic Sunday in late October, amid church services and canvass launches, Mr. Mamdani, "
    "a state assemblyman, wanted to talk about a different idea that Mr. Lander had floated. He told the comptroller "
    "that he would like to continue their partnership — by supporting him in a primary challenge against "
    "Representative Daniel Goldman, a vulnerable and more moderate Democrat, according to three people familiar with "
    "the exchange.\n\n"
    "As for the high-level administration post Mr. Lander, 56, had also coveted, Mr. Mamdani told him that he planned "
    "to go in a different direction. The sharp change-up has captivated New York's political chattering class since it "
    "spilled into public in recent days, setting the stage for a potentially explosive House primary in the heart of "
    "New York City.\n\n"
    "Mr. Mamdani's quiet maneuvering — much of which has not been previously reported — has also offered an early "
    "window into the unsentimental calculations guiding the incoming mayor as he builds his administration and flexes "
    "his political muscle.\n\n"
    "Asked to comment for this story, Mr. Mamdani's spokeswoman, Dora Pekec, said simply that Mr. Lander "
    '"continues to be a trusted ally and partner to the mayor-elect." But other supporters who have spoken to him '
    "added that Mr. Mamdani, a sharp critic of Israel, was eager to unseat Mr. Goldman, whose views on the war in "
    "Gaza and other issues are well to his right.\n\n"
    "People who have spoken with Mr. Lander recently said he had played down the sting of being passed over for a "
    "top city post.\n\n"
    "\"Brad's moral clarity, his willingness to use his voice to defend our democracy and put his body on the line to "
    'protect our neighbors are all vitally important and unfortunately all too rare," said his top adviser, '
    'Alison Hirsh. She said he would bring these qualities to Washington "if he chooses to run."\n\n'
    "The relationship between Mr. Lander and Mr. Mamdani has been the subject of unusual interest since the two men "
    "rolled out a novel cross-endorsement in June as competing candidates for mayor. Politicians often talk about "
    "forming alliances to defeat a common enemy, in this case former Gov. Andrew M. Cuomo, but rarely follow through. "
    "Mr. Lander, a well-known progressive with 15 years in public office, vouched for Mr. Mamdani, a 34-year-old "
    "Muslim and democratic socialist, with fellow Jewish Democrats. And after federal agents arrested Mr. Lander as "
    "he escorted migrants in an immigration courthouse, he used some of the attention to boost his formal rival.\n\n"
    "On the night of his primary victory, Mr. Mamdani put his arm around Mr. Lander and said they had modeled "
    '"the politics of the future, one of partnership and of sincerity."\n\n'
    "Many progressive New Yorkers supporting Mr. Mamdani — but uncertain about his youth with just five years in the "
    "State Assembly under his belt — felt comforted by the prospect of Mr. Lander joining City Hall as a partner "
    "overseeing the city's day-to-day operations."
)
