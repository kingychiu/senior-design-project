# sklearn
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
# other classes
from file_io import FileIO
import re


class PreProcess:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        lines = FileIO.read_file_to_lines(self.file_path)
        # spiting labels and sentences
        sentences = [l.split('\\C')[1].split(',')[0] for l in lines]
        print('## First sentence')
        print(sentences[0])
        sentences = [(lambda str: re.sub("[^a-zA-Z]", " ", str))(sentence) for sentence in
                     sentences]
        sentences_in_ascii = [self.sentence_to_ascii_list(sentence) for sentence in sentences]
        print('## First sentence in ascii codes')
        print(sentences_in_ascii[0])
        print()

        sentences_in_ascii = self.fixing_dimension(sentences_in_ascii)
        sentences_in_one_hot_vector = self.generate_one_hot_vector(sentences_in_ascii)
        labels = [l.split('\\C')[0] for l in lines]
        return labels, sentences_in_one_hot_vector

    def sentence_to_ascii_list(self, s):
        return [ord(char.lower()) - ord('a') for char in list(s)]

    def fixing_dimension(self, data):
        fix_size = 40
        for i in range(0, len(data)):
            if len(data[i]) >= fix_size:
                data[i] = data[i][:fix_size]
            else:
                diff = fix_size - len(data[i])
                data[i] += (diff * [26])
        print('Fixing all sentences to ', fix_size, ' char')
        return data

    def generate_one_hot_vector(self, data):
        # create one hot vector
        one_hot_tensor = []
        for d in data:
            one_hot_matrix = []
            for char in d:
                one_hot_vector = ['0'] * 27
                if char >= 0:
                    one_hot_vector[char] = '1'
                else:
                    one_hot_vector[26] = '1'
                one_hot_matrix.append(one_hot_vector)
            one_hot_tensor.append(one_hot_matrix)
        return one_hot_tensor


p = PreProcess('./datasets/ag_dataset_10000_each.txt')
labels, tensor = p.run()

with open('./datasets/ag_dataset_10000_each_one_hot.txt', 'w', encoding='utf8') as f1:
    document_strs = []
    for matrix in tensor:
        char_strs = []
        for vector in matrix:
            char_str = ','.join(vector)
            char_strs.append(char_str)
        document_str = '|c|'.join(char_strs)
        document_strs.append(document_str)
    lines = []
    for i in range(len(document_strs)):
        lines.append(labels[i] + '|l|' + document_strs[i])
    f1.write('\n'.join(lines))
