from time import sleep
from modules import constants
from exceptions.custom_exceptions import ValidationError, CTypeError
from modules.common_fun import validate_date, is_in_list, c_msg


def y_or_n(input_str):
    answer = input("\n"+input_str+" ... y/N ")
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        print("Insert y or n ...")
        sleep(1)
        return y_or_n(input_str)

def date_input(msg="", nullable=True):
    date_inp = input(msg+" -- insert a date in a valid date format (DD-MM-YYYY) ")
    if validate_date(date_inp, nullable):
        return date_inp
    return date_input(msg, nullable)


def define_input_key(input_data):
# this function is used to validate user's data
    key = None
    param_keys = list(constants.params.keys())
    for el in param_keys:
        if el == input_data:
            key = el
    return key

def validate_input(value,input_data):
    key = define_input_key(input_data)
    if value == "":
        return
    elif key == "brand":
        if not is_in_list(constants.brand_list, value):
            raise ValidationError("Insert a valid brand: ({})".format(constants.brand_list))
    elif key == "price":
        try:
            value = int(value)
            if value < 500:
                raise ValidationError("Are you kidding? You're buying a car... value must be above 500")
        except Exception:
            raise CTypeError("Please insert a valid numeric value between 500 and 1000000")
    elif key == "fuel":
        if value not in constants.fuel:
            raise ValidationError("The fuel entered doesn't belong to the available list: {}".format(constants.fuel.keys()))


def handle_input_request(input_string):
    try:
        value = input(f"{input_string}: ")
        validate_input(value, input_string)
        return value
    except Exception as e:
        print(e)
        return handle_input_request(input_string)


def get_inputs():
    user_params = {
        "fuel":None,
        "brand":None,
        "price":None
    }
    param_keys = constants.params.keys()
    for param in param_keys:
        user_params[param] = handle_input_request(param)
    return user_params