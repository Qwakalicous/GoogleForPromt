from googleapiclient.discovery import build
import json
from bs4 import Beautifulsoup


# Make a google search
# Print search results
# Read user input (index of webage)
# Clear screan
# Print webpage content
# Go-back option?


api_key = "AIzaSyBZLXdfal_8z72p1Jk-kR-JHuAz9_21Cy0"
cse_id = "012240546049780461316:yornpovhbwk"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


#For reducing number of searches by storing search results
def save_json(data, filename):
	with open(filename, "w+") as outputfile:
		json.dump(data, outputfile)


def load_json(filename):
	with open(filename, "r") as inputfile:
		return json.load(inputfile)


def print_menu(json_file):
	for i, item in enumerate(json_file["items"]):
		print("\n\n" + str(i) + ": " + item["title"])
		print("\t" + item["formattedUrl"])
		print("\t" + item["snippet"].replace("\n", "")) #Fix printing width with indentations


def print_webpage(link):
	print("Comming soon")
