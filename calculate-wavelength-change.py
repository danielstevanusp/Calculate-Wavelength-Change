def calculate_wavelength_change(lambda1, lambda2):

    delta_lambda = lambda2 - lambda1
    return delta_lambda

lambda1 = float(input("Enter the initial wavelength (lambda1) in meters: "))
lambda2 = float(input("Enter the final wavelength (lambda2) in meters: "))

delta_lambda = calculate_wavelength_change(lambda1, lambda2)
print(f"The change in wavelength (Δλ) is: {delta_lambda} meters")
