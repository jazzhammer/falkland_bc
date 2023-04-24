import random
import isbnlib

"""
The International Standard Book Number (ISBN) is a unique identifier for books, 
consisting of 13 digits (formerly 10 digits). The ISBN is composed of five parts, 
each separated by hyphens, as follows:

Prefix element: 
    The prefix element is currently composed of either "978" or "979", 
    which identifies the book as an ISBN-13.
Registration group element: 
    The registration group element identifies the particular country, 
    geographical region, or language area participating in the ISBN system. 
    This element is a single digit between 0 and 9, 
    or "X" for the special case of the English language registration group.
Registrant element: 
    The registrant element identifies the publisher or imprint of the book. 
    This element is a variable length, between 1 and 7 digits.
Publication element: 
    The publication element identifies the specific edition, format, and version of the book. 
    This element is a variable length, between 1 and 6 digits.
Check digit: 
    The final digit of the ISBN is a check digit, calculated using a formula that ensures the accuracy and integrity of the ISBN.

Here's an example ISBN-13 with its corresponding parts labeled:

978-0-393-04002-9
Prefix: 978
Registration group: 0
Registrant: 393
Publication element: 04002
Check digit: 9
"""


def compose_isbn(options):
    prefix = options['prefix']
    if prefix != 978 and prefix != 979:
        raise ValueError('prefix must be 978 or 979')
    registration_group = options['registration_group']
    if registration_group < 0 or registration_group > 9:
        raise ValueError('registration_group must be 0 through 9')
    registrant = options['registrant']
    if isinstance(registrant, str):
        if registrant.isnumeric():
            if registrant >=1 and registrant <= 9999999:
                pass
            raise ValueError('registrant must be a 1-7 digit string or value from 1 through 9999999')
        else:
            raise ValueError('registrant must be a 1-7 digit string or value from 1 through 9999999')
    elif isinstance(registrant, int):
        if registrant >= 1 and registrant <= 9999999:
            pass
        else:
            raise ValueError('registrant must be a 1-7 digit string or value from 1 through 9999999')
    publication_element = options['publication_element']
    if isinstance(publication_element, str):
        if publication_element.isnumeric():
            if publication_element >=1 and publication_element <= 999999:
                pass
            raise ValueError('publication_element must be a 1-6 digit string or value from 1 through 999999')
        else:
            raise ValueError('publication_element must be a 1-6 digit string or value from 1 through 999999')
    elif isinstance(publication_element, int):
        if publication_element >= 1 and publication_element <= 999999:
            pass
        else:
            raise ValueError('publication_element must be a 1-6 digit string or value from 1 through 999999')
    checksum = options['checksum']
    if checksum == None:
        print('calculating checksum...')
        concatenated = '{}{}{}{}'.format(prefix, registration_group, registrant, publication_element)
        checksum = isbnlib.check_digit10(concatenated) if len(concatenated) == 9 else isbnlib.check_digit13(concatenated)
    else:
        print(f'using checksum {checksum}')
    """
    Composes an ISBN-13 given the known parts of the number.
    :param prefix: The prefix of the ISBN-13 (e.g. '978')
    :param registration_group: The registration group element of the ISBN-13
    :param registrant: The registrant element of the ISBN-13
    :param publication_element: The publication element of the ISBN-13
    :param checksum: The checksum digit of the ISBN-13
    :return: The composed ISBN-13
    """
    isbn = '{}-{}-{}-{}-{}'.format(prefix, registration_group, registrant, publication_element, checksum)
    return isbn
