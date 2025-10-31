"""
Define custom exceptions for Data Quality (DQ) failures.

This module provides exception classes to handle various data quality failure
scenarios, including schema mismatches and empty file detections.

Notes
-----
Use these exceptions to signal specific DQ failure conditions in data
processing pipelines.
"""


class DQFail(Exception):
    """
    Raise this exception for generic data quality (DQ) failures.

    Use this base class to signal a DQ failure in data processing pipelines.
    Subclass this exception to represent specific DQ failure scenarios.

    Parameters
    ----------
    message : str, optional
        The error message describing the DQ failure.

    Examples
    --------
    Raise a generic DQ failure:

        raise DQFail("DQ FAIL: Generic failure")
    """


class DQSchemaMismatchAndEmptyFile(DQFail):
    """
    Raise this exception for schema mismatch and empty file data quality (DQ)
    failures.

    Signal a DQ failure when both a schema mismatch and an empty file are
    detected during data processing.

    Parameters
    ----------
    message : str, optional
        The error message describing the DQ failure. Defaults to
        "DQ FAIL: SCHEMA MISMATCH AND EMPTY FILE".

    Examples
    --------
    Raise this exception when both a schema mismatch and an empty file are
    encountered:

        raise SchemaMismatchAndEmptyFile()
        raise SchemaMismatchAndEmptyFile("Custom error message")
    """

    def __init__(self, message="DQ FAIL: SCHEMA MISMATCH AND EMPTY FILE"):
        super().__init__(message)


class DQSchemaMismatch(DQFail):
    """
    Raise this exception for schema mismatch data quality (DQ) failures.

    Signal a DQ failure when a schema mismatch is detected during data
    processing.

    Parameters
    ----------
    message : str, optional
        The error message describing the DQ failure. Defaults to
        "DQ FAIL: SCHEMA MISMATCH".

    Examples
    --------
    Raise this exception when a schema mismatch is encountered:

        raise SchemaMismatch()
        raise SchemaMismatch("Custom error message")
    """

    def __init__(self, message="DQ FAIL: SCHEMA MISMATCH"):
        super().__init__(message)


class DQEmptyFile(DQFail):
    """
    Raise this exception for empty file data quality (DQ) failures.

    Signal a DQ failure when an empty file is detected during data processing.

    Parameters
    ----------
    message : str, optional
        The error message describing the DQ failure. Defaults to
        "DQ FAIL: EMPTY FILE".

    Examples
    --------
    Raise this exception when an empty file is encountered:

        raise EmptyFile()
        raise EmptyFile("Custom error message")
    """

    def __init__(self, message="DQ FAIL: EMPTY FILE"):
        super().__init__(message)


# eof
