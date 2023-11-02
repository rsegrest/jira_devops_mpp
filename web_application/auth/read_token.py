def read_token():
    """ Read token from text file, return token string
        Add your token to a file called 'token.txt' in this directory
    """
    with open('auth/token.txt', 'r', encoding='utf-8') as file:
        token = file.read()
    return token
