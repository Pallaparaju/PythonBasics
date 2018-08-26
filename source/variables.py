""""Variables"""

# alt+insert --> to seet he module operation
# shift +alt +f10 --> to execute the operation
# shift +f10 --> to return to the previous execution

emp_name = "Pallaparaju Mallipudi"  # string
emp_id = 2067  # integer
emp_email = "imraju2067@gmail.com"
emp_salary = 234567.70  # float
emp_address = "8926 N Scrmshaw Dr" \
              "Apt 201" \
              "Peoria" \
              "Illinois-61615"
emp_phone = 8163287083

system_ip = "10.3.4.5"

print(emp_name, '\n', emp_id, '\n', emp_salary, '\n', emp_address, '\n', emp_phone, '\n', system_ip)

# DB_NAME =10#
# print(db_name)                 UNSUPPORTED#

# THREE VARIABLES ASSIGNED TO SAME VALUE
a = b = c = 1
print(a)
print(b)
print(c)

# Multiple Variables to multiple values
a, b, c = 1, 20.23, "Python"
print(a, b, c)
print(id(a), id(b), id(c))
