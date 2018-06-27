#!/usr/local/bin/python2.7
# encoding: utf-8
'''
tcrunner -- A test case runner for QA automation process

tcrunner is designed to automatically excecute test cases, manage logs
and produce results.

It defines classes_and_methods

@author:     ERM

@copyright:  2018 mobomo. All rights reserved.

@license:    license

@contact:    eduardo@mobomo.com
@deffield    updated: 10/4/2018

TODO List:
 - Include a separate configuration FIle
 - Add a useful way to target different test groups.
 - Improve the logging and report generation

'''

import sys
import os
import inspect
import shlex
from lettuce.bin import main as lettuce

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from libs import builtins

__all__ = []
__version__ = 0.1
__date__ = '2018-03-16'
__updated__ = '2018-03-16'
PROFILE = 0


class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''

    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg

    def __str__(self):
        return self.msg

    def __unicode__(self):
        return self.msg


def o_run_test(testpath, options):
    """ Runs all tests in the given path or runs the given test if only one is provided
    """
    # raise ValueError('lettuce {} -v {} {}'.format(options,
    # builtins.VERBOSITY_LEVEL, testpath))

    args = '{} -t-{} -v {} {}'.format(options, builtins.DEVICE, builtins.VERBOSITY_LEVEL, testpath)
    status = -1
    if type(args) == str:
        args = shlex.split(args)

    try:
        lettuce(args)
        # Lettuce always raises a SystemExit, so something bad
        # has happened.  Fail.
        status = 1
    except SystemExit as e:
        status = e.code
    # finally:
    #     return status


def run_test(testpath, options):
    
    rc = os.system('lettuce {} -t-{} -t-{} -v {} {}'.format(options, builtins.DEVICE, builtins.ENVIRONMENT,
                                                builtins.VERBOSITY_LEVEL, testpath))
    # TODO: Use log files
    return rc


def main(argv=None):  # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (
        program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by ERM on %s.
  Copyright 2018 mobomo. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(
            description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-V', '--version', action='version',
                            version=program_version_message)
        parser.add_argument('-e', '--env', dest="env",
                            help="select the environment to run tests (dev, local)", default="dev")
        parser.add_argument('-d', '--device', dest="device",
                            help="select the device to run the device (iphone, ipad, nexus)", default="default")
        parser.add_argument('-f', '--filter', dest="filt",
                            help="apply filters to the scenarios in the given path", default=None)
        parser.add_argument('-o', '--options', dest="opts",
                            action='append', help="options to pass on to lettuce")
        parser.add_argument(
            dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", default="Tests", nargs='+')

        # Process arguments
        args = parser.parse_args()
        opts = args.opts
        scenario_filter = args.filt
        paths = args.paths
        env = args.env
        device = args.device

        #recurse = args.recurse
        # inpat = args.include
        # expat = args.exclude

        if builtins.VERBOSITY_LEVEL > 0:
            print("Verbose mode on")
            # todo: print default options
            if builtins.RECURSIVE:
                print("Recursive mode on")
            else:
                print("Recursive mode off")

        # prepare variables for testcase run
        # TODO: Load default setup from config.json and overwrite default
        # builtins configuration

        # set up options
        options = ""
        if scenario_filter:
            options += " -t {}".format(scenario_filter)

        # set environment
        builtins.ENVIRONMENT = env

        # set up device
        builtins.DEVICE = device

        # set up special paths
        builtins.PROJ_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        builtins.set_up_paths(["libs", "proj"])

        result = []
        final_rc = 0
        for inpath in paths:
            if builtins.RECURSIVE:
                for feature_file in builtins.get_features_from_path(inpath):
                    rc = int(run_test(feature_file, options))
                    result.append([feature_file, rc])
                    final_rc = rc if rc else final_rc
            else:
                final_rc = int(run_test(inpath, options))
                result.append([inpath, final_rc])

        builtins.print_result(result)
        return 0 if not final_rc else 1
    # except KeyboardInterrupt:
    #    ### handle keyboard interrupt ###
    #    return 0
    except Exception, e:
        if builtins.DEBUG or builtins.TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    if builtins.DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if builtins.TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'aux_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
