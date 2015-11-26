def get_labels(infile, minPatientNumber = 0, maxPatientNumber = float("inf")):
	labelFile = open(infile, "r")
	count = 0
	labels = []
	for line in labelFile:
		if count == 0:
			count += 1
			continue

		splitLine = line.split(",")
		patient = splitLine[0]
		patient = patient.split("_")
		if int(patient[0]) > maxPatientNumber:
			break
		if int(patient[0]) >= minPatientNumber: labels.append(int(splitLine[1].strip('\n')))
	return labels
