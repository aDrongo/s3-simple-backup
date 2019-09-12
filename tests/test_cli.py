import pytest

from S3Backup import cli

target = "./test.txt"
bucket = "bucket"

@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser(parser):
    args = parser.parse_args([target, bucket])
    assert args.target == target
    assert args.bucket == bucket
