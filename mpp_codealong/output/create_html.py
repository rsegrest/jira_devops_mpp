driver_array_for_table = [
    ['row1 data', '123', '456'], ['row2data', '789', '10-11-12']]
# expected_table_body_string = '<table><tbody><tr><td>row1 data</td><td>123</td><td>456</td></tr><tr><td>row2 data</td><td>789</td><td>10-11-12</td></tr>'


def create_table_body_string(table_data):
    body_string = '<table><tbody>'
    for row in table_data:
        body_string += '<tr>'
        for cell in row:
            body_string += '<td>' + cell + '</td>'
        body_string += '</tr>'
    body_string += '</table></tbody>'
    return body_string
