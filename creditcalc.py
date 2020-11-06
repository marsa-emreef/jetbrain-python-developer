import sys
from math import ceil, pow, floor, log

argv_len = len(sys.argv)
args = dict(argv.split('=') for argv in sys.argv[1:argv_len])

# --- section where we pull the param ---
type_ = ''
if '--type' in args:
    type_ = args['--type']

payment_ = 0
if '--payment' in args:
    payment_ = float(args['--payment'])

principal_ = 0
if '--principal' in args:
    principal_ = int(args['--principal'])

periods_ = 0
if '--periods' in args:
    periods_ = int(args['--periods'])

interest_ = 0
if '--interest' in args:
    interest_ = float(args['--interest'])


# --- validator function ---
def print_error():
    print('Incorrect parameters')
    exit()


def validator_non_negative(params):
    for param in params:
        if param < 0:
            print_error()


# --- section where we validate the param ---
if argv_len < 4:
    print_error()

if interest_ == 0:
    print_error()

if type_ == '':
    print_error()

if type_ == 'diff' and payment_ > 0:
    print_error()

validator_non_negative([interest_, periods_, principal_])


# number_of_payments_ = 1
# current_repayment_month_ = 1


def calculate_month_differentiated_payment(principal, number_of_payment, interest, current_repayment_month):
    return (principal / number_of_payment) + ((interest / 12 / 100) * (
            principal - ((principal * (current_repayment_month - 1)) / number_of_payment)))


def calculate_by_diff(principal, period, interest):
    total_payment = 0
    for month in range(1, period + 1):
        payment = ceil(calculate_month_differentiated_payment(principal, period, interest, month))
        total_payment += payment
        print(f'Month {month}: payment is {payment}')
    overpayment = total_payment - principal_

    print(f'\nOverpayment = {overpayment}')


def calculate_annuity_payment(principal, period, interest):
    interest = (interest / 12 / 100)
    monthly_payment = ceil(principal * ((interest * pow(1 + interest, period)) / (
            pow(1 + interest, period) - 1)))
    overpayment = principal_ - monthly_payment * period
    print(f'Your annuity payment = {monthly_payment}!')
    print(f'Overpayment = {overpayment}')


def calculate_annuity_principal(payment, period, interest):
    interest = (interest / 12 / 100)
    principal = floor(payment / ((interest * pow(1 + interest, period)) / (
            pow(1 + interest, period) - 1)))
    overpayment = round(abs(payment * period - principal))
    print(f'Your annuity principal = {principal}!')
    print(f'Overpayment = {overpayment}')


def calculate_annuity_periods(principal, payment, interest):
    interest = (interest / 12 / 100)
    periods = ceil(log(payment / (payment - interest * principal), interest + 1))
    years = floor(periods / 12)
    months = periods % 12
    overpayment = round((payment * periods) - principal)
    if months == 0:
        print(f'It will take {years} years to repay this loan!')
    else:
        print(f'It will take {years} years and {months} months to repay this loan!')
    print(f'Overpayment = {overpayment}')
    pass


if type_ == 'diff':
    calculate_by_diff(principal_, periods_, interest_)
elif type_ == 'annuity':
    if principal_ > 0 and periods_ > 0:
        calculate_annuity_payment(principal_, periods_, interest_)
    elif payment_ > 0 and periods_ > 0:
        calculate_annuity_principal(payment_, periods_, interest_)
    elif principal_ > 0 and payment_ > 0:
        calculate_annuity_periods(principal_, payment_, interest_)
