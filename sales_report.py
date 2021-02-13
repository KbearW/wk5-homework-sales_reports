"""Generate sales report showing total melons each salesperson sold."""

def get_melons_sold_by_salesperson(file_path):
    # return a dict of {salesperson_name: melons_sold}.

    melons_sales = {}

    with open (file_path) as f:
        for line in f:
            entries = line.rstrip()
            salesperson_name, total_dollars, melons_sold = line.split('|')
            
            if salesperson_name in melons_sales:
                melons_sales[salesperson_name] += int(melons_sold)

            else:
                melons_sales[salesperson_name] = int(melons_sold)
    return melons_sales

# This function's argument asks for a dict called: melons_sold_by_salesperson. 
# This will be auto created and renamed from the function prior. 
# In this case, melons_sales == melons_sold_by_salesperson.
# That's why the call function will work in L29.
def print_sales_report(melons_sold_by_salesperson):
    for salesperson_name, melons_sold in melons_sold_by_salesperson.items():
        print(f'{salesperson_name} sold {melons_sold} melons')

# this is to combine both functions (think of it as nested functions)
print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))

# Benefit of nested function is to hide the complexity of the function and display a clear logic flow.