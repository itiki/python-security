#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from jinja2 import Template

# sys.argv[1] = '{{ this is a test }}'

# template = Template("Your input: {}".format(sys.argv[1] if len(sys.argv) > 1 else '<empty>'))
# data = "{{ __import__('os').system('clear') }}"
data = """{% for c in [].__class__.__base__.__subclasses__() %} 
              {% if c.__name__ == 'open' %} {{ c }} {% endif %} 
              {%% __import__('os').system('clear') %%}
          {% endfor %}"""
# data = """{{ open('testt.txt', 'w') }}"""
input_data = "Your input {}".format(data)
template = Template(input_data)
# template.globals['os'] = os
print template.render()
