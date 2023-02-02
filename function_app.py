import azure.functions as func
import logging
import datetime

# from flask import Flask, request, Response, redirect, url_for 

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel
# Get started by running the following code to create a function using a HTTP trigger.
# @app.function_name(name="HttpTrigger1")
# @app.route()
# def test_function(req: func.HttpRequest) -> func.HttpResponse:
#     return "Foo"

@app.function_name(name="mytimer")
@app.schedule(schedule="0 */5 * * * *", arg_name="mytimer", run_on_startup=True,
              use_monitor=False) 
def test_function(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)


@app.route(route="hello")
def test_function1(req):
    return "Hello"
