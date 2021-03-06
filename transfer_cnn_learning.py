# numpy
import numpy as np
# keras
from keras.utils import np_utils
from keras.models import load_model, Sequential, Model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import SGD, Adam, Adadelta
# sklearn
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
# other
from file_io import FileIO
import datetime


### DATA ###
def get_data(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
        tensor = []
        labels = []
        for line in lines:
            matrix = []
            labels.append(line.split('|l|')[0])
            char_look_up_list = line.split('|l|')[1].split(',')
            for char_look_up in char_look_up_list:
                look_up_vector = []
                for digit_str in char_look_up:
                    if digit_str == '0' or digit_str == '1':
                        look_up_vector.append(int(digit_str))
                matrix.append(look_up_vector)
            tensor.append(matrix)
        print(tensor[0])
        x = np.array(tensor)
        del tensor
        print(x.shape)
        classes = sorted(list(set(labels)))
        y = np.asarray([classes.index(item) for item in labels])
        print('Labels', classes)
        # shuffle
        x, y = shuffle(x, y, random_state=0)
        ## cut
        x = x[:50000]
        y = y[:50000]
        print(len(x))
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
        f.close()
        return x_train, x_test, y_train, y_test, len(classes)


x_train = {}
x_test = {}
y_train = {}
y_test = {}
num_classes = {}
x_train['ag1'], x_test['ag1'], y_train['ag1'], y_test['ag1'], num_classes['ag1'] = get_data(
    './datasets/ag_7blkup_10000each.txt')
x_train['ag2'], x_test['ag2'], y_train['ag2'], y_test['ag2'], num_classes['ag2'] = get_data(
    './datasets/ag2_7blkup_10000each.txt')
x_train['bbc'], x_test['bbc'], y_train['bbc'], y_test['bbc'], num_classes['bbc'] = get_data(
    './datasets/bbc_7blkup.txt')
# Convert class vectors to binary class matrices
y_train['ag1'] = np_utils.to_categorical(y_train['ag1'], num_classes['ag1'])
y_train['ag2'] = np_utils.to_categorical(y_train['ag2'], num_classes['ag2'])
y_train['bbc'] = np_utils.to_categorical(y_train['bbc'], num_classes['bbc'])
y_test['ag1'] = np_utils.to_categorical(y_test['ag1'], num_classes['ag1'])
y_test['ag2'] = np_utils.to_categorical(y_test['ag2'], num_classes['ag2'])
y_test['bbc'] = np_utils.to_categorical(y_test['bbc'], num_classes['bbc'])
# Reshape
x_train['ag1'] = x_train['ag1'].reshape(x_train['ag1'].shape[0], x_train['ag1'].shape[1],
                                        x_train['ag1'].shape[2], 1)
x_train['ag2'] = x_train['ag2'].reshape(x_train['ag2'].shape[0], x_train['ag2'].shape[1],
                                        x_train['ag2'].shape[2], 1)
x_train['bbc'] = x_train['bbc'].reshape(x_train['bbc'].shape[0], x_train['bbc'].shape[1],
                                        x_train['bbc'].shape[2], 1)
x_test['ag1'] = x_test['ag1'].reshape(x_test['ag1'].shape[0], x_test['ag1'].shape[1],
                                      x_test['ag1'].shape[2], 1)
x_test['ag2'] = x_test['ag2'].reshape(x_test['ag2'].shape[0], x_test['ag2'].shape[1],
                                      x_test['ag2'].shape[2], 1)
x_test['bbc'] = x_test['bbc'].reshape(x_test['bbc'].shape[0], x_test['bbc'].shape[1],
                                      x_test['bbc'].shape[2], 1)
### END OF DATA ###

### COMMON CNN LAYERS TEMPLATE###
input_shape = (x_train['ag1'].shape[1], x_train['ag1'].shape[2], x_train['ag1'].shape[3])
epoch_step = 1


def create_cnn_layers():
    init_model = Sequential()
    init_model.add(Convolution2D(2 ** 7, 3, 3,
                                 border_mode="same",
                                 input_shape=input_shape))
    init_model.add(Activation('relu'))
    init_model.add(Convolution2D(2 ** 7, 3, 3, border_mode='same'))
    init_model.add(Activation('relu'))
    init_model.add(MaxPooling2D(pool_size=(4, 2)))
    init_model.add(Dropout(0.25))

    init_model.add(Convolution2D(2 ** 8, 3, 3, border_mode='same'))
    init_model.add(Activation('relu'))
    init_model.add(Convolution2D(2 ** 8, 3, 3, border_mode='same'))
    init_model.add(Activation('relu'))
    init_model.add(MaxPooling2D(pool_size=(4, 2)))
    init_model.add(Dropout(0.25))
    init_model.add(Flatten())
    return init_model


### END OF COMMON CNN LAYERS TEMPLATE ###


### MODEL HELPER FUNC ###
def pop_layer(model):
    ## https://github.com/fchollet/keras/issues/2640
    if not model.outputs:
        raise Exception('Sequential model cannot be popped: model is empty.')

    model.layers.pop()
    if not model.layers:
        model.outputs = []
        model.inbound_nodes = []
        model.outbound_nodes = []
    else:
        model.layers[-1].outbound_nodes = []
        model.outputs = [model.layers[-1].output]
    model.built = False


def renew_fc_layers(model, out_dim):
    if len(model.layers) == 18:
        pop_layer(model)
        pop_layer(model)
        pop_layer(model)
        pop_layer(model)
        pop_layer(model)
    model.add(Dense(1536, name='d_cl_1'))
    model.add(Activation('relu', name='a_cl_1'))
    model.add(Dropout(0.25, name='dr_cl_1'))
    model.add(Dense(out_dim, name='d_cl_2'))
    # print(model.summary())
    model.add(Activation('softmax', name='a_cl_2'))
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(),
                  metrics=['accuracy'])


