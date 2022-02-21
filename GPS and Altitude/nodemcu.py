import urllib.request
root_url = "http://192.168.10.3"  # ESP's url, ex: http://192.168.102 (Esp prints it to serial console when connected to wifi)

def get_data(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode("utf-8")
    return data

# Example usage
def ret_data(answer):
	if (answer=="gps"):
		data=get_data(root_url).split()
		data_ext=data[0]+" "+data[1]
		return data_ext
	elif (answer=="alt"):
		data=get_data(root_url).split()
		data_ext=data[2]
		return data_ext
	else :
		return "Invalid request"