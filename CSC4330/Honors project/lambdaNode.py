class LambdaNod():
    def __init__(self, expr_type, **any_num_of_args):
        self._kind = expr_type
        self._free = set()
        if expr_type == "var":
            self._name = any_num_of_args["name"]
        elif expr_type == "apply":
            self._opr = any_num_of_args["opr"]
            self._oprsa = any_num_of_args["oprsa"]
        elif expr_type == "lambda":
            self._bind = any_num_of_args["bind"]
            self._body = any_num_of_args["body"]
        elif expr_type == "op":
            self._oprator = any_num_of_args["oprator"]
            self._left = any_num_of_args["left"]
            self._right = any_num_of_args["right"]
        elif expr_type == "number":
            self._value = float(any_num_of_args["value"])

    def __str__(self):
        expr_type = self._kind
        if expr_type == "var":
            return self._name
        elif expr_type == "number":
            return str(self._value)
        elif expr_type == "apply":
            return f"({self._opr} {self._oprsa})"
        elif expr_type == "lambda":
            return f"(lambda {self._bind} {self._body})"
        elif expr_type == "op":
            return f"({self._oprator} {self._left.__str__()} {self._right.__str__()})"

    # Returns a property object, so that the type of the node can be accessed anywhere we need it to
    @property
    def type(self):
        return self._kind

class OperationN():
    def __init__(self, oper_type, tree, **any_num_of_args):
        self._lambda = tree
        if oper_type == "eval":
            self._kind = "eval"
        elif oper_type == "fv":
            self._kind = "fv"
        elif oper_type == "alpha":
            self._kind = "alpha"
            self._naya = any_num_of_args["nay_nam"]
        elif oper_type == "sub":
            self._kind = "sub"
            self._sub_var = any_num_of_args["sub_var"]
            self._sub_expr = any_num_of_args["sub_expr"]

    def __str__(self):
        # Stringifies the operation node and shoots it out
        return f"{self._kind}, {self._lambda}"