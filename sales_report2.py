"""Generate sales report showing total melons each salesperson sold."""

# Create empty lists for new variables: salesperson and melons_sold
salespeople = []
melons_sold = []

# this function will open and close the file all in one-line
with open ('sales-report.txt', 'r') as f:
    # Iterate over each line within the file
    for line in f:
        # Strip out spacing on the right for each line
        line = line.rstrip()
        # split the lines with '|' and put them in a list named entries
        entries = line.split('|')

        # assign the first index as a new variable- salesperson
        salesperson = entries[0]
        # assign the last index as a new variable- melons
        melons = int(entries[2])
        
        # conditional statements to add salesperson to the list of salespeople if not there, then add 1 to melons_sold count.
        if salesperson in salespeople:
            position = salespeople.index(salesperson)

            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)

# Iterate over each salespeople list and print
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
