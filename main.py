import operations_rational as op
import choice as ty
import operations_complex as opCom


type = ty.type()

while type ==  '1':
    op.mainterminal()

if type == '2':
    repeat = True
    while repeat == True:
        operands = opCom.insert_numbers()
        if operands[2] == "+":
            opCom.record_in_file(opCom.addition(opCom.take_rational_part(operands[0]), opCom.take_symbol(operands[0]), opCom.take_imaginary_part(operands[0]), opCom.take_rational_part(operands[1]), opCom.take_symbol(operands[1]), opCom.take_imaginary_part(operands[1])))
        elif operands[2] == "-":
            opCom.record_in_file(opCom.deduction(opCom.take_rational_part(operands[0]), opCom.take_symbol(operands[0]), opCom.take_imaginary_part(operands[0]), opCom.take_rational_part(operands[1]), opCom.take_symbol(operands[1]), opCom.take_imaginary_part(operands[1])))
        elif operands[2] == "*":
            opCom.record_in_file(opCom.multiply(opCom.take_rational_part(operands[0]), opCom.take_symbol(operands[0]), opCom.take_imaginary_part(operands[0]), opCom.take_rational_part(operands[1]), opCom.take_symbol(operands[1]), opCom.take_imaginary_part(operands[1])))
        else:
            opCom.record_in_file(opCom.division(opCom.take_rational_part(operands[0]), opCom.take_symbol(operands[0]), opCom.take_imaginary_part(operands[0]), opCom.take_rational_part(operands[1]), opCom.take_symbol(operands[1]), opCom.take_imaginary_part(operands[1])))
        repeat = opCom.repeat_or_no()