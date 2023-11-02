
def reduce_decimal_string(number):
    """Takes a string that may have a floating point with
       too many significant digits after decimal 

    Args:
        string or number: number or number string 

    Returns:
        string: number string with only two decimals
    """
    # return number_string
    return_string = str(number)
    element_parts = return_string.split('.')
    if len(element_parts) > 1:
        if len(element_parts[1]) > 3:
            decimal = element_parts[1][:3]
            return_string = str(element_parts[0])+'.'+str(decimal)
    return return_string
