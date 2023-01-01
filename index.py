'''

    Webapp interface for 4=10 solver.

'''
from starlette.responses import FileResponse
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from solver import solve

app = FastAPI()


# @app.route("/", defaults={"path": ""})
@app.get("/")
async def render_landing():
    return FileResponse("../files/index.html")


app.mount("/js", StaticFiles(directory="../files/js"), name="webapp_files")


@app.post("/api")
async def webservice(
    numbers: str = Form()
):

    def convert_to_listof_stings(lst: list) -> list:
        resval = []
        for l in lst:
            resval.append(' '.join([str(x) for x in l]))
        return sorted(set(resval))

    try:
        int(numbers)
    except ValueError as _:
        #raise HTTPException(400, 'Parameter must be a number!') from e
        return {"status": "Error", "message": "Parameters has to be a number!"}
    if len(numbers) != 4:
        return {"status": "Error", "message": "Parameters has to be a four digit number!"}

    results = convert_to_listof_stings(solve([int(num) for num in numbers], return_all_solutions=True))
    return {
        "status": "OK",
        "numbers": numbers,
        "number_of_solutions": len(results),
        "results": results
    }
