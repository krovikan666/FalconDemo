# Falcon Demo
Simple test demo to start new falcon based REST APIs.


## Requirements
Falcon is required [https://github.com/falconry/falcon], as well as a WSGI server I use waitress.

## Usage
Once you have cloned the repo open a command prompt and navigate to the repo directory.

1. waitress-serve --port=8000 rest:app
2. http://127.0.0.1:8000/test?test=test   

## Result

```json
{
    "data": "Test data",
    "params": {
        "test": "test"
    }
}
```

