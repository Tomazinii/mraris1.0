
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from routers. import selected_form_router, add_rem_red_router
from exercise_route import exercise_api_route
from web.fastapi_app.routers import account_router, classroom_router, mrplato_router, problem_router, statistic_router
# from routers.problem_router import problem_router

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()



origins_test = [
    "http://localhost",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3001",
    "https://localhost:3001",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost:80",
    "http://192.168.15.3:80",
    "https://192.168.15.3:80",
    "http://192.168.15.3:8000",
    "https://192.168.15.3:8000",
    "http://192.168.15.3",
    "https://192.168.15.3",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:80",
    "http://nginx:80",
    "https://nginx:80",
]

origins = [
    "http://localhost",
    "https://localhost.tiangolo.com",
    "http://200.137.197.240",
    "https://200.137.197.240",
    "https://mraristotle.site",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Instrumentator().instrument(app).expose(app)


app.include_router(exercise_api_route, prefix="/api/v1/exercises")
app.include_router(problem_router, prefix="/api/v1/problems")
app.include_router(mrplato_router, prefix="/api/v1/mrplato")
app.include_router(account_router, prefix="/api/v1/accounts")
app.include_router(classroom_router, prefix="/api/v1/classroom")
app.include_router(statistic_router, prefix="/api/v1/statistic")

