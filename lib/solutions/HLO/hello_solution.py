

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) is str and not None:
        return f"Hello, {friend_name}!"
    return "Hello, World!"
