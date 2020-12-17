# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = claimzai.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging
import utilities

from claimzai import __version__

__author__ = "nadavsegal"
__copyright__ = "nadavsegal"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="ClaimzAI {ver}".format(ver=__version__))
    parser.add_argument(
        "--n",
        dest="n",
        help="n-th Fibonacci number",
        type=int,
        metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    # logging.basicConfig(level=loglevel, stream=sys.stdout,
    #                     format=logformat, datefmt="%Y-%m-%d %H:%M:%S")
    logging.basicConfig(filename='./src/claimzai.log', level=loglevel,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")
    logging.getLogger().addHandler(logging.StreamHandler())


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    logging.getLogger('matplotlib.font_manager').disabled = True
    args.extend(['--n', '40', '--verbose', '--very-verbose'])
    args = parse_args(args)
    setup_logging(args.loglevel)

    data = utilities.PrepareData()
    data.clean()
    data.add()

    descriptive = utilities.Descriptive(data)
    descriptive.top_chart()


    utilities.predictive()
    utilities.prescriptive()


    process_frame.init_bbox()
    _logger.debug("Starting crazy calculations...")
    print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
