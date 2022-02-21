import tags

def test_tag_seperation():
	test_inputs = [
		"lime mango",
		"lime,mango",
		"lime, mango",
		"lime    mango",
		"lime,,,,, mango"
	]

	for tag_string in test_inputs:
		processed_tags = tags.process(tag_string)
		assert len(processed_tags) == 2

def test_tag_capitalisation():
	test_inputs = [
		"LIME",
		"Lime",
		"lime"
	]

	for tag_string in test_inputs:
		processed_tags = tags.process(tag_string)
		assert processed_tags[0] == "lime"

def test_tag_stringification():
	test_tags = [
		"custard",
		"creme",
		"hobby-horse"
	]

	tag_string = tags.to_string(test_tags)

	assert tag_string == "custard creme hobby-horse"