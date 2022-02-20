import argparse







def main():
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg1', help='arg1 help')
    parser.add_argument('--arg2', help='arg2 help')
    args = parser.parse_args()
    print("arg1 {}, arg2 {}".format(args.arg1, args.arg2))
    print("hello brother")

