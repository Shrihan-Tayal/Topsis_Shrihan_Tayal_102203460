from topsis.topsis import Topsis

# Test the package
Topsis.calculate(
    input_file='data.xlsx',
    weights='1,1,1,2,2',
    impacts='+,+,-,+,-',
    output_file='output.xlsx'
)
