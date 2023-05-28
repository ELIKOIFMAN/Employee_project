def salary_after_tax(payment=0):
    """payment calculation after tax"""
    tax = 0
    if payment > 6790:
        # first pay grade
        tax = 6790 * 0.1
        print(tax)
        if payment >= 9730:
            # we passed the 2nd pay grade
            pay_grade = 9730 - 6791
            tax = tax + (pay_grade * 0.14)
            print(tax)
            if payment > 15620:
                #  we passed the 3rd pay grade
                pay_grade = 15620 - 9731
                tax = tax + (pay_grade * 0.2)
                print(tax)
                if payment > 21710:
                    # we passed the 4th pay grade
                    pay_grade = 21710 - 15621
                    tax = tax + (pay_grade * 0.31)
                    print(tax)
                    if payment > 45180:
                        # we passed the 5th pay grade
                        pay_grade = 45180 - 21711
                        tax = tax + (pay_grade * 0.35)
                        print(tax)
                        if payment > 58191:
                            # 7th pay grade
                            pay_grade = (payment - 58191) * 0.5
                            tax = tax + pay_grade
                            print(tax)
                        elif payment <= 58190:
                            # 6th pay grade
                            pay_grade = (payment - 45181) * 0.47
                            print(pay_grade)
                            tax = tax + pay_grade
                            print(tax)
                    elif payment <= 45180:
                        # 5th pay grade
                        pay_grade = payment - 21711
                        tax = tax + (pay_grade * 0.35)
                elif payment <= 21710:
                    # 4th pay grade
                    pay_grade = payment - 15621
                    tax = tax + (pay_grade * 0.31)
            elif payment <= 15620:
                # 3rd pay grade
                pay_grade = payment - 9731
                tax = tax + (pay_grade * 0.2)
        elif payment > 6790:
            # 2nd pay grade
            pay_grade = payment - 6791
            tax = tax + (pay_grade * 0.14)
    elif payment <= 6790:
        tax = payment * 0.1
    after_tax = payment - tax
    return print(f"you salary after tax is:{after_tax}")


salary_after_tax(50000)
