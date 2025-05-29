#!/usr/bin/env python3

"""
LightWeight Useful Library (lwul)

A minimal, zero-dependency collection of utility functions for Python.
"""

__version__ = "1.0.0"

# ─────────────────────────────────────
# ANSI Color Wrappers

def red(text): return "\033[31m" + text + "\033[0m"
def green(text): return "\033[32m" + text + "\033[0m"
def yellow(text): return "\033[33m" + text + "\033[0m"
def blue(text): return "\033[34m" + text + "\033[0m"
def magenta(text): return "\033[35m" + text + "\033[0m"
def cyan(text): return "\033[36m" + text + "\033[0m"
def white(text): return "\033[37m" + text + "\033[0m"

# ─────────────────────────────────────
# ANSI Text Styles

def italic(text): return "\033[3m" + text + "\033[0m"
def underline(text): return "\033[4m" + text + "\033[0m"
def reverse(text): return "\033[7m" + text + "\033[0m"

# ─────────────────────────────────────
# Status Message Formatters

def info(text): return "\033[33m[i] " + text + "\033[0m"
def warn(text): return "\033[31m[!] " + text + "\033[0m"

# ─────────────────────────────────────
# Demo

if __name__ == "__main__":
    # Colors
    print(red("This text is red."))
    print(green("This text is green."))
    print(yellow("This text is yellow."))
    print(blue("This text is blue."))
    print(magenta("This text is magenta."))
    print(cyan("This text is cyan."))
    print(white("This text is white."))
    print()

    # Styles
    print(italic("This text is italic."))
    print(underline("This text is underlined."))
    print(reverse("This text is reversed."))
    print()

    # Messages
    print(info("This is an informational message."))
    print(warn("This is a warning message."))
