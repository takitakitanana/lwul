#!/usr/bin/env python3

"""
LightWeight Useful Library (lwul)

A minimal, zero-dependency collection of utility functions for Python.
"""

__version__ = "1.1.2"

# ─────────────────────────────────────
# ANSI Color Wrappers

def red(text): """Wrap text in red ANSI color."""; return "\033[31m" + text + "\033[0m"
def green(text): """Wrap text in green ANSI color."""; return "\033[32m" + text + "\033[0m"
def yellow(text): """Wrap text in yellow ANSI color."""; return "\033[33m" + text + "\033[0m"
def blue(text): """Wrap text in blue ANSI color."""; return "\033[34m" + text + "\033[0m"
def magenta(text): """Wrap text in magenta ANSI color."""; return "\033[35m" + text + "\033[0m"
def cyan(text): """Wrap text in cyan ANSI color."""; return "\033[36m" + text + "\033[0m"
def white(text): """Wrap text in white ANSI color."""; return "\033[37m" + text + "\033[0m"

# ─────────────────────────────────────
# ANSI Text Styles

def italic(text): """Wrap text in ANSI italic style."""; return "\033[3m" + text + "\033[0m"
def underline(text): """Wrap text in ANSI underline style."""; return "\033[4m" + text + "\033[0m"
def reverse(text): """Wrap text in ANSI reverse video style."""; return "\033[7m" + text + "\033[0m"

# ─────────────────────────────────────
# Status Message Formatters

def info(text): """Format text as [i] info message in yellow."""; return "\033[33m[i] " + text + "\033[0m"
def warn(text): """Format text as [!] warning message in red."""; return "\033[31m[!] " + text + "\033[0m"

# ─────────────────────────────────────
# Misc Functions

def gibberish(length):
    """Generate a random string of specified length (letters, digits, symbols)."""
    from random import choices
    import string
    char_set = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choices(char_set, k=length))

def slowprint(text, min_delay=0.05, max_delay=0.15):
    """Print text one character at a time, simulating human typing."""
    from time import sleep
    from random import uniform
    from sys import stdout
    for char in text + '\n':
        stdout.write(char)
        stdout.flush()
        sleep(uniform(min_delay, max_delay))

def timestamp(fmt="%Y-%m-%d %H:%M:%S"):
    """Return current date and time as a string (default format: YYYY-MM-DD HH:MM:SS)."""
    from datetime import datetime
    return datetime.now().strftime(fmt)

def pretty_json(data):
    """Pretty-print a Python dict (or JSON string) as formatted JSON."""
    import json

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return "[!] Invalid JSON string."

    return json.dumps(data, indent=4, sort_keys=True)

# ─────────────────────────────────────
# Web

def status_code(url):
    """Return HTTP status code for a URL."""
    import urllib.request
    request = urllib.request.Request(url, method='HEAD')
    with urllib.request.urlopen(request) as response:
        return response.getcode()

def response_headers(url):
    """Return response headers for a URL as a dict-like object."""
    import urllib.request
    with urllib.request.urlopen(url) as response:
        return dict(response.getheaders())

# ─────────────────────────────────────
# Demo

if __name__ == "__main__":

    # Version
    print(f"lwul v{__version__}\n")

    # Colors
    print(red("This text is red()."))
    print(green("This text is green()."))
    print(yellow("This text is yellow()."))
    print(blue("This text is blue()."))
    print(magenta("This text is magenta()."))
    print(cyan("This text is cyan()."))
    print(white("This text is white()."))
    print()

    # Styles
    print(italic("This text is italic()."))
    print(underline("This text is underline()."))
    print(reverse("This text is reverse()."))
    print()

    # Messages
    print(info("This is a info() message."))
    print(warn("This is a warn() message."))
    print()

    # Misc
    print(f"Here is some gibberish() text -> {reverse(gibberish(16))}.")
    slowprint("This is printed using slowprint() func.")
    print(f"Current timestamp -> {timestamp()} using timestamp().")
    print("pretty_json(json string) ->")
    print(pretty_json('{"project":"lwul","version":"1.1.0","active":true}'))
    print()

    # Web
    print(f"status_code('https://example.com') -> {status_code('https://example.com')}")
    print("response_headers('https://example.com') ->")
    print(pretty_json(response_headers('https://example.com')))
    print()
