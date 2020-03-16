from opencage.geocoder import OpenCageGeocode

key = '306b85ef43d145c9b6b04bdedf78d34a'
geocoder = OpenCageGeocode(key)

def getGeoCode(query):
	results = geocoder.geocode(query)
	return results[0]['geometry']['lat'],results[0]['geometry']['lng']
#query = u'petrolina, Pernambuco, Brasil'

'''
print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade
'''