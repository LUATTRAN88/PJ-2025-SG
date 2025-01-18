import http.client

def requestGET(reqsv):
    # Use HTTPConnection for an HTTP server
    connection = http.client.HTTPConnection("1.54.24.134", 200)
    
    # Send GET request with the correct path and query parameters
    connection.request("GET", "/infos/?reqsv="+reqsv)  # Adjust to match your API route
    
    response = connection.getresponse()
    #print("Status: {} and reason: {}".format(response.status, response.reason))
    
    # Print response body (if any)
    #print("Response data:", )

    
    connection.close()
    return response
    
    


