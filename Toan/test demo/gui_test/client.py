import http.client

def requestGET(reqsv):
    # Use HTTPConnection for an HTTP server
    # connection = http.client.HTTPConnection("1.54.24.134", 200)
    
    connection = http.client.HTTPConnection("127.0.0.1", 5000)
    
    # Send GET request with the correct path and query parameters
    connection.request("GET", "/infos/?reqsv="+reqsv)  # Adjust to match your API route
    
    response = connection.getresponse()  
    connection.close()
    return response
def requestCtrlPort_GET(reqsv,port,status):
    # Use HTTPConnection for an HTTP server
    # connection = http.client.HTTPConnection("1.54.24.134", 200)
    
    connection = http.client.HTTPConnection("127.0.0.1", 200)
    
    # Send GET request with the correct path and query parameters
    url ="/infos/?reqsv="+str(reqsv) +"&port="+str(port) +"&status="+str(status)
    print(url)
    connection.request("GET", url)  # Adjust to match your API route
    
    response = connection.getresponse()  
    connection.close()
    return response
    


