from learntools.core.utils import bind_exercises
from learntools.core.problem_factories import simple_problem
from learntools.core.richtext import CodeSolution as CS
from learntools.core.problem import *

class SumStringsWithNumbers(CodingProblem):
    _var = 'result'
    _hint = ''
    _solution = """It would be helpful to know whether New York City taxis
    vary prices based on how many passengers they have. Most places do not
    change fares based on numbers of passengers.
    If you assume New York City is the same, than only the top 4 features listed should matter. At first glance, it seems all of those should matter equally.
    """
    _solution = CS(
"""
result = str(1) + " is the first number." + '\n' + "And " + str(3.2) + " is a decimal"
""")
    def check(self, result_obj):
        assert result_obj == str(1) + " is the first number." + '\n' + "And " + str(3.2) + " is a decimal"

class FirstPermImportance(CodingProblem):
    _var = 'result'
    _hint = ''
    _solution = CS(
"""
numbers = [1,2,3]
new_list = []
result = 0
new_list.append(str(numbers[0]))
new_list.append(str(numbers[1]))
new_list.append(str(numbers[2]))
result = new_list[1]
""")
    def check(self, result_obj):
        assert result_obj == "2"

class WhyLatitude(CodingProblem):
    _var = 'result'
    _hint = ''
    _solution = CS(
"""
result = 0
numbers = [10, 20, 30, 40]
for n in numbers:
    result = result + n
""")
    def check(self, result_obj):
        assert result_obj == 100

class ImportanceWithAbsFeatures(CodingProblem):
    _var = 'result'
    _hint = ''
    _solution = CS(
"""
numbers = [1,2,3,4,5,6,7,8,9]
result = numbers[1::2] 
""")
    def check(self, result_obj):
        assert result_obj == [2,4,6,8]

class ScaleUpFeatureMagnitude(CodingProblem):
    _var = 'result'
    _hint = ''
    _solution = CS(
"""
x_list = [1,2,3,]
y_list = [3, "hello", 65]
# Replace these values
first_term = sum(x_list)
y_list.reverse() # remember that the `reverse()` operation does not have a result!
second_term = y_list[0]

result = first_term + second_term
""")
    def check(self, result_obj):
        assert result_obj == 71

class FromPermImportanceToMarginalEffect(CodingProblem):
    _var = 'result'
    _hint = ''
    _solution = CS(
"""
data = ["John", "Doe", 53.44]
result = f"Hello {data[0]} {data[1]}. Your current balance is ${data[2]}."
""")
    def check(self, result_obj):
        assert result_obj == "Hello John Doe. Your current balance is $53.44."

qvars = bind_exercises(globals(), [
    SumStringsWithNumbers,
    FirstPermImportance,
    WhyLatitude,
    ImportanceWithAbsFeatures,
    ScaleUpFeatureMagnitude,
    FromPermImportanceToMarginalEffect
    ],
    tutorial_id=131,
    var_format='q_{n}',
    )
__all__ = list(qvars)

