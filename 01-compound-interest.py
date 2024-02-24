def compound_interest(principal_amount, interest, years):

    decimal_interest = interest / 100
    times_per_year = 1
    
    future_amount = principal_amount * (1 + decimal_interest / times_per_year) ** (times_per_year * years)
    
    return future_amount

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("La entrada no es válida, por favor introduce un número.")
            
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("La entrada no es válida, por favor introduce un número entero.")
            

principal_amount = input_float("Introduce el monto principal: ")
interest = input_float("Introduce la tasa de interés anual (en %): ")
years = input_int("Introduce el número de años: ")

future_amount = compound_interest(principal_amount, interest, years)
print(f"El monto futuro después de {years} años es: ${future_amount:.2f}")
