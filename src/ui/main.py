from nicegui import app as nicegui_app, ui
from src.api.main import analyse_input, router
from src.config import settings
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@ui.page("/")
def homepage():
    # Container for results
    result_container = ui.column().classes("w-full")

    # ---------------- TEXT INPUT ----------------
    ui.label("Analyse an article").classes("text-lg font-semibold")
    ui.label("Paste article text below to analyse tone and bias.").classes("text-[12px] text-slate-400 mb-2")

    article_input = ui.textarea(
        label="Article text",
        placeholder="Paste or type your article here...",
    ).classes(
        "w-full bg-slate-100 border border-slate-800 rounded-2xl "
        "text-slate-100 text-white px-4 py-3 text-sm min-h-[100px]"
    )

    async def handle_analysis():
        result_container.clear()
        with result_container:
            # Show loading spinner
            ui.spinner(size="lg")
            ui.label("Analyzing article...")

        try:
            # Call the async analysis function
            response = await analyse_input(article_input.value or "")
            # ui.notify(response)

            # Clear loading and show results
            result_container.clear()
            with result_container:
                # ui.json_editor({"content": {"json": response.model_dump_json()}})
                with ui.grid(columns=1).classes("w-full gap-6 lg:grid-cols-2"):
                    # LEFT COLUMN: Bias Dashboard & Claims
                    with ui.column().classes("w-full gap-6"):
                        # BIAS DASHBOARD
                        with ui.card().classes("bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-sm"):
                            ui.label("Bias Dashboard").classes("text-md font-semibold mb-4 text-white")

                            # Header row
                            with ui.row().classes(
                                "w-full text-[12px] text-slate-400 border-b border-slate-700 pb-2 mb-2"
                            ):
                                ui.label("Entity").classes("flex-1 font-medium")
                                ui.label("Tone").classes("flex-1 font-medium")
                                ui.label("Evidence").classes("flex-1 font-medium")
                                ui.label("Loaded Phrases").classes("flex-1 font-medium")

                            # Data rows
                            for entity in response.entities:
                                evidence_display = ""
                                for i, evidence in enumerate(entity.evidence_sentences):
                                    evidence_display += str(i + 1) + ". " + evidence + "\n"

                                loaded_phrases_display = ""
                                for i, loaded_phrase in enumerate(entity.loaded_phrases):
                                    loaded_phrases_display += str(i + 1) + ". " + loaded_phrase + "\n"
                                with ui.row().classes(
                                    "w-full text-[13px] text-slate-200 py-2 border-b border-slate-800/50 last:border-b-0"
                                ):
                                    ui.label(entity.name).classes("flex-1 font-medium")
                                    ui.label(entity.tone).classes("flex-1")
                                    ui.label(evidence_display).classes("flex-1")
                                    ui.label(loaded_phrases_display).classes("flex-1")

                        # CLAIMS & CHECKS
                        with ui.card().classes("bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-sm"):
                            ui.label("Claims & Checks").classes("text-md font-semibold mb-4 text-white")

                            for claim in response.claims:
                                with ui.column().classes("w-full mb-3 last:mb-0"):
                                    ui.label(claim.claim).classes("text-[13px] text-slate-200 font-medium")
                                    ui.label(claim.type + ": " + claim.reasoning).classes(
                                        "text-[11px] text-slate-400 mt-1"
                                    )

                        # FURTHER RESEARCH ON OPINION CLAIMS
                        with ui.card().classes("bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-sm"):
                            ui.label("Researching Opinion Claims").classes("text-md font-semibold mb-4 text-white")

                            # Header row
                            with ui.row().classes(
                                "w-full text-[12px] text-slate-400 border-b border-slate-700 pb-2 mb-2"
                            ):
                                ui.label("Claim").classes("flex-1 font-medium")
                                ui.label("Statement").classes("flex-1 font-medium")
                                ui.label("Opinion/Fact").classes("flex-1 font-medium")
                                ui.label("Supporting/Refuting Claim").classes("flex-1 font-medium")
                                ui.label("Source").classes("flex-1 font-medium")

                            i = 0
                            for claim in response.claims:
                                if claim.type == "opinion":
                                    related_findings = response.related_findings[i]
                                    i += 1
                                    for finding in related_findings.opinion_statements:
                                        supporting = "Refuting"
                                        if finding.supporting:
                                            supporting = "Supporting"
                                        with ui.row().classes("w-full mb-3 last:mb-0"):
                                            ui.label(claim.claim).classes(
                                                "flex-1 text-[13px] text-slate-200 font-medium"
                                            )
                                            ui.label(finding.statement).classes(
                                                "flex-1 text-[11px] text-slate-400 mt-1"
                                            )
                                            ui.label("Opinion").classes("flex-1 text-[11px] text-slate-400 mt-1")
                                            ui.label(supporting).classes("flex-1 text-[11px] text-slate-400 mt-1")
                                            ui.label(finding.source).classes("flex-1 text-[11px] text-slate-400 mt-1")
                                    for finding in related_findings.factual_context:
                                        supporting = "Refuting"
                                        if finding.supporting:
                                            supporting = "Supporting"
                                        with ui.row().classes("w-full mb-3 last:mb-0"):
                                            ui.label(claim.claim).classes(
                                                "flex-1 text-[13px] text-slate-200 font-medium"
                                            )
                                            ui.label(finding.statement).classes(
                                                "flex-1 text-[11px] text-slate-400 mt-1"
                                            )
                                            ui.label("Factual Context").classes(
                                                "flex-1 text-[11px] text-slate-400 mt-1"
                                            )
                                            ui.label(supporting).classes("flex-1 text-[11px] text-slate-400 mt-1")
                                            ui.label(finding.source).classes("flex-1 text-[11px] text-slate-400 mt-1")

        except Exception as e:
            result_container.clear()
            with result_container:
                ui.label(f"Error: {str(e)}").classes("text-negative")
                import traceback

                ui.label(traceback.format_exc()).classes("text-caption")

    with ui.row().classes("mt-2"):
        ui.button("Analyse article", on_click=handle_analysis).classes(
            "bg-sky-600 hover:bg-sky-700 rounded-xl px-6 py-2 text-white text-sm"
        )


nicegui_app.include_router(router)


def run_app():
    ui.run(
        storage_secret="test_secret",  # pragma: allowlist secret
        host=settings.server.host,
        port=settings.server.port,
        reconnect_timeout=1800,
        reload=settings.get("server.reload", False),
        uvicorn_reload_dirs="src/" if settings.get("server.reload", False) else None,
    )


if __name__ in {"__main__", "__mp_main__"}:
    run_app()
