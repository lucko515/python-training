import argparse
import os
import sys

# Command-line parsing with argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description="A script for command-line parsing and system management.")
    parser.add_argument("--name", type=str, required=True, help="Your name")
    parser.add_argument("--age", type=int, required=True, help="Your age")
    return parser.parse_args()

# System management with os, sys
def system_management():
    print("Current Working Directory:", os.getcwd())
    print("System Path:", sys.path)
    
def main():
    args = parse_arguments()
    print(f"Name: {args.name}, Age: {args.age}")
    system_management()

if __name__ == "__main__":
    main()
