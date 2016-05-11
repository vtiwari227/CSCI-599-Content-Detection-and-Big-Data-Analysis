import nltk
from nltk.tag import PerceptronTagger
from nltk.data import find

def extract_entity_names(t, label):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        if t.label() == label:
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child, label))
    return entity_names

PICKLE = "averaged_perceptron_tagger.pickle"
AP_MODEL_LOC = 'file:'+str(find('taggers/averaged_perceptron_tagger/'+PICKLE))
tagger = PerceptronTagger(load=False)
tagger.load(AP_MODEL_LOC)
pos_tag = tagger.tag
tokenized = nltk.word_tokenize('The quick brown fox  named Ron and Donald Trump jumps over the lazy dog')
tagged = pos_tag(tokenized)
namedEnt = nltk.ne_chunk(tagged, binary=True)
names = extract_entity_names(namedEnt, 'NE')
#check=pos_tag('The quick brown fox jumps over the lazy dog'.split())
print names

