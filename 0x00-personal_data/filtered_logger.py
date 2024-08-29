#!/usr/bin/env python3
"""
This module contains a logging system that obfuscates
sensitive personal information (PII) from logs.
"""

import re
import logging
import os
import mysql.connector


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specified fields in the log message.

    Args:
        fields (list of str): Fields to obfuscate.
        redaction (str): The string to replace PII with.
        message (str): The original log message.
        separator (str): The character that separates key-value pairs.

    Returns:
        str: The log message with obfuscated fields.
    """
    pattern = f"({'|'.join(fields)})=([^({separator})]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to filter PII fields in logs.

    Attributes:
        REDACTION (str): The string to replace PII with.
        FORMAT (str): The log message format.
        SEPARATOR (str): The character that separates key-value pairs.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """
        Initializes the formatter with specific fields to obfuscate.

        Args:
            fields (list of str): Fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record):
        """
        Formats the log record, applying field filtering.

        Args:
            record (logging.LogRecord): The log record.

        Returns:
            str: The formatted log record with obfuscated fields.
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger():
    """
    Returns a logger object configured with PII filtering.

    Returns:
        logging.Logger: The configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    logger.addHandler(handler)

    return logger


def get_db():
    """
    Connects to a secure database and returns a MySQLConnection object.

    Returns:
        mysql.connector.connection.MySQLConnection: The database connection.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main():
    """
    Retrieves all rows in the users table and logs each row
    with PII fields obfuscated.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    logger = get_logger()

    for row in cursor:
        message = (
            f"name={row[0]}; email={row[1]}; phone={row[2]}; ssn={row[3]}; "
            f"password={row[4]}; ip={row[5]}; last_login={row[6]}; "
            f"user_agent={row[7]};"
        )
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
