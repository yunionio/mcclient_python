"""
Command-line interface to the API server.
"""

import argparse
import httplib2
import sys
import readline
import shlex

import yunionclient.api.client
from yunionclient import __version__
from yunionclient.common import exceptions as exc
from yunionclient.common import utils
import importlib


class APIShell(object):
    def __init__(self, command_dict):
        self.command_dict = dict(command_dict)

    def get_base_parser(self):
        parser = argparse.ArgumentParser(
            prog='climc',
            description=__doc__.strip(),
            epilog='See "climc help COMMAND" '
                   'for help on a specific command.',
            add_help=False,
            formatter_class=HelpFormatter,
        )

        # Global arguments
        parser.add_argument('-h', '--help',
            action='store_true',
            help=argparse.SUPPRESS,
        )

        parser.add_argument('--debug',
            default=False,
            action='store_true',
            help=argparse.SUPPRESS)

        #parser.add_argument('--insecure',
        #    default=False,
        #    action='store_true',
        #    help=argparse.SUPPRESS)

        parser.add_argument('--timeout',
            default=600,
            help='Number of seconds to wait for a response')

        parser.add_argument('--os-username',
            default=utils.env('OS_USERNAME'),
            help='Defaults to env[OS_USERNAME]')

        parser.add_argument('--os_username',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-password',
            default=utils.env('OS_PASSWORD'),
            help='Defaults to env[OS_PASSWORD]')

        parser.add_argument('--os_password',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-project-id',
            default=utils.env('OS_PROJECT_ID'),
            help='Defaults to env[OS_PROJECT_ID]')

        parser.add_argument('--os_project_id',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-project-name',
            default=utils.env('OS_PROJECT_NAME'),
            help='Defaults to env[OS_PROJECT_NAME]')

        parser.add_argument('--os_project_name',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-domain-name',
            default=utils.env('OS_DOMAIN_NAME', default='Default'),
            help='Defaults to env[OS_DOMAIN_NAME]')

        parser.add_argument('--os_domain_name',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-auth-url',
            default=utils.env('OS_AUTH_URL'),
            help='Defaults to env[OS_AUTH_URL]')

        parser.add_argument('--os_auth_url',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-region-name',
            default=utils.env('OS_REGION_NAME'),
            help='Defaults to env[OS_REGION_NAME]')

        parser.add_argument('--os-zone-name',
            default=utils.env('OS_ZONE_NAME'),
            help='Defaults to env[OS_ZONE_NAME]')

        parser.add_argument('--os_region_name',
            help=argparse.SUPPRESS)

        parser.add_argument('--os_zone_name',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-api-version',
            default=utils.env('OS_API_VERSION', default='1'),
            help='Defaults to env[OS_API_VERSION] or 1')

        parser.add_argument('--os_api_version',
            help=argparse.SUPPRESS)

        parser.add_argument('--os-endpoint-type',
            default=utils.env('OS_ENDPOINT_TYPE', default='publicURL'),
            choices=['publicULR', 'internalURL'],
            help='Defaults to env[OS_ENDPOINT_TYPE] or publicURL')

        parser.add_argument('--os_endpoint_type',
            help=argparse.SUPPRESS)

        parser.add_argument('--export-client-desc',
            help='Export client description into a file')

        parser.add_argument('--import-client-desc',
            help='Import client description from a file')

        return parser

    def get_subcommand_parser(self, version):
        parser = self.get_base_parser()

        self.subcommands = {}
        subparsers = parser.add_subparsers(metavar='<subcommand>')
        submodule = utils.import_module('shells')
        self._find_actions(subparsers, submodule)
        self._find_actions(subparsers, self)

        return parser

    def _find_actions(self, subparsers, actions_module):
        for attr in (a for a in dir(actions_module) if a.startswith('do_')):
            # I prefer to be hypen-separated instead of underscores.
            command = attr[3:].replace('_', '-')
            callback = getattr(actions_module, attr)

            desc = callback.__doc__ or ''
            help = desc.strip().split('\n')[0]
            arguments = getattr(callback, 'arguments', [])

            subparser = subparsers.add_parser(command,
                help=help,
                description=desc,
                add_help=False,
                formatter_class=HelpFormatter
            )
            subparser.add_argument('-h', '--help',
                action='help',
                help=argparse.SUPPRESS,
            )
            self.subcommands[command] = subparser
            _args = []
            for (args, kwargs) in arguments:
                for item in args:
                    _args.append(item)
                subparser.add_argument(*args, **kwargs)
            subparser.set_defaults(func=callback)
            self.command_dict.setdefault(command, _args)

        readline.set_completer(BufferAwareCompleter(self.command_dict).complete)
        # Deal with special characters('-', '<', '>')
        DEFAULT_DELIMS = readline.get_completer_delims()
        DEFAULT_DELIMS = DEFAULT_DELIMS.replace('-', '')
        DEFAULT_DELIMS = DEFAULT_DELIMS.replace('<', '')
        DEFAULT_DELIMS = DEFAULT_DELIMS.replace('>', '')
        readline.set_completer_delims(DEFAULT_DELIMS)
        # Use the tab key for completion
        readline.parse_and_bind('tab: complete')

    def main(self, argv, flag):
        if not argv and flag==1:
            print('Welcome to yunionclient interactive mode. version %s' % __version__)
            print('Type "help" for help or "help COMMAND" for a specific command.')
            print('Enter "quit/exit" to exit console.')
            return 0

        # Parse args once to find version
        parser = self.get_base_parser()
        (options, args) = parser.parse_known_args(argv)

        # build available subcommands based on version
        api_version = options.os_api_version
        subcommand_parser = self.get_subcommand_parser(api_version)
        self.parser = subcommand_parser

        # Prompt the user for text
        if flag == 2:
            input_cmd = input("yunion_cli> ")
            if input_cmd is None:
                return None
            else:
                input_cmd = input_cmd.strip()
                if input_cmd == '':
                    return None
                if input_cmd == 'quit' or input_cmd == 'exit':
                    sys.exit(0)

            try:
                argv = shlex.split(input_cmd, posix=True)
            except ValueError as e:
                print('args parse error: %s' % e)
                return 0

        # Handle top-level --help/-h before attempting to parse
        # a command off the command line
        if options.help:
            self.do_help(options)
            return 0

        # Parse args again and call whatever callback was selected
        try:
            args = subcommand_parser.parse_args(argv)
        except SystemExit:
            return 0

        # Deal with global arguments
        if args.debug:
            httplib2.debuglevel = 1

        # Short-circuit and deal with help command right away.
        if args.func == self.do_help:
            self.do_help(args)
            return 0

        if not args.os_username and not args.import_client_desc:
            raise exc.CommandError("You must provide a username via"
                        " either --os-username or env[OS_USERNAME]")

        if not args.os_password and not args.import_client_desc:
            raise exc.CommandError("You must provide a password via"
                        " either --os-password or env[OS_PASSWORD]")

        if not (args.os_project_id or args.os_project_name) and \
                not args.import_client_desc and \
                getattr(args, 'show_projects', None) is None:
            args.os_project_name = args.os_username

        if not args.os_auth_url and not args.import_client_desc:
            raise exc.CommandError("You must provide an auth url via"
                        " either --os-auth-url or via env[OS_AUTH_URL]")

        args.insecure = True
        if args.import_client_desc:
            client = yunionclient.api.client.Client(None, None, None, None,
                                            timeout=args.timeout,
                                            insecure=args.insecure)
            client.from_file(args.import_client_desc)
        else:
            client = yunionclient.api.client.Client(args.os_auth_url,
                                        args.os_username,
                                        args.os_password,
                                        args.os_domain_name,
                                        region=args.os_region_name,
                                        zone=args.os_zone_name,
                                        endpoint_type=args.os_endpoint_type,
                                        timeout=args.timeout,
                                        insecure=args.insecure)
            if (args.os_project_name is not None and \
                    len(args.os_project_name) > 0) or \
                    (args.os_project_id is not None and \
                        len(args.os_project_id) > 0):
                if not client.set_project(project_name=args.os_project_name,
                                project_id=args.os_project_id):
                    raise exc.CommandError("Invalid Keystone credentials.")
        try:
            args.func(client, args)
            if args.export_client_desc:
                client.to_file(args.export_client_desc)
        except exc.Unauthorized:
            raise exc.CommandError("Invalid Keystone credentials.")
        except exc.ClientException as e:
            print(e)
            if flag == 1 and argv:
                sys.exit(-1)

    @utils.arg('command', metavar='<subcommand>', nargs='?',
               help='Display help for <subcommand>')
    def do_help(self, args):
        """
        Display help about this program or one of its subcommands.
        """
        if getattr(args, 'command', None):
            if args.command in self.subcommands:
                self.subcommands[args.command].print_help()
            else:
                raise exc.CommandError("'%s' is not a valid subcommand" %
                                       args.command)
        else:
            self.parser.print_help()

        print('Enter \"quit/exit\" to exit console.')

    def get_options(self, argv):
        """
        Get options for climc completion
        """
        # Parse args once to find version
        parser = self.get_base_parser()
        (options, args) = parser.parse_known_args(argv)

        # build available subcommands based on version
        api_version = options.os_api_version
        subcommand_parser = self.get_subcommand_parser(api_version)
        self.parser = subcommand_parser

        return self.command_dict

