'''

    Webapp interface for 4=10 solver.

'''
from unittest import result
from fastapi import FastAPI, Query, HTTPException
from solver import solve

app = FastAPI()


@app.get("/")
async def root(
    numbers: str = Query('4 letters long string: 4 numbers', min_length=4, max_length=4)
):

    def convert_to_listof_stings(lst: list) -> list:
        resval = []
        for l in lst:
            resval.append(' '.join([str(x) for x in l]))
        return resval

    try:
        int(numbers)
    except Exception as exception:
        raise HTTPException(400, 'Parameter must be a number!') from exception

    results = solve([int(num) for num in numbers], return_all_solutions=True)
    return {
        "status": "OK",
        "numbers": numbers,
        "results": convert_to_listof_stings(results)
    }
