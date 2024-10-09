import requests
import sys

def check_cidr(ip_address):
    # fetch data
    response = requests.get("https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix")

    # fail if not 200
    if response.status_code != 200:
        raise Exception("error fetching data from ripe ncc")

    # convert response to json format
    data = response.json()

    # drill down and set ip list as var
    cidr_blocks = data['data']['resources']['ipv4']

    # check if cidr exists in cidr_blocks list
    if ip_address in cidr_blocks:
        return True
    else:
        return False

def run_tests():
    # test: expect to find a matching cidr
    expected = "223.165.112.0/20"
    
    # run expected test
    try:
        if check_cidr(expected):
            print('positive test result: pass') 
        else:
            print('positive test result: fail')
    except Exception as error:
        print(error) 

    # set unexpected ip
    unexpected = "192.0.2.0/24"

    # run unexpected test
    try:
        if not check_cidr(unexpected):
            print('negative test result: pass')
        else:
            print('negative test result: fail')
    except Exception as error:
        print(error)

## accept param from cli for main file function
if __name__ == "__main__":
    ip_address = sys.argv[1]
    # run main function
    check_cidr(ip_address)
  
    # run static unit tests
    run_tests()
