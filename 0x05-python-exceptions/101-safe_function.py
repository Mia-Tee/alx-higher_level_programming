#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        g = fct(*args)
        return g
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
