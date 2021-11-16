# Introduction

This project aims to work on image recognition using tesseract library provided by Google

Tutorial: https://nanonets.com/blog/ocr-with-tesseract/

## Quickstart

Run the following command in your terminal

```
python3 ocr.py <image_source>
```

The source folder contains images than can be used for tests purpose

## FastApi

The project uses FastApi to implement an API to run tesseract image processing. To run the API, we are using uvicorn as a server. You can install it using `pip install uvicorn`.

To start the api, run:

```
uvicorn main:<app> --reload
```

<app> should be rename by the name of the variable from which FastApi() is called in your code.

The app is available on 127.0.0.1:8000

The doc is accessible on **/docs** or **/redoc**. You can use the doc it try out the endpoint available in the api.