class HelpFormatter(argparse.HelpFormatter):
    def start_section(self, heading):
        # Title-case the headings
        heading = '%s%s' % (heading[0].upper(), heading[1:])
        super(HelpFormatter, self).start_section(heading)

    def _split_lines(self, text, width):
        if text.startswith('M|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)

#Refer to some standard method
class BufferAwareCompleter(object):
    def __init__(self, options):
        self.options = options
        self.current_candidates = []
        #return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = list(self.options.keys())
                    else:
                        # later word
                        first = words[0]
                        candidates = self.options[first]
                    if being_completed:
                        # match options with portion of input being completed
                        self.current_candidates = [w for w in candidates if w.startswith(being_completed)]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates
                except (KeyError, IndexError) as err:
                    self.current_candidates = []
                    raise err
        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        return response


def setup_utf8():
    default_encoding = 'utf-8'

    if sys.getdefaultencoding() != default_encoding:
        importlib.reload(sys)
        sys.setdefaultencoding(default_encoding)


def main():

    setup_utf8()
    # Console init state
    cli_flag = 1

    # Dict to register our completer parameters
    command_dict = {}
    api_shell = APIShell(command_dict)

    while True:
        try:
            # Deal with the direct command without interactive action
            api_shell.main(sys.argv[1:], cli_flag)

            if len(sys.argv) == 1:
                # Deal with interactive commands
                cli_flag = 2
            else:
                break
        except Exception as e:
            if httplib2.debuglevel == 1:
                raise
            else:
                print(e, file=sys.stderr)
            sys.exit(1)
