#!/usr/bin/python

import sys
import subprocess

# full path to ...-linux-android-addr2line binary
ADDR2LINE_BINARY = ''

# dictionary with full path to your .so files
LIBS = {
    '': ''
}

class DecodedFrame():
    number = ''
    address = ''
    lib = ''
    output = ''

lines = []
decoded_frames = []

def input_frames():
    print('Paste the stack trace. Press ENTER two times to submit. CTRL-C to exit.')
    while True:
        try:
            line = input()
            if not line:
                break
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            break
        lines.append(line)


def print_progress(current):
    sys.stdout.write("\rProgress:" + str(current) + "/" + str(len(lines)))
    sys.stdout.flush()


def process_frames():
    i = 0
    print('Please wait:')

    for line in lines:
        parsedFrame = parse_frame(line)
        get_parsed_result(parsedFrame)
        decoded_frames.append(parsedFrame)
        print_progress(i)
        i += 1


def print_frames():
    print("\n---------- Decoded Stacktrace: ----------------")

    for item in decoded_frames:
        print(item.number)
        print(item.output)


def parse_frame(line):
    result = DecodedFrame()

    if '.0x' in line:
        splitted = line.split('.')
        result.address = splitted[1]
        result.lib = splitted[0] + ".so"

    else:
        splitted = line.split(' ')
        result.number = splitted[0]
        result.address = splitted[2]
        result.lib = splitted[3]

    return result


def get_parsed_result(frame):
    output = ""

    if frame.lib in LIBS:
        output = subprocess.run([ADDR2LINE_BINARY, '-a', '-s', '-f', '-e', LIBS[frame.lib], frame.address],
                                stdout=subprocess.PIPE,
                                universal_newlines=True)
        frame.output = output.stdout
    else:
        frame.output = "[No dsym found] " + frame.number + " " + frame.address + " " + frame.lib + "\n"

def main():
    input_frames()
    process_frames()
    print_frames()


if __name__ == '__main__':
    main()
