#!/usr/bin/env python3

import re

if __name__ == '__main__':
    herit_pattern_str = r'\w*herit\w*'
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)

    input_file = "origin.txt"
    output_file = "herit_results.txt"
