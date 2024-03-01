def compound_interest_with_monthly_contributions(principal_amount, monthly_contribution, interest_rate, years_remaining):
    if years_remaining == 0:
        return principal_amount
    else:
        decimal_interest_rate = interest_rate / 100
        for month in range(1, 13):
            principal_amount += monthly_contribution
        # Aplica el interés compuesto al final del año
        principal_amount *= (1 + decimal_interest_rate)
        # Llamada recursiva para el siguiente año, reduciendo el contador de años
        return compound_interest_with_monthly_contributions(principal_amount, monthly_contribution, interest_rate, years_remaining - 1)

def input_float(prompt):
    while True:
        try:
            # Solicita al usuario que ingrese un valor y trata de convertirlo a float
            return float(input(prompt))
        except ValueError:
            # Si la conversión falla, informa al usuario y solicita nuevamente la entrada
            print("La entrada no es válida, por favor introduce un número.")

def input_int(prompt):
    while True:
        try:
            # Solicita al usuario que ingrese un valor y trata de convertirlo a int
            return int(input(prompt))
        except ValueError:
            # Si la conversión falla, informa al usuario y solicita nuevamente la entrada
            print("La entrada no es válida, por favor introduce un número entero.")

principal_amount = input_float("Introduce el monto principal: ")
monthly_contribution = input_float("Introduce el monto de la contribución mensual: ")
interest = input_float("Introduce la tasa de interés anual (en %): ")
years = input_int("Introduce el número de años: ")

future_amount = compound_interest_with_monthly_contributions(principal_amount, monthly_contribution, interest, years)
print(f"El monto futuro después de {years} años es: ${future_amount:.2f}")

