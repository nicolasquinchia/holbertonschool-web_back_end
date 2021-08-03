#!/usr/bin/env python3
"""This module holds a Regex-ing task
"""

import logging
from typing import List
import re
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """The function should use a regex to replace
    occurrences of certain field values
    Args:
        fields (List[str]): Strings representing all fields
        redaction (str):
        [String representing by what the field will be obfuscated
        message (str): String representing the log line
        separator (str):
        String representing by which character is separating all fields
    Returns:
        str: [The log message obfuscated]
    """
    for index in fields:
        message = re.sub(index + "=[^=]*" + separator,
                         index + "=" + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor method sets the initial
        atributes of the instance
        Args:
            fields (List[str])
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Method to filter values in incoming log records
        Args:
            record (logging.LogRecord):
            Keep information in memory until it is processed
        Returns:
            str:
            Filtered values ​​on incoming records using filter_datum
        """
        return filter_datum(
            self.fields, self.REDACTION, super(
                RedactingFormatter, self).format(record),
            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Method that takes no arguments
    Returns:
        logging.Logger: Logging.Logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Method that allows connection to a database
    Returns:
        mysql.connector.connection.MySQLConnection:Connector to the database
    """
    username = "PERSONAL_DATA_DB_USERNAME"
    password = "PERSONAL_DATA_DB_PASSWORD"
    host = "PERSONAL_DATA_DB_HOST"
    db_name = "PERSONAL_DATA_DB_NAME"
    my_db = mysql.connector.connection.MySQLConnection(
        user=os.getenv(
            username, "root"), password=os.getenv(
            password, ""), host=os.getenv(
                host, "localhost"), database=os.getenv(db_name))
    return my_db
