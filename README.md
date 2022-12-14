# 4=10 solver

This little utility solves the [popular game](https://play.google.com/store/apps/details?id=app.fourequalsten.fourequalsten_app).

## CLI

Usage:

```
python solver_cli.py --numbers n1 n2 n3 n4
```

or:

```
python solver_cli.py --shortnumbers n1n2n3n4
```

Get help:
 ```
 python solver_cli.py -h
 ```

## Web GUI

Start the server
 ```
uvicorn solver_webapp:app
```

Open your browser. The URL is: http://localhost:8000/webapp/index.html


## Rest API

Start the server
 ```
uvicorn solver_webapp:app
```

The webserver runs at the ```:8000``` port by default. The documentation and testing page is here: [http://localhost:8000/docs#](http://localhost:8000/docs)

Return value is in json format:

```
{
    "status":"OK",
    "numbers":"1234",
    "number_of_solutions":380
    "results":[   
        "1 + 2 + 3 + 4",
        "( 1 + 2 ) + 3 + 4",
        ..
        "4 * ( 3 / 2 + 1 )"
    ]
}
```