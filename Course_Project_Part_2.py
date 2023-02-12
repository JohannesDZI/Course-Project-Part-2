#Johannes Dzidzienyo - CIS 261 - 003VA016-1232-001
#Course Project Part 2

def get_name():
    temp_name = input("Enter employee name: ")
    return temp_name


def get_date():
    temp_start_date = input('Enter Start Date (mm/dd/yyyy): ')
    temp_end_date = input('Enter End Date (mm/dd/yyyy): ')
    return temp_start_date, temp_end_date


def get_total_hours():
    temp_total_hours = input('Enter amount of hours worked: ')
    return temp_total_hours


def get_hourly_rate():
    temp_hourly_rate = input('Enter hourly rate: ')
    return temp_hourly_rate


def get_income_tax_rate():
    temp_income_tax_rate = input('Enter tax rate: ')
    return temp_income_tax_rate


def calculate_payroll(total_hours, hourly_rate, income_tax_rate):
    temp_gross_pay = float(total_hours) * float(hourly_rate)
    temp_tax_rate = float(income_tax_rate) * 100
    temp_tax_calc = float(income_tax_rate) * temp_gross_pay
    temp_net_pay = temp_gross_pay - temp_tax_calc
    return temp_gross_pay, temp_tax_rate, temp_tax_calc, temp_net_pay


def print_info(name, date_from, date_to, total_hours, hourly_rate, gross_pay, tax_rate, tax_calc, net_pay):
    print('')
    print('Name: ' + name)
    print('From Date: ' + date_from)
    print('To Date: ' + date_to)
    print('Hours Worked: %.2f' % float(total_hours))
    print('Hourly Rate: %.2f' % float(hourly_rate))
    print('Gross Pay: %.2f' % float(gross_pay))
    print('Tax Rate: ' + str(tax_rate) + '%')
    print('Income Tax: %.2f' % float(tax_calc))
    print('Net Pay: %.2f' % float(net_pay))


def print_all_info(totals):
    print('')
    print("Total Number of Employees: " + str(totals['total_employee_count']))
    print("Total Hours Worked: " + str(totals['total_hours']))
    print("Total Gross Pay: %.2f" % float(totals['total_gross_pay']))
    print("Total Income Tax: %.2f" % float(totals['total_tax']))
    print("Total Net Pay: %.2f" % float(totals['total_net_pay']))
    print('Press any key to continue . . . ')


def func():
    total_employee_count = 0
    total_hours_worked = 0
    total_gross_pay = 0
    total_income_tax_rate = 0
    total_net_pay = 0
    totals_dict = {}
    for person in employees_information_list:
        gross_pay, tax_rate, tax_calc, net_pay = calculate_payroll(person[3], person[4], person[5])
        print_info(person[0], person[1], person[2], person[3], person[4], gross_pay, tax_rate, tax_calc, net_pay)
        total_employee_count = total_employee_count + 1
        total_hours_worked = total_hours_worked + float(person[3])
        total_gross_pay = total_gross_pay + float(gross_pay)
        total_income_tax_rate = total_income_tax_rate + float(tax_calc)
        total_net_pay = total_net_pay + float(net_pay)
    totals_dict['total_employee_count'] = total_employee_count
    totals_dict['total_hours'] = total_hours_worked
    totals_dict['total_tax'] = total_income_tax_rate
    totals_dict['total_net_pay'] = total_net_pay
    totals_dict['total_gross_pay'] = total_gross_pay
    print_all_info(totals_dict)


if __name__ == "__main__":
    employees_information_list = []
    condition = True
    # 1
    while condition:
        name = get_name()
        if name.lower() == 'end':
            func()
            condition = False
        else:
            information_list = []
            from_date, end_date = get_date()
            information_list.append(name)
            information_list.append(from_date)
            information_list.append(end_date)
            information_list.append(get_total_hours())
            information_list.append(get_hourly_rate())
            information_list.append(get_income_tax_rate())
            employees_information_list.append(information_list)


