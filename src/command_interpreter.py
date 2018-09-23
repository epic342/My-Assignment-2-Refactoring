from cmd import Cmd
from src import controller
import argparse
from src.database.statistics_creator import StatisticsCreator

class CommandLine(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        # Command line argument variables
        self.files = None
        self.statistics = None
        self.extracted_modules = None
        self.output = None
        self.args = self.register_arguments()
        self.parse_arguments()
        self.controller = controller.Controller(self)
        self.prompt = '> '

    def run_console(self):
        self.cmdloop('Starting prompt...\n'
                     'Type "help" for commands')

    def register_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-f",
            "--file",
            nargs="+",
            help="Multiple file input for parse")
        parser.add_argument(
            "-s",
            "--statistics",
            action='store_true',
            help="Print Statistics for classes uploaded")
        parser.add_argument(
            "-o",
            "--output",
            help="Setting name of the output location")
        return parser.parse_args()

    def parse_arguments(self):
        if self.args.statistics:
            self.statistics = StatisticsCreator("statistics")
            self.statistics.create_tables()
            print("Statistics collecting is turned on")
        # Created by Braeden
        if self.args.file is not None:
            self.files = self.args.file
            print("Files selected: ")
            print(*self.files, sep="\n")
        # Created by Michael Huang
        if self.args.output is not None:
            self.output = self.args.output
            print("Now setting names of output files")

    def do_enable_statistics(self, args):
        """
        Enabled statistics collection
        Author: Jake Reddock
        Syntax: enable_statistics
        """
        if self.controller.enable_statistics(args):
            print("Enabled statistics")
        else:
            print("Statistics pls")

    def do_show_statistics(self, args):
        """
        Show statistics about the analysed classes
        Author: Jake Reddock
        Syntax: show_statistics
        Requires: enable_statistics, output_to_dot
        """
        if self.controller.show_statistics(args):
            print("Showing statistics")
        else:
            print("Not showing statistics")

    def do_set_input_file(self, args):
        """
        Sets the input file that will be converted into a UML diagram.
        Author: Jake Reddock
        Syntax: set_input_file [file_name]
        """
        if self.controller.set_input_file(args):
            print("You have set the input file.")
        else:
            print("Failed to set an input file.")

    def do_output_to_dot(self, args):
        if self.controller.output_to_dot(args):
            print("You have outputted the file in dot format.")
        else:
            print("No dot file outputted.")

    def do_output_to_file(self, args):
        """
        Sets the output of the class diagram to a file location.
        Author: Michael Huang
        Syntax: output_to_file
                output_to_file [path]
        """
        if self.controller.output_to_file(args):
            print("You have successfully copied the file to your desired location.")
        else:
            print("Failed to copy the file to your location.")

    def do_output_to_png(self, args):
        """
        Converts dot file into PNG
        Author: Braeden
        """
        if self.controller.output_to_png(args) is not None:
            print("You have successfully outputted the file in png format.")
        else:
            print("no output to png")