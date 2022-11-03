'''

    Webapp interface for 4=10 solver.

'''
from fastapi import FastAPI, Form
from solver import solve
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/webapp", StaticFiles(directory="../files"), name="webapp_files")


@app.post("/webservice")
async def webservice(
    #    numbers: str = Query('4 letters long string: 4 numbers', min_length=4, max_length=4)
    numbers: str = Form()
):

    def convert_to_listof_stings(lst: list) -> list:
        resval = []
        for l in lst:
            resval.append(' '.join([str(x) for x in l]))
        return sorted(set(resval))

    try:
        int(numbers)
    except Exception as exception:
        return {"status": "Error", "message": "Parameters has to be a number!"}
#        raise HTTPException(400, 'Parameter must be a number!') from exception
    if len(numbers) != 4:
        return {"status": "Error", "message": "Parameters has to be a four digit number!"}

    results = convert_to_listof_stings(solve([int(num) for num in numbers], return_all_solutions=True))
    return {
        "status": "OK",
        "numbers": numbers,
        "number_of_solutions": len(results),
        "results": results
    }
