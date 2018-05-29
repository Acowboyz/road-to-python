# create a factory
class OperationFactory(object):
    def create_operator(self, op):
        if op == '+':
            return AddOperation()
        elif op == '-':
            return MinusOperation()
        elif op == '*':
            return MultiplyOperation()
        elif op == '/':
            return DivideOperation()


# create a common class for the product
class Operation(object):
    def calc(self, num1, num2):
        pass


# create real products for operation
class AddOperation(Operation):
    def calc(self, num1, num2):
        print("the result is {}".format(num1 + num2))


class MinusOperation(Operation):
    def calc(self, num1, num2):
        print("the result is {}".format(num1 - num2))


class MultiplyOperation(Operation):
    def calc(self, num1, num2):
        print("the result is {}".format(num1 * num2))


class DivideOperation(Operation):
    def calc(self, num1, num2):
        try:
            print("the result is {}".format(num1 / num2))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    op_factory = OperationFactory()
    # add operation
    op_add = op_factory.create_operator('+')
    op_add.calc(1, 2)
    # minus operation
    op_minus = op_factory.create_operator('-')
    op_minus.calc(1, 2)
    # multiply operation
    op_multiply = op_factory.create_operator('*')
    op_multiply.calc(1, 2)
    # divide operation
    op_divide = op_factory.create_operator('/')
    op_divide.calc(1, 0)
