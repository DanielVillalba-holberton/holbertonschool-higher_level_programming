#!/usr/bin/python3
""" module append"""


def append_write(filename="", text=""):
    """docs for append write"""
    ch_w = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        ch_w += f.write(text)
        f.close()
    return ch_w
