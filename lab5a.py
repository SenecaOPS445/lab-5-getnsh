#!/usr/bin/env python3
# Author ID: gchawla4

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."
    except PermissionError:
        return "Permission denied."

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return "File not found."
    except PermissionError:
        return "Permission denied."

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))