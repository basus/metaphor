import os
from parser import Parser, Validator
from constructor import Constructor

print "Welcome to the Metaphor system"
prompt = "Enter the name of the Metaphor rule file to use"
input(prompt) = filename

rules = open(filename)
rule_parser = Parser(rules)
rule_parser.program()			#Calls a method in the parser, might have to be streamlined

rule_tree = rule_parser.astree
rule_validator = Validator(rule_tree)
rule_validator.program()

rule_env_patterns = rule_validator.env_patterns
rule_constructor = Constructor(rule_tree, rule_env_patterns)
