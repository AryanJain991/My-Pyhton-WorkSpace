import argparse

parser = argparse.ArgumentParser(description="Simple Caculator")

parser.add_argument("num1", type=float, help="first Numeber")
parser.add_argument("num2", type=float, help="Second Numeber")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()

print(args)

if(args.operation == "add"):
    print(f"The Result is {args.num1 + args.num2}")

elif(args.operation == "sub"):
    print(f"The Result is {args.num1 - args.num2}")

elif(args.operation == "mul"):
    print(f"The Result is {args.num1 * args.num2}")

elif(args.operation == "div"):
    print(f"The Result is {args.num1 / args.num2}")

else:
    print("Pls Enter Valid Number")