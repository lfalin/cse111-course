import requests
from requests.exceptions import ConnectionError, Timeout, \
        TooManyRedirects, HTTPError, RequestException
from datetime import datetime, timedelta

def main():
    try:
        # qcode is short for Quandl Code and is the code that determines
        # what data will be downloaded from Quandl by the http request.
        qcode = "ODA/PWOOLC_USD"

        # This is the uniform resource locator (URL)
        # where this program will send an http request.
        endpoint = f"https://www.quandl.com/api/v3/datasets/{qcode}.json"

        # These are the start and end dates for the data request. The start
        # date will be about 13 months before today, and the end date will
        # be today.
        end = datetime.today()
        start = end - timedelta(days=13*30)

        # Arguments that focus the http data request.
        args = {
            # The API key should remain private. Do not save
            # it to a public repository or public web site.
            "api_key" : "The API key is in your I-Learn course.",

            "start_date" : start.strftime("%Y-%m-%d"),
            "end_date" : end.strftime("%Y-%m-%d"),
            "collaspe" : "monthly",
            "order" : "asc"
        }

        # Request the commodities data from Quandl.
        response = requests.get(endpoint, params=args)
        response.raise_for_status()

        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            # If the request was succesful, print
            # the data that Quandl returned to us.
            print(qcode)
            dataset = response.json()["dataset"]
            print(dataset["name"])
            print(dataset["start_date"], dataset["end_date"])
            print(dataset["column_names"])
            data = dataset["data"]
            for datum in data:
                print(datum)
        else:
            # If the request was not successful, print the status code.
            print(response.status_code)

    except ConnectionError as ex:
        print("Connection error: ", ex)
    except Timeout as ex:
        print("Timeout: ", ex)
    except TooManyRedirects as ex:
        print("Too many redirects: ", ex)
    except HTTPError as ex:
        print("HTTP error: ", ex)
    except RequestException as ex:
        print("Request exception: ", ex)
    except RuntimeError as ex:
        # RuntimeError is probably the most general type of exception
        # that you want to handle in a Python program. Exception is
        # more general than RuntimeError. However, Exception includes
        # SyntaxError, and you probably don't want to handle
        # SyntaxError. Instead, you want your program to crash for
        # SyntaxError and print the line number where the SyntaxError
        # occurred.
        print(type(ex).__name__, ex, sep=": ")


# Call the main function so that
# this program will start executing.
main()
