import pronouncing
print pronouncing.phones_for_word("ooh-ooh")
phones = pronouncing.phones_for_word("ooh-ooh")[0]
phones_split = phones.split()
last_phone = phones_split[-1]
		# if phones_split[-1] in rhymes:
print last_phone
# print pronouncing.search(phones)
