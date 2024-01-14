def jsonify_decorator(function):
    """
    Let’s say we have a python code where we want all the output to be in JSON format.
    It doesn’t make sense to include code for these in each of the methods as it
    makes the lines of code redundant.
    In such cases, we can handle this with a decorator.
    Args:
        function:

    Returns:

    """

    def modify_output():
        return {"output": function()}

    return modify_output


@jsonify_decorator
def hello():
    """
    The method decorator is also referred to as the wrapper, which wraps the output of the function, that it decorates.
    In the above code sample, jsonify-decorator is the decorator method.
    We have added this decorator to hello() and add().
    The output of these method calls will now be wrapped and decorated with the jsonify_decorator.
    Returns:

    """
    return 'hello world'


@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1) + int(num2)


print(hello())
print(add())
