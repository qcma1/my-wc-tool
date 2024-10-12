import argparse
import os 
import sys
import locale

def get_num_bytes(filename: str) -> int:
    return os.path.getsize(filename)

def get_num_lines(filename: str) -> int:
    with open(filename, mode="r") as f:
        return sum(1 for line in f)
    
def get_num_words(filename: str) -> int:
    with open(filename, mode="r") as f:
        return len(f.read().split())
    
def get_num_bytes_from_stdin(raw_data: bytes) -> int:
    return len(raw_data)

def get_num_lines_from_stdin(raw_data: bytes) -> int:
    return raw_data.count(b'\n')

def get_num_words_from_stdin(raw_data: bytes, encoding: str) -> int:
    str_data = raw_data.decode(encoding=encoding)
    return len(str_data.split())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="my_wc",
        description="My own simplified wc unix tool for coding challenge",
    )
    parser.add_argument("-c", help="return the number of characters/bytes in the file", action="store_true")
    parser.add_argument("-l", help="return the number of lines in the file", action="store_true")
    parser.add_argument("-w", help="return the number of words in the file", action="store_true")
    parser.add_argument("-m", 
                        help="return the number of characters in the file with consideration to multibyte characters", 
                        action="store_true"
                        )

    parser.add_argument("filename", nargs="*") # use "+" if there is >= 1 positional arguments. "*" -> >= 0.
    args = parser.parse_args()

    if not args.filename:
        raw_data = sys.stdin.buffer.read()
        encoding = locale.getpreferredencoding()
        if args.c:
            print(get_num_bytes_from_stdin(raw_data))
        elif args.l:
            print(get_num_lines_from_stdin(raw_data))
        elif args.w:
            print(get_num_words_from_stdin(raw_data, encoding))
        elif args.m:
            data_str = raw_data.decode(encoding=encoding)
            print(len(data_str))
        else:
            print(get_num_lines_from_stdin(raw_data), get_num_words_from_stdin(raw_data, encoding), get_num_bytes_from_stdin(raw_data))
    else:
        if args.c:
            for fn in args.filename:
                print(get_num_bytes(fn))
        elif args.l:
            for fn in args.filename:
                print(get_num_lines(fn))
        elif args.w:
            for fn in args.filename:
                print(get_num_words(fn))
        elif args.m:
            for fn in args.filename:
                with open(fn, mode="r", newline="") as f:
                    content = f.read() # returns entire file content in a single string
                print(len(content))
        else:
            for fn in args.filename:
                print(get_num_lines(fn), get_num_words(fn), get_num_bytes(fn))
