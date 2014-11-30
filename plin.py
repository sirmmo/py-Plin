from time import sleep
import requests

class Plin():
	def __init__(self, ip="localhost", port=4124):
		self.address = ip
		self.port = port

	def put(tup):
		to_send = []
		for el in tup:
			to_send.append({"t":str(type(el)), "v":str(el)})
		requests.post("http://%s:%s/out", params={"tuple":json.dumps(to_send)})
		return True

	def get(tup, blocking=True):
		to_send = []
		for el in tup:
			to_send.append({"t":str(type(el)), "v":str(el)})

		ret = requests.post("http://%s:%s/in", params={"tuple":json.dumps(to_send)})
		while ret.json and blocking is None:
			sleep(1)
			ret = requests.post("http://%s:%s/in", params={"tuple":json.dumps(to_send)})
		return self.tuplize(ret.json) if ret is not None else None

	def read(tup):
		pass
			
	def tuplize(js):
		tup = ()
		for step in js:
			tup += eval("%s(%s)" % (step["t"], steè["v"]))
		return tup
