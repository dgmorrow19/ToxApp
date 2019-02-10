input_wt = input("Enter patient weight: ")
input_units = input("Enter units (kg or lbs): ")


def convert_weight(input_wt, input_units):
    '''

        takes user input for weight and units of weight
        if weight input is lbs converts to kg, rounds the
        results to 1 decimal place
        parameters: weight, units
    '''
    if input_units == "lbs":
        input_wt = float(input_wt)
        calculated_wt = input_wt / 2.2
        return round(calculated_wt, 1)
    elif input_units == "kg":
        calculated_wt = round(float(input_wt))
        return round(calculated_wt, 1)
    else:
        print("Unable to calculate, invalid units")


print("Paient dosing wt = " + str(convert_weight(input_wt, input_units)) + " kg")

systolic_bp = input("Enter Systolic Blood Pressure (mmHg): ")
diastolic_bp = input("Enter Diastolic Blood pressure (mmHg): ")

def calculate_map(systolic_bp, diastolic_bp):
    '''
    estimates MAP(mean arterial pressure)
    :param systolic_bp: in mmHg
    :param diastolic_bp: in mmHg
    :return: map (mean arterial pressure in mmHg)
    '''

    diastolic_bp = int(diastolic_bp)
    systolic_bp = int(systolic_bp)

    mean_arterial_pressure = (diastolic_bp * 2 + systolic_bp) / 3
    return int(mean_arterial_pressure)

print("Approximate Mean Arterial Pressure = " + str(calculate_map(systolic_bp, diastolic_bp)))
