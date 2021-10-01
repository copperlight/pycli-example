import argparse
import json
import sys
import time
from argparse import Namespace
from typing import List

import requests

EXAMPLE_URL = 'https://jsonplaceholder.typicode.com/posts'


def parse_args(argv: List[str]) -> Namespace:
    parser = argparse.ArgumentParser('Example Python CLI')
    parser.add_argument('-n', '--name', type=str, help='say hello to this name')
    parser.add_argument('-j', '--json', action='store_true', help='fetch some sample json data')
    return parser.parse_args(argv)


def status_message(msg: str) -> None:
    sys.stdout.write('\r' + msg)
    sys.stdout.flush()


def reset_status(length: int) -> None:
    status_message(' ' * length)
    status_message('')


def countdown(msg: str) -> None:
    last_msg_len = 0

    for i in range(3, 0, -1):
        m = f'{i} ' + msg
        status_message(m)
        last_msg_len = len(m)
        time.sleep(1)

    reset_status(last_msg_len)


def say_hello(args: Namespace) -> None:
    countdown(f'Preparing to say hello...')
    print(f'Hello, {args.name}!')


def fetch_json() -> None:
    countdown(f'Preparing to fetch json...')
    r = requests.get(EXAMPLE_URL)

    if r.ok:
        data = r.json()
        print(f'Download successful ({r.status_code}), data has {len(data)} entries.')
        print(f'The contents of the 10th entry:')
        print(json.dumps(data[10], indent=4, sort_keys=True))
    else:
        print('Download failed.')


def main() -> None:
    args = parse_args(sys.argv[1:])

    if args.name:
        say_hello(args)
    elif args.json:
        fetch_json()


if __name__ == '__main__':
    main()
