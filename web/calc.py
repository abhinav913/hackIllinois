import math


#queue for timestamps, also a dictionary with MAC addresses
#time_dict = {}
#holds device MAC addresses, dictionary of timestamps, and signal strengths 
dict_storage = {}
#holds MAC addresses, timestamps, and final (x,y) coordinates; dict_coord[mac][n] where n = 0(timestamp), 1(x coord), 2(y coord)
dict_coordinates = {}
#holds router MAC Addresses, should hold 3 values max
router_addresses = {}
#router coordinates:
x1 = 0
y1 = 0
x2 = 4
y2 = 0
x3 = 3
y3 = 1

def routerAddress(router_mac_addr) :

	if (len(router_addresses.keys()) < 3) :
		if (not router_addresses.has_key(router_mac_addr)) :
			router_addresses[router_mac_addr] = len(router_addresses.keys())
	

def checkForUpdates(mac_addr, timestamp, signal, router_addr):
	if (not dict_storage.has_key(mac_addr)):
		dict_storage[mac_addr] = {timestamp: [0, 0, 0]}	
		dict_coordinates[mac_addr] = [timestamp, 0, 0]
		#time_dict[mac_addr] = [timestamp]
	if (not dict_storage[mac_addr].has_key(timestamp)) :
		dict_storage[mac_addr][timestamp] = [0, 0, 0]
		#time_dict[mac_addr].append(timestamp)
	dict_storage[mac_addr][timestamp][router_addresses[router_addr]] = signal
	for x in dict_storage[mac_addr][timestamp]:
		if x == 0 :
			return None
	
	if dict_storage[mac_addr][timestamp][0] and dict_storage[mac_addr][timestamp][1] and dict_storage[mac_addr][timestamp][2]:
		output = dict_storage[mac_addr][timestamp]
		del dict_storage[mac_addr][timestamp]
		return (trilateration_x(dict_storage[mac_addr][timestamp][0], dict_storage[mac_addr][timestamp][1]),
			trilateration_y(dict_storage[mac_addr][timestamp][0], dict_storage[mac_addr][timestamp][2], dict_coordinates[mac_addr][1]),
			mac_addr)
	else:
		return None
	#if int(timestamp) > int(dict_coordinates[mac_addr][0]) :
	#	dict_coordinates[mac_addr][0] = timestamp
	#	dict_coordinates[mac_addr][1] = trilateration_x(dict_storage[mac_addr][timestamp][0], dict_storage[mac_addr][timestamp][1])
	#	dict_coordinates[mac_addr][2] = trilateration_y(dict_storage[mac_addr][timestamp][0], dict_storage[mac_addr][timestamp][2], dict_coordinates[mac_addr][1])
	#	temp = sorted(dict_storage[mac_addr].keys(), key = lambda x: int(x))
		#time_dict[mac_addr].sort(key = float) 
	#	while (1) :
	#		if (dict_storage[mac_addr][0] < timestamp) :
	#			#a = str (time_dict[mac_addr][0])
	#			#del time_dict[mac_addr][0]
	#			del dict_storage[mac_addr][0]
	#		else :
	#			break	
	#	del dict_storage[mac_addr][timestamp]
	#	return (dict_coordinates[mac_addr][1], dict_coordinates[mac_addr][2], mac_addr) #returns (x, y, MAC addr) as tuple
	#else: 
	#	print "delete node"
	#	print dict_storage[mac_addr][timestamp]
	#	del dict_storage[mac_addr][timestamp]
	#	return None


#def sig_strengthToDistance(signal_strength) :
#
#	distance = (27.55 - 20*(math.log10(2437) + math.fabs(signal_strength)) / 20)
#	distance = math.pow(10.0, distance)
#	return distance

def trilateration_x(s1, s2) :

	x = (math.pow(s1, 2) - math.pow(s2, 2) + math.pow(x2, 2)) / (2 * x2)
	return x

def trilateration_y(s1, s3, trilat_x) :

	y = ((math.pow(s1, 2) - math.pow(s3, 2) + math.pow(x3, 2) + math.pow(y3, 2)) / (2 * y3)) - ((x3 * trilat_x) / y3)
	return y

if __name__ == "__main__":
	routerAddress("1")
	routerAddress("2")
	routerAddress("3")
	print checkForUpdates("50", "121221230", -15, "1")
	print dict_storage
	print time_dict
	print checkForUpdates("50", "121221231", -32, "2")
	print dict_storage
	print checkForUpdates("50", "121221231", -24, "1")
	print dict_storage
	print checkForUpdates("50", "121221230", -12, "3")
	print dict_storage
	print checkForUpdates("50", "121221233", -15, "2")
	print dict_storage
	print checkForUpdates("50", "121221233", -24, "1")
	print checkForUpdates("50", "121221233", -55, "3")
	print dict_storage



