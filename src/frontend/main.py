from typing import Literal, List, Union, Dict
from nicegui import ui
from fastapi import FastAPI

# FastAPI application
app = FastAPI()

Tone = Literal["positive", "negative"]
ArticlePart = Union[str, Dict[str, str]]

# ---------------- Mock data (replace with model output later) ---------------- #

mock_summary = (
    "This article frames the subject in a largely positive light, using emotionally "
    "charged language and selective statistics. While it acknowledges some criticisms, "
    "these are downplayed compared to supportive quotes and optimistic projections."
)

mock_stats = {
    "biased_keywords": 17,
    "positive_bias_comments": 9,
    "negative_bias_comments": 5,
}

mock_article_parts: List[ArticlePart] = [
    "The report describes the new policy as ",
    {
        "id": "h1",
        "text": "an unprecedented success",
        "explanation": "Emotionally loaded phrase presented as fact without evidence.",
        "tone": "positive",
    },
    ", highlighting only the short-term economic gains. Critics are described as ",
    {"id": "h2", "text": "vocal outliers", "explanation": "Dismisses opposing views as fringe.", "tone": "negative"},
    ". The article claims the government has shown ",
    {
        "id": "h3",
        "text": "remarkable leadership",
        "explanation": "Subjective praise framed as objective fact.",
        "tone": "positive",
    },
    " while omitting major challenges.",
]

# ---------------- UI Helpers ---------------- #


def stat_card(label: str, value: int, subtitle: str):
    with ui.card().classes("bg-slate-900/80 rounded-2xl px-4 py-3 w-full"):
        ui.label(label).classes("text-[11px] text-slate-400")
        ui.label(str(value)).classes("text-xl font-semibold")
        ui.label(subtitle).classes("mt-1 text-[10px] text-slate-500")


def bias_label(text: str, explanation: str, tone: Tone) -> None:
    base = "inline px-1 py-0.5 rounded border cursor-pointer transition-colors text-xs"
    cls = base + (
        " bg-emerald-500/20 text-emerald-100 border-emerald-400 hover:bg-slate-800"
        if tone == "positive"
        else " bg-rose-500/20 text-rose-100 border-rose-400 hover:bg-slate-800"
    )
    label = ui.label(text).classes(cls)
    label.tooltip(explanation)


# ---------------- MAIN UI ---------------- #


@ui.page("/")
def main_page():
    with ui.column().classes("min-h-screen bg-slate-950 text-slate-50 w-full"):
        # ---------------- TOP BANNER ----------------
        with ui.row().classes(
            "w-full border-b border-slate-800 bg-slate-950/90 backdrop-blur px-6 py-4 items-center justify-between"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.label("BL").classes(
                    "h-10 w-10 flex items-center justify-center rounded-xl "
                    "bg-gradient-to-tr from-sky-500 to-violet-500 text-sm font-bold"
                )
                with ui.column().classes("gap-0"):
                    ui.label("BiasLens").classes("text-xl font-semibold")
                    ui.label("Detect and visualize bias in news articles.").classes("text-[12px] text-slate-400")

            ui.label("UCL × HolisticAI Hack")
            ui.label("Prototype").classes(
                "text-[10px] hidden md:flex text-slate-400 border border-slate-700 rounded-full px-3 py-1"
            )

        with ui.column().classes("w-full px-6 py-8 gap-6 max-w-[1400px] self-center"):
            # ---------------- URL INPUT (FULL WIDTH) ----------------
            ui.label("Analyze an Article").classes("text-lg font-semibold")
            ui.label("Paste a URL to fetch and analyze the article text.").classes("text-[12px] text-slate-400 mb-2")

            url_box = ui.input(
                label="Article URL",
                placeholder="https://example.com/news/article",
            ).classes("w-full bg-slate-900 border border-slate-700 rounded-xl text-slate-200 px-4 py-3")

            def fetch_url():
                # Replace this with:
                # cleaned_text = prepare_article_for_model(url_box.value, "url")
                ui.notify(f"Fetching and cleaning: {url_box.value}")

            ui.button("Fetch Article", on_click=fetch_url).classes(
                "bg-sky-600 hover:bg-sky-700 rounded-xl px-6 py-2 text-white"
            )

            # ---------------- SUMMARY CARD ----------------
            with ui.card().classes("bg-slate-900/60 border border-slate-800 rounded-2xl p-6 w-full"):
                with ui.row().classes("justify-between items-center mb-1"):
                    ui.label("Bias-aware summary").classes("text-md font-semibold")
                    ui.label("Model output").classes(
                        "text-[10px] uppercase tracking-wide text-slate-400 "
                        "border border-slate-700 rounded-full px-2 py-0.5"
                    )

                ui.label(mock_summary).classes("text-[13px] text-slate-200 leading-relaxed")

            # ---------------- STAT CARDS (FULL WIDTH) ----------------
            with ui.row().classes("w-full gap-4"):
                stat_card("Biased keywords", mock_stats["biased_keywords"], "Flagged terms in the article")
                stat_card("Positive bias", mock_stats["positive_bias_comments"], "Favourable framing")
                stat_card("Negative bias", mock_stats["negative_bias_comments"], "Hostile framing")

            # ---------------- ARTICLE VIEW (FULL WIDTH) ----------------
            with ui.card().classes("w-full bg-slate-900/60 border border-slate-800 rounded-2xl p-6"):
                with ui.row().classes("justify-between items-start mb-4"):
                    with ui.column():
                        ui.label("Article view").classes("text-md font-semibold")
                        ui.label("Hover over highlighted phrases to see why they may be biased.").classes(
                            "text-[12px] text-slate-400"
                        )
                    with ui.row().classes("gap-3 text-[12px] text-slate-400"):
                        with ui.row().classes("items-center gap-1"):
                            ui.element("span").classes("inline-block h-2 w-2 rounded-full bg-emerald-400")
                            ui.label("Positive")

                        with ui.row().classes("items-center gap-1"):
                            ui.element("span").classes("inline-block h-2 w-2 rounded-full bg-rose-400")
                            ui.label("Negative")

                with ui.element("div").classes(
                    "rounded-xl border border-slate-800 bg-slate-950/80 "
                    "px-6 py-4 max-h-[600px] overflow-y-auto text-sm "
                    "leading-relaxed text-slate-100"
                ):
                    with ui.row().classes("flex-wrap gap-[4px] items-start"):
                        for part in mock_article_parts:
                            if isinstance(part, str):
                                ui.label(part).classes("inline text-sm")
                            else:
                                bias_label(part["text"], part["explanation"], part["tone"])


# ---------------- Run with FastAPI ---------------- #

ui.run_with(
    app=app,
    storage_secret="super-secret-key",
)


def __main__():
    ui.run(host="127.0.0.1", port=8000, title="BiasLens Dashboard")
