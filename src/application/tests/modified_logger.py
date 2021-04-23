# Imports
import os
import getpass
import shutil
import tkinter.filedialog
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path
import src.application.new_views.results as results


# This is a modified version of Mr. Fed's original logger program in the 'common' directory.
# This program works with the results.py program. It logs the grades shown in results.


class Logger:
    """This class configures the logger for the Math Facts program."""

    def __init__(self, log_file, message):
        """ Logger constructor. """
        # String constants
        self.app_log = logging.getLogger('root')
        self.COMMA = ","
        self.NEW_LINE = "\n"
        self.FORMATTED_DATE = "%m-%d-%Y_%H_%M_%S"
        self.END = "end"
        self.START = "start"
        # Work directory where the parent power data directory is located
        self.root_dir = str(self.get_project_root())
        # Set the scratch directory
        self.scratch_dir = self.root_dir + "/scratch/"
        # Program's root directory reference to locate files in the /common/ subdirectory
        self.properties_path = self.root_dir + "/src/common/properties/"
        self.log_dir = self.root_dir + "/scratch/logs/"
        self.log_file = log_file
        # Properties file name
        self.prop_file_name = "math_facts.properties"
        # Default properties file
        self.default_properties_file = self.root_dir + "/src/common/properties/" + self.prop_file_name
        # Define the common
        self.COMMON_PATH = self.root_dir + "/src/common/"
        # Numeric constants
        self.SIZE = 50
        self.MB = 1024 * 1024
        self.LOG_FILE_SIZE = self.SIZE
        # Initialize
        # If the scratch directory does not exist, create it
        if not os.path.exists(self.scratch_dir):
            os.makedirs(self.scratch_dir)
        # If the log directory does not exist, create it
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        # If log file does not exist, create it
        mode = 'a' if os.path.exists(self.log_dir + self.log_file) else 'w'
        with open(self.log_dir + self.log_file, mode) as f:
            # Code for writing to the log file.
            #f.write(f"Program started on {datetime.now()}\n")
            f.write(message)

        # self.config_logger()

    def get_datetime_string(self):
        """
        This function computes the current date and time and puts it in a string format
        :return: a string formatted to show month-day-year_Hour_Minute_Second
        """
        now = datetime.now()
        date = now.strftime(self.FORMATTED_DATE)
        return date

    def announce_run(self, mode):
        """
        This function writes an announcement to the log.
        :param mode: label to denote what to write on the log,
                     "start" writes the start of a new program run
                     "end" writes the end of a new program run
        :return: None
        """
        if mode == self.START:
            self.app_log.info("**********************************************************************")
            self.app_log.info(f"Math Facts App")
            self.app_log.info(f"Program started on {datetime.now()}")
            self.app_log.info(f"Maximum log file size allowed: {self.SIZE} MB. It rolls over after max size reached.")
        elif mode == self.END:
            self.app_log.info(f"Program ended on {datetime.now()}")
            self.app_log.info("----------------------------------------------------------------------")

    def load_properties(self, filepath, sep='=', comment_char='#'):
        """
        Jm!ha?0$@att
        This function loads the properties for the program.
        :param filepath: the path of the properties file
        :param sep: property separator
        :param comment_char: comment character
        :return: a python dictionary containing all the program properties
        """
        props = {}
        with open(filepath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
        return props

    def get_project_root(self) -> Path:
        return Path(__file__).parent.parent.parent.parent

    def config_logger(self):
        # Load properties
        properties_map = self.load_properties(self.default_properties_file)
        log_file_size = int(properties_map['logging.file.size'])

        # Set logging configuration
        log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
        logFile = self.log_dir + self.log_file
        my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=log_file_size * self.MB,
                                         backupCount=2, encoding=None, delay=0)
        my_handler.setFormatter(log_formatter)
        my_handler.setLevel(logging.INFO)
        self.app_log.setLevel(logging.INFO)
        self.app_log.addHandler(my_handler)

    def get_log_dir(self):
        return self.log_dir

    def get_log_file(self):
        return self.log_dir + self.log_file

    def print_log(self, type, msg):
        self.app_log.type(msg)


if __name__ == '__main__':
    logger = Logger('math_facts.log', f"Program started on {datetime.now()}\n")
    # Announce start of program
    logger.announce_run("start")
    # Announce end of program
    logger.announce_run("end")
