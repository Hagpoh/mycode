#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    enddate = "end_date=2019-11-14"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata['element_count'])
    hazardous = 0
    for date in neodata["near_earth_objects"].keys():
        for asteroid in neodata["near_earth_objects"][date]:
            if asteroid["is_potentially_hazardous_asteroid"]:
                hazardous += 1
    print(hazardous)

if __name__ == "__main__":
    main()

