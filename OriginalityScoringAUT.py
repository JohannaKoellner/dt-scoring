#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:15:37 2019

@author: Johanna
"""

import io
import numpy as np

modelfile = "cc.de.300.vec" #can be downloaded from https://fasttext.cc/docs/en/crawl-vectors.html
csv_file = 'Büroklammer_output.csv'

given_object = """add given object here as a string"""

#each item represents subject code and ideas of 1 person separated by '+'
data_list = [""" add ideas here in the following format: 'subject1+idea1+idea2+...','subject2+idea1+...' """]



#################### FUNCTIONS ###########################

def openfile(file_name):
    f = open(file_name,'r')
    f.close()

def writefile(file_name):
    f = open(file_name,'w')
    f.close()

def trytofindfile(file_name):
    try:
        openfile(file_name)
    except FileNotFoundError:
        writefile(file_name)
        
def append(text, file_name):
    f = open(file_name,'a')
    f.write(text)
    f.close()
    
def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = np.array(list(map(float, tokens[1:])))
        #data[tokens[0]] = [float(i) for i in tokens[1:]]
    return data

def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according 
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)

###### INITIALIZING #######################################################

trytofindfile(csv_file)

#load model
model = load_vectors(modelfile)

#create vector representing the given object
list_object = model[given_object]
vector_object = np.array(list_object)
#############################################################

def l2_norm(x):
   return np.sqrt(np.sum(x**2))

def div_norm(x):
   norm_value = l2_norm(x)
   if norm_value > 0:
       return x * ( 1.0 / norm_value)
   else:
       print('l2 norm not found')
       return x

def get_phrase_vector(wordvec_list):
    sumofnormvecs = 0
    for item in wordvec_list:
        sumofnormvecs += div_norm(item)
    avg = sumofnormvecs / len(wordvec_list)
    return avg
        
    
def get_word_vector(word):
    try:
        list_idea = model[word]
        vector_idea = np.array(list_idea)
        return vector_idea
    except KeyError:
        print(word, 'was not found in the model.')
        return vector_object
        
def get_semantic_distance(vector1, vector2, word1, word2):
    semantic_distance = 1 - cos_sim(vector1, vector2)
    semantic_distance = round(semantic_distance, 2)
    print('Distance ', word1, ' vs. ', word2, ' = ', semantic_distance)
    semantic_distance = str(semantic_distance)
    sd_text = ';' + semantic_distance
    append(sd_text, csv_file)


######### HERE'S THE MAGIC GOING ON ###################################

while data_list != []:
    #create list from first item of data
    idea_list = data_list[0].split('+') #results in e.g. ['1','Ohren putzen', 'Handy']
    
    #first item of idea_list is subject number
    #write subject number in csv file (new line)
    text = ' \n' + str(idea_list[0])
    append(text, csv_file)
    
    #delete subject number
    idea_list = idea_list[1:] # results in ['Ohren putzen', 'Handy']
    
    #create vector representing each idea & calculating distance to object
    # also check the .pages document in literature folder
    for idea in idea_list:
        wholeidea = idea.split(' ') #splits 'Ohren putzen' into ['Ohren', 'putzen']
        
        if len(wholeidea) > 1: # if the idea is a phrase (consists of multiple words)
            phrase_vector_list = []
            for eachword in wholeidea: # get vector for each single word
                word_vector = get_word_vector(eachword)
                phrase_vector_list.append(word_vector)  # append vector to a list of vectors of this phrase
            my_vector = get_phrase_vector(phrase_vector_list)
               
        elif len(wholeidea) == 1: #if idea is just one word
            wholeidea = wholeidea[0]
            my_vector = get_word_vector(wholeidea)
        
        else:
            print('Something went wrong.')

        get_semantic_distance(vector_object, my_vector, given_object, idea)

    #delete first subject's ideas from data
    data_list = data_list[1:]

###########################


