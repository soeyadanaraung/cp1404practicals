"""
Module to test the ProgrammingLanguage class.
Estimated time: 10 minutes
Actual time: 20 minutes
"""

from programming_language import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)
print(ruby)
print(visual_basic)

languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
