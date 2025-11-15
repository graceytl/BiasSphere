from fastapi import FastAPI

from src.api.models import BiasAnalysisResponse
import uvicorn

app = FastAPI(
    root_path="/api"
)

@app.get('/')
def read_root():
    return "Welcome to BiasSphere API"

@app.get('/health')
def health_check():
    return {'status': 'ok'}

@app.post('/analyse')
def analyse_article(article: str) -> BiasAnalysisResponse:
    # Placeholder for analysis logic
    result = {"analysis": "This is a placeholder analysis result."}
    return result

def __main__():
    uvicorn.run("src.api.app:app", host="127.0.0.1", port=8000)