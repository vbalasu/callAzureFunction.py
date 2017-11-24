def callAzureFunction(baseurl, code, clientId, json):
    import requests
    querystring = {"code":code,"clientId":clientId}
    payload = json
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        }
    response = requests.request("POST", baseurl, data=payload, headers=headers, params=querystring)
    return(response.text)

#USAGE: print(callAzureFunction("https://cloudmaticafunctions.azurewebsites.net/api/echo", "JPPXiWIHCmGciaQ6Kj4qpmayDkXcIBFBi68GXziYkMMeWAUMIZ388Q==","default", "{\"text\":\"Python Postman\"}"))
