import io
from contextlib import redirect_stdout

import pycli_example.cmd


def test_secure_url():
    assert 'https' in pycli_example.cmd.EXAMPLE_URL


def test_args():
    args = pycli_example.cmd.parse_args([])
    assert args.json is False
    assert args.name is None

    args = pycli_example.cmd.parse_args(['-j'])
    assert args.json is True
    assert args.name is None

    args = pycli_example.cmd.parse_args(['-n', 'Frasier'])
    assert args.json is False
    assert args.name == 'Frasier'


def test_status_message():
    f = io.StringIO()
    with redirect_stdout(f):
        pycli_example.cmd.status_message('foo')
    assert f.getvalue() == '\rfoo'


def test_reset_status():
    f = io.StringIO()
    with redirect_stdout(f):
        msg = 'foo'
        pycli_example.cmd.status_message(msg)
        pycli_example.cmd.reset_status(len(msg))
    assert f.getvalue() == '\rfoo\r   \r'
