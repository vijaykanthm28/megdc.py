import pkg_resources
import argparse
import logging
import textwrap
import os
import sys
import megdc



__header__ = textwrap.dedent("""

    Megam System  megdc-%s

Full documentation can be found at: http://docs.megam.io
""" % megdc.__version__)


def log_flags(args, logger=None):
    logger = logger or LOG
    logger.info('megdc options:')

    for k, v in args.__dict__.items():
        if k.startswith('_'):
            continue
        logger.info(' %-30s: %s' % (k, v))


def get_parser():
   parser = argparse.ArgumentParser(
        prog='megdc',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Datacenter ready in minutes \n\n%s' % __header__,
        )
   parser.add_argument(
        '--version',
        action='version',
        version='%s' % megdc. __version__,
        help='the current installed version of megdc',
        )

# create the top-level parser
   sub = parser.add_subparsers(
        title='commands',
        metavar='COMMAND',
        help='description',
        )
   entry_p = {}
   for ep in pkg_resources.iter_entry_points(group='megdc.cib',name= None) :
        if not entry_p.has_key(ep.dist):
           entry_p[ep.dist] = {}
        entry_p.update({eb.name:ep.load()})
        logger.info('dist -=> %s', ep.dist)
   entry_p.sort(key = lambda name, fn : getattr(fn, 'priority', 100))
   for (name, fn) in entry_points:
        p = sub.add_parser(
            name,
            description=fn.__doc__,
            help=fn.__doc__,
            )

        # flag if the default release is being used
        p.set_defaults(default_release=False)
        fn(p)
   parser.set_defaults(
        cluster='megam',
        )

   return parser

   args = parser.parse_args(sys.argv[1:])
   args.func(args)

#@catches((KeyboardInterrupt, RuntimeError, exc.DeployError,), handle_all=True)
def _main(args=None, namespace=None):
    '''    # Set console logging first with some defaults, to prevent having exceptions
    # before hitting logging configuration. The defaults can/will get overridden
    # later.

    # Console Logger
    sh = logging.StreamHandler()
    sh.setFormatter(log.color_format())
    sh.setLevel(logging.WARNING)

    # because we're in a module already, __name__ is not the ancestor of
    # the rest of the package; use the root as the logger for everyone
    root_logger = logging.getLogger()

    # allow all levels at root_logger, handlers control individual levels
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(sh)'''

    parser = get_parser()
    if len(sys.argv) <= 2:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args(args=args, namespace=namespace)

    ''' console_loglevel = logging.DEBUG  # start at DEBUG for now
    if args.quiet:
        console_loglevel = logging.WARNING
    if args.verbose:
        console_loglevel = logging.DEBUG

    # Console Logger
    sh.setLevel(console_loglevel)

    # File Logger
    fh = logging.FileHandler('{cluster}.log'.format(cluster=args.cluster))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(log.BASE_FORMAT))

    root_logger.addHandler(fh)

    # Reads from the config file and sets values for the global
    # flags and the given sub-command
    # the one flag that will never work regardless of the config settings is
    # logging because we cannot set it before hand since the logging config is
    # not ready yet. This is the earliest we can do.
    #args = megdc.conf.megdc.set_overrides(args)

    LOG.info("Invoked (%s): %s" % (
        megdc.__version__,
        join(sys.argv, " "))
    )
    log_flags(args)
    '''
    return args.func(args)


def main(args=None, namespace=None):
    try:
        _main(args=args, namespace=namespace)
    finally:
        # This block is crucial to avoid having issues with
        # Python spitting non-sense thread exceptions. We have already
        # handled what we could, so close stderr and stdout.
        if not os.environ.get('MEGAM_TEST'):
            try:
                sys.stdout.close()
            except:
                pass
            try:
                sys.stderr.close()
            except:
                pass
