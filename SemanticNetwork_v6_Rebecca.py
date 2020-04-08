#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:15:37 2019

@author: Johanna
"""

import io
import numpy as np

modelfile = "cc.de.300.vec"
csv_file = 'Output_Rebecca.csv'

given_object = 'Rebecca begonnen studieren teilt Mitbewohnerin Helene Wochen Rebecca Helene anders Hexe Gefangen fesselnden Freundschaft entwickelt starke Verbindung Weg Studium zaubern'

#each item represents subject code and ideas of 1 person separated by '+'
data_list = ['1+verhext Studium+Bei Vollmond in der Vorlesung+4 Kröten Beine in der Mensa+Ein Scheiterhaufen zum Abschluss+Walpurgisnacht in den Ferien+Studentin So schwer wie eine Ente+Können sie schwimmen',
             '2+Studying Witchcraft+Algebra Abrakadabra+Bestes Hexe Exemplar+vor zaubern Studenten+Zauberei und Mathe 3+Wunschdenken',
             '3+WG verhext+verhext verliebt verzaubert+kommunale Einrichtung WG und Hexe+Boku life und Hexenkessel+Wie man mit einer Hexe zusammenlebt',
             '4+Zauberhaftes Lernen+Uni mit Überraschungen+Eine magische Mitbewohnerin+Zufällige Vorteile+Magisch gute Freundinnen+Rebecca und die Hexe',
             '5+Charming College+Abracadabra Uni+Salem U+It is not cheating if+Time flies+Dorm witches+No spells allowed+Why is the phone floating',
             '6+Rebecca verhext+Fessle mich Rebecca+Wir fegen durchs Studium+verhexen mich+Mit einem Besen lebt sichs leichter+Hexen Haar oh wunderbar',
             '7+Verhext und zugenäht+Molch Augen und Algebra+verhext Studium+13 Flüche für den Professor+Die verhexten Uni Jahre+Besen Ritt zum Abschluss',
             '8+Eine Freundschaft mit einer Hexe+Überraschung ich wohne mit einer Hexe zusammen+Studium und ein Hexen Leben+Alles steht Kopf im WG Leben',
             '9+Hogwarts University+Magische Freundschaft+Köpfchen und Stäbchen+Wie man einen Muggel hinters Licht führt+Magical Highschool Sequel+Zauberei im Studium wie man durch Zauberei schummelt+Helene Potter und ...+2 Freunde kein Todesfall+Die Zauber WG+Rebecca die normale',
             '10+Das zauberhafte Studienleben+Studieren ist doch keine eine Hexerei+Wie ich mich durchs Studium zauberte+Hexe Lily mal anders',
             '11+Die Mitbewohnerin Beschwörerin+Bücher Bier Besen+Immer der verfluchte Unistress+Organische Alchemie 1. Semester',
             '12+In der Regelstudienzeit durch Hexerei+Sexy Hexi und ihre heiße Mitbewohnerin+Ehe auf 3 Jahre Bis uns ein Zauber scheidet+Die Zauberformel zur 1+Die Rothaarige und ihre Studienkollegin+Hexerei im Studentenwohnheim',
             '13+Hexe Helene+Schummelei Zauberei+Best friend+Freundschaft mal anders+Die Hexe ohne Besen+study buddies+Gefangen oder erlöst+Fesselnde Freundschaft',
             '14+Helene die Hexe+Hexe am Campus+Meine Freundin ist eine Hexe+Hexen Studentin Helene+Rebecca und Helene+Studium Zauberei+Hex Helene Hex+Sie ist eine Hexe+Hexe Helene auf der Spur+Freundschaft+Hexe',
             '15+verhext Studium+Die Studentin auf dem Besen+Ein zauberhaftes Studium+Hexen studieren besser+Verhext gute Noten+Hogwarts ist für Anfänger',
             '16+Die spontane Hexe Helene+Freundschaft mit einer Hexe oder nicht+Meine Mitbewohnerin ist eine Hexe+Eine Hexe als Mitbewohnerin+durchs Studium gehext+Ein verhext Studium',
             '17+group work eine zauberhafte Geschichte+hex hex Uni ist weg+eine magische Unizeit+Studieren mit ein bisschen Magie+Gemeinsam zaubert es sich leichter+Zaubern muss gelernt sein',
             '18+Hexenhaus+Hermine Granger und die Kammer von Rebecca+Verhext schwierig+Meine Mitbewohnerin die Hexe+2 Zimmer Bad und Hexenkessel+Das Zauberei Studium+Hogwarts+Leben studieren zaubern',
             '19+Zwei Freundinnen+verhext Studium+Verhexte Freundinnen+Glückliches Hexen zum Master+Freundschaft wirkt+Mädels halten auch Hexen aus+Hexen leicht gemacht+Die Burschen waren wie verhext+Professor hex hex hex+Die Mädels kommen+Studium verliebt verhext geschafft+Mädels hexen halt+Heute wird überrascht+Ah so eine bist du+Freu mich dich kennenzulernen+Mädels WG täglich neu',
             '20+Zauberhafte Freundschaft+Studieren mit Magie+Die etwas andere Mitbewohnerin+Verhext auf der Uni+Helene oder Hexe',
             '21+verhext Studium+Zauberhafte Freundschaft+Hexen auf der Uni+Eine Hexe zur besten Freundin+Mit Besen und schwarzer Katze zur Uni',
             '22+Doch Hogwarts+Studium einfach gemacht+Wie verzaubert+Positiv aufgeladen gezaubert+Die etwas andere Freundschaft+Die schöne Helene kann auch anders+Von der Mitbewohnerin verhext+Zauberhaftes Studieren+Wies auf einmal wie von Zauberhand geht+Ganz anders',
             '23+Zauberhaftes Zeugnis+Arbeitsgruppe der besonderen Art+Hilfe meine Mitbewohnerin ist eine Hexe+Zauberei für Fortgeschrittene+Magische Mitbewohnerin+Sabrina die Studienjahre+Walpurgis WG+Zaubermittel gegen Prüfungsangst+Hexen 101+Wozu Auslandssemester',
             '24+Bezauberndes erstes Semester+Ein magischer Studienbeginn+Sich schnell und einfach durch die STEOP hexen+eine Uni ein Studium und eine Hexe+Verhexte Freundschaften auf der Uni+Universität Freundschaft der anderen Art',
             '25+Zauberhaftes Studium+Jung noch dumm und verzaubernd+magische Prüfungsergebnisse+verhext und gut studiert+wie leicht studieren sein kann+mit Zauber studieren macht mehr Freude+zauberhafte Studentinnen+die magische Studenten WG+eine bezaubernde WG',
             '26+ein zauberhaftes Studium+eine Hexe als Freundin+Rebecca und Helene ein verhexte Studium+Hilfe ich habe eine Hexe in meinem Zimmer+Hexen geht über lernen+die zauberhafte Mitbewohnerin+studieren für fortgeschrittene Magier+lieber Zauberstab als Kugelschreiber+zaubern muss man nicht studieren',
             '27+verhext+meine Freundin die Hexe+zauberhaft+mein neues Leben+das Studium der Hexenkunst+Hexenzauber+das Geheimnis+Helenes Geheimnis+ich werde eine Hexe+wie man eine Hexe wird',
             '31+die außergewöhnliche Freundschaft+die Studium Zauberei+Rebecca und ihre besondere Mitbewohnerin+Die Hexe+Warum fai bleiben wenn man auch Hexen kann+eine starke Verbindung+eine Freundschaft die kein gutes Ende nimmt+der zauberhafte Weg durchs Studium+Helene ist besonders',
             '32+Helene total verhext+fesselnde Freundschaft+verzaubernde Freundschaft+verhexte Freundschaft+verhexte Studium+Unzertrennlich verzaubert verhext+zauber Studium',
             '33+Hexe Helene und ihre Mitbewohnerin Becci+Achtung Hexe+Uni leicht gemacht mit Zauberei+Hilfe meine Mitbewohnerin ist eine Hexe+verzauberte Freundschaft+Ratgeber was tun wenn meine Freundin eine Hexe ist',
             '34+Hexenhaus verzaubertes Lernen+verhexte Freundschaft+Studium mal anders+verzauberte Freundschaft+hexen für gute Noten+verhexte Prüfung+Rebecca und Helene verhexen die Uni+Uni leicht gemacht+mit Hexen ans Ziel+zaubern um zu bestehen+Simsalabim Diplom Bachelor+Bachelor leicht gemacht',
             '35+einfach verhext+bezaubernd zaubern durch das Studium+hex hex Helene+Einfach durchs Studium fliegen+verhexte Freundschaft',
             '37+Hexen Studium+Freundschaft Hexerei+Zauber Studium+Helene Hexe studieren mit Rebecca Hexe als Hex+Studium Hexerei+Zauber Freundinnen+Studium als Hexerei+Hexen Band',
             '38+die große Überraschung+das Geheimnis der Freundin+mit Zauberei durchs Studium+Freundschaft hilft+meine Freundin die Hexe',
             '40+bezaubernd studieren+Helene die Hexe+die verhexten Freundinnen+Rebecca und ihr verhexte Freundin',
             '43+Mitbewohnerinnen fürs Leben+Helene und ich+Helene die Hexe+das Leben von Hexe Helene und Rebecca+die unglaubliche Helene+mit Hexen lebt es sich besser+ich kann nicht ohne Helene+Rebecca und Helene unzertrennlich+Rebecca und Helene das WG-Leben',
             '49+die verhexte Freundschaft+Hexe Helene+die bezaubernden Mitbewohnerinnen+die WG der Hexen+als Hexe ist das Studium gar nicht so schwer',
             '50+verhexte Studium+Rebecca und die verhexte Studien Partnerin+eine fast verhexte Freundschaft im Studium+eine verhexte Geschichte die mir niemand glaubt+verhext einfache Studienzeit',
             '52+verhexte Freundschaft+Hexe exzellent Zeit+zauberhafte Freundinnen+Hexe Helene+verliebt verhext verzaubert+ene meine mei befreundet sind die zwei',
             '53+eine zauberhafte Abschlussarbeit+Betrug oder Anwendung bestimmter Lernmethoden+Warum lernen wenn das Leben von allein geht+wie leicht studieren sein kann+Vorsicht Hexerei bitte nicht nachmachen+so hat sich Rebecca studieren wohl nicht vorgestellt',
             '54+zauberhaftes Studium+Rebecca die Besondere+Studieren mal anders+Freundschaft fesselt+Mitbewohner',
             '56+das Hexen Duo+die verwunschenen Mädchen+bezaubernde Studentinnen+zauberhafter Weg+in Freundschaft verzaubert+Hexenschule+Studium mit Schwung',
             '57+Rebecca und Helene+verhext Studium+stranger witches+Freundschaft bis zum Morgengrauen+magna cum magic+eta sigma Studium+Hexen Freundschaft+instant noodles Red Bull und Hexerei',
             '58+Hermine Granger+zauberhaft+Kartoffelbrei+Hogwarts+eins zwei drei Hexerei+verrückt wie zwei+Zauber Freundschaft+ein Besen zum Fliegen durchs Studium',
             '60+verzauberte Studienzeit+verzauberte Studienzeit+verhexte Freunde+gezaubert geteilt+Mitbewohnerin gehext+zauberhafte Studentin+zauberhaftes Studium+Hexen Studium+Hexen Uni+Uni Hexe+durch die Uni gezaubert']



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

def l2_norm(x):
   return np.sqrt(np.sum(x**2))

def div_norm(x):
   norm_value = l2_norm(x)
   if norm_value > 0:
       return x * ( 1.0 / norm_value)
   else:
       print('l2norm not found')
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
    print('Distance Rebecca vs. ', word2, ' = ', semantic_distance)
    semantic_distance = str(semantic_distance)
    sd_text = ';' + semantic_distance
    append(sd_text, csv_file)

###### INITIALIZING #######################################################

trytofindfile(csv_file)

#load model
model = load_vectors(modelfile)

wholegiven = given_object.split(' ') #splits 'Ohren putzen' into ['Ohren', 'putzen']

if len(wholegiven) > 1: # if the idea is a phrase (consists of multiple words)
    phrase_vector_list = []
    for eachword in wholegiven: # get vector for each single word
        word_vector = get_word_vector(eachword)
        phrase_vector_list.append(word_vector)  # append vector to a list of vectors of this phrase
    my_vector = get_phrase_vector(phrase_vector_list)
       
elif len(wholegiven) == 1: #if idea is just one word
    wholegiven = wholegiven[0]
    my_vector = get_word_vector(wholegiven)

else:
    print('Something went horribly wrong')

#create vector representing the given object
#list_object = model[given_object]
vector_object = my_vector
#############################################################



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
            print('Something went horribly wrong')

        get_semantic_distance(vector_object, my_vector, given_object, idea)

    #delete first subject's ideas from data
    data_list = data_list[1:]

###########################


