#!/usr/bin/env python3
'''returns a tuple'''


def index_range(page: int, page_size: int) -> tuple:
    """retuens a tuple"""
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
