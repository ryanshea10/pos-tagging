#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ryanshea
"""

# convert file to list and remove unwanted elements
def conllu_to_list(raw_file) :
    for i in range(len(raw_file)):
        raw_file[i] = raw_file[i].split()
    
    prepped_train = []
    for i in range(len(raw_file)):
        if len(raw_file[i]) == 0:
            prepped_train.append(['\n'])
        elif raw_file[i][0].isnumeric():
            prepped_train.append([raw_file[i][2], '|||',raw_file[i][3]])
    
    return prepped_train

# convert list to a string to be exported
def list_to_text(prepped_file):
    for i in range(len(prepped_file)):
        prepped_file[i] = "".join(prepped_file[i])
    
    train = ""
    for i in prepped_file:
        if i != "\n":
            train += i + " "
        else:
            train += i
    
    return train

# write format data and write to a .txt file
def format_data(input_path, output_path):
    
    with open(input_path, encoding='utf8') as inp:
        raw_file = inp.readlines()
    
    prepped_file = conllu_to_list(raw_file)
    final_text = list_to_text(prepped_file)

    file = open(output_path, 'w')
    file.write(final_text)
    file.close()
    
    
format_data("en_gum-ud-train.conllu", "training_set.txt")
format_data("en_gum-ud-test.conllu", "test_set.txt")
format_data("en_gum-ud-dev.conllu", "dev_set.txt")










