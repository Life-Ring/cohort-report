# Command-line utility for creating the LifeRing cohort report
#
# To run:
#
#    python3 cohort-report.py build
#

import argparse
import sys
from typing import List

def __collect() -> None:
    """Collect data to build out the cohort report."""
    print("TODO: Collect data to build report")

def __build() -> None:
    """Build the cohort report."""
    print("TODO: Build the cohort report")

def __main(args: List[str]) -> None:
    """Cohort report main method.
    
    Parse command-line arguments and dispatch to the appropriate underlying function."""
    parser = argparse.ArgumentParser(
        prog="cohort-report",
        description="Collects data for and creates the LifeRing cohort report.",
    )
    subparsers = parser.add_subparsers(help="sub-command help", dest='subcmd')
    collect = subparsers.add_parser('collect', help='collect help')
    collect = subparsers.add_parser('build', help='build help')
    
    parsed = parser.parse_args(args)

    if parsed.subcmd == "collect":
        __collect()
    elif parsed.subcmd == "build":
        __build()


if __name__ == "__main__":
    __main(sys.argv[1:])
