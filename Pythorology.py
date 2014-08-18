"""
Pythorology 1.0.
Written by Ericson Willians.
"""

class WeirdResultError(Exception):
	pass

class Decipher:

	def __init__(self, name=""):
	
		self.name = name
		self.data = {}
		self.fill_data()
		
	def fill_data(self):
	
		self.data["asd"] = 1
		self.data["bkt"] = 2
		self.data["clu"] = 3
		self.data["dmv"] = 4
		self.data["enw"] = 5
		self.data["fox"] = 6
		self.data["gpy"] = 7
		self.data["hqz"] = 8
		self.data["ir"] = 9
		
	def make_out(self):
	
		result = []
	
		for c in self.name:
			for item in self.data.items():
				if c.lower() in item[0]:
					result.append(str(item[1]))
		
		return result
		
	def _sum(self):
	
		decoded = self.make_out()
		
		return sum([int(x) for x in decoded])
		
	def to_one(self):
	
		_su = str(self._sum())
		if len(_su) == 2:
			su = sum([int(x) for x in _su])
			if su == 11 or su == 22 or su == 33:
				return su
			elif len(str(su)) == 2:
				if str(su)[1] == "0":
					return int(str(su)[0])
				else:
					return sum([int(x) for x in str(su)])
			elif len(str(su)) == 1:
				return su
			else:
				raise WeirdResultError("Something weird happened. Result = " + str(su) + " | " + _su + ".")
		elif len(_su) == 1:
			return int(_su)
		else:
			return sum([int(x) for x in _su])
		
	def raw(self):
	
		return "-".join(self.make_out())
		
class Vcipher():

	def __init__(self, name):
		
		vowels = list("aeiou")
		self.vname = []
		self.cname = name.lower()
		for vowel in name.lower():
			if vowel in vowels:
				self.vname.append(vowel)
				self.cname = self.cname.replace(vowel, "")
		
		self.v = Decipher(''.join(self.vname))
		self.c = Decipher(self.cname)
		
class OutputModel:

	def __init__(self, _in):
	
		self._in = _in
		self.d = Decipher(self._in)
		self.v = Vcipher(self._in)
		
	def output(self):
	
		print "Raw: " + self.d.raw()
		print "Sum: " + str(self.d.to_one())
		print "VRaw: " + self.v.v.raw()
		print "VSum: " + str(self.v.v.to_one())
		print "CRaw: " + self.v.c.raw()
		print "CSum: " + str(self.v.c.to_one())
		
if __name__ == "__main__":
	name = raw_input("Name: ")
	OutputModel(name).output()
