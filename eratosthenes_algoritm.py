import math
import time


class Prime:
    def __init__(self, primenumbers):
        self.primenumbers = primenumbers
        self.send_function()

    def send_function(self):
        end_number = int(math.sqrt(self.primenumbers[-1]))
        time_end = end_number
        try:
            for number in self.primenumbers:
                if end_number <= number:
                    print(f"\rTime: 0 second", end='')
                    break
                else:
                    for check in self.primenumbers:
                        if check % number == 0 and check != number:
                            self.primenumbers.remove(check)
                """time_calculation_base = 0.7
                time_calculation_pow = math.log10(end_number/number)
                time_calculation: str = str(float(math.pow(time_calculation_base,
                                                           time_calculation_pow)))
                print(f"\rTime: {time_calculation[:3]} second", end='')"""

            Prime.list_prime_function(self)
        except Exception as es:
            print(f"Error is: {es}")

    def list_prime_function(self):
        # count: int = 1
        try:
            with open('prime_output_eratosthenes.txt', 'w') as file:
                for prime in self.primenumbers:
                    file.write(f"{prime} is prime\n")
                    # print(prime, end=' ')
                    # count += 1
                    # if 0 != count % 20 or count < 1:
                    #    continue
                    # print("\n")
                print("\nDone")
        except Exception as es:
            print(f"File error: {es}")