### END OF HELPER FUNC ###
### TRAINING MODEL ###
acc = {}
acc['ag1'] = []
acc['ag2'] = []
acc['bbc'] = []
val_acc = {}
val_acc['ag1'] = []
val_acc['ag2'] = []
val_acc['bbc'] = []
training_model = create_cnn_layers()
for i in range(0, 100):
    if i % 3 == 0:
        # train on ag1
        renew_fc_layers(training_model, num_classes['ag1'])
        print('ag1:', training_model.output_shape)
        training_model.fit(x_train['ag1'], y_train['ag1'], 128, epoch_step,
                           verbose=1, validation_data=(x_test['ag1'], y_test['ag1']))
        score1 = training_model.evaluate(x_train['ag1'], y_train['ag1'], verbose=0)
        score2 = training_model.evaluate(x_test['ag1'], y_test['ag1'], verbose=0)
        print('Train accuracy:', score1[1])
        print('Test accuracy:', score2[1])
        acc['ag1'].append(score1[1])
        val_acc['ag1'].append(score2[1])
    elif i % 3 == 1:
        # train on ag2
        renew_fc_layers(training_model, num_classes['ag2'])
        print('ag2:', training_model.output_shape)
        training_model.fit(x_train['ag2'], y_train['ag2'], 128, epoch_step,
                           verbose=1, validation_data=(x_test['ag2'], y_test['ag2']))
        score1 = training_model.evaluate(x_train['ag2'], y_train['ag2'], verbose=0)
        score2 = training_model.evaluate(x_test['ag2'], y_test['ag2'], verbose=0)
        print('Train accuracy:', score1[1])
        print('Test accuracy:', score2[1])
        acc['ag2'].append(score1[1])
        val_acc['ag2'].append(score2[1])
    else:
        # train on bbc
        renew_fc_layers(training_model, num_classes['bbc'])
        print('bbc:', training_model.output_shape)
        training_model.fit(x_train['bbc'], y_train['bbc'], 128, epoch_step,
                           verbose=1, validation_data=(x_test['bbc'], y_test['bbc']))
        score1 = training_model.evaluate(x_train['bbc'], y_train['bbc'], verbose=0)
        score2 = training_model.evaluate(x_test['bbc'], y_test['bbc'], verbose=0)
        print('Train accuracy:', score1[1])
        print('Test accuracy:', score2[1])
        acc['bbc'].append(score1[1])
        val_acc['bbc'].append(score2[1])
    lines = []
    lines.append('ag1')
    lines.append(','.join([str(a) for a in acc['ag1']]))
    lines.append(','.join([str(a) for a in val_acc['ag1']]))
    lines.append('ag2')
    lines.append(','.join([str(a) for a in acc['ag2']]))
    lines.append(','.join([str(a) for a in val_acc['ag2']]))
    lines.append('bbc')
    lines.append(','.join([str(a) for a in acc['bbc']]))
    lines.append(','.join([str(a) for a in val_acc['bbc']]))
    FileIO.write_lines_to_file('./switch_learning_ag12bbc.log', lines)
    training_model.save('./models/switch_learning_ag12bbc.h5')
