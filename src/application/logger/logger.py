# **************************************************************************
#  This file is to serve as an example.
# **************************************************************************

# Imports
import os
import shutil
import tkinter.filedialog
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# ****************************************************
# Global Variables
# ****************************************************
processed_files_list = []
processed_directories = []
payloads = {}

# ****************************************************
# Constants
# ****************************************************

# String formatting strings
COMMA = ","
NEW_LINE = "\n"
FORMATTED_DATE = "%m-%d-%Y_%H_%M_%S"
END = "end"
START = "start"

# Numeric
SIZE = 50
MB = 1024 * 1024
LOG_FILE_SIZE = SIZE
# ****************************************************
# Function Definition
# ****************************************************

def get_datetime_string():
    """
    This function computes the current date and time and puts it in users_list string format
    :return: users_list string formatted to show month-day-year_Hour_Minute_Second
    """
    now = datetime.now()
    date = now.strftime(FORMATTED_DATE)
    return date

def announce_run(mode):
    """
    This function writes an announcement to the log.
    :param mode: label to denote what to write on the log,
                 "start" writes the start of users_list new program run
                 "end" writes the end of users_list new program run
    :return: None
    """
    if mode == START:
        app_log.info("**********************************************************************")
        app_log.info(f"Running the MPS Power Data Analyzer Tool")
        app_log.info(f"Program started on {datetime.now()}")
        app_log.info(f"Maximum log file size allowed: {SIZE} MB. It rolls over after max size reached.")
    elif mode == END:
        app_log.info(f"Program ended on {datetime.now()}")
        app_log.info("----------------------------------------------------------------------")

def load_properties(filepath, sep='=', comment_char='#'):
    """
    This function loads the properties for the program.
    :param filepath: the path of the properties file
    :param sep: property separator
    :param comment_char: comment character
    :return: users_list python dictionary containing all the program properties
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

# *****************************************************************************************
# **************v******************************************************v*******************
#                                       Main Program
# **************^******************************************************^*******************
# *****************************************************************************************

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Define directories and system files to use
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Work directory where the parent power data directory is located
WORK_DIR = tkinter.filedialog.askdirectory()
# Program's root directory reference to locate files in the /common/ subdirectory
COMMON_PATH = os.path.dirname(os.path.dirname(__file__)) + "/common"


# Load properties
properties_map = load_properties(WORK_DIR + "/math_facts.properties")
LOG_FILE_SIZE = int(properties_map['logging.file.size'])

# Set logging configuration
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
logFile = WORK_DIR + "/math_facts.log"
my_handler = RotatingFileHandler(logFile, mode='users_list', maxBytes=LOG_FILE_SIZE * MB,
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)
app_log.addHandler(my_handler)

# Announce start of program
announce_run(START)


# Announce end of program
announce_run(END)