
import requests

def url_checker(url):
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds 
		if get.status_code == 200:
			print(f"{url}: is reachable")
		else:
			print(f"{url}: is Not reachable, status_code: {get.status_code}")

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

url_checker("https://www.youtube.com/watch?v=4NYsqm2E41k")
