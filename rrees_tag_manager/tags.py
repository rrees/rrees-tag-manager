import re

def process(tag_string):
	return re.split("[ ,]+", tag_string.lower())

def as_string(tags):
	return " ".join(tags)