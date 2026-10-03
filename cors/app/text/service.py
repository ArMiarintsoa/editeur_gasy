from rapidfuzz.distance import Levenshtein
import csv

class TextService:
	def __init__(self):
		pass

	def find_closest_word(input_text, csv_file):
		closest_word = None
		smallest_distance = float('inf')

		with open(csv_file, 'r', encoding='utf-8') as file:
			reader = csv.reader(file)
			next(reader)
			for row in reader:
				word = row[0]
				distance = Levenshtein.distance(input_text, word)
				if distance < smallest_distance:
					smallest_distance = distance
					closest_word = word

		return closest_word, smallest_distance