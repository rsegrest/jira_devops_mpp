def check_key(o, k):
    """Check if key exists in object"""
    if o is None:
        return False
    if k in o:
        return True
    else:
        return False
