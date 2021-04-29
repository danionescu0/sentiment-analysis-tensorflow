import tflearn
import pickle


def load_model(lang: str):
    net = tflearn.input_data([None, 150])
    net = tflearn.embedding(net, input_dim=10000, output_dim=128)
    net = tflearn.lstm(net, 128, dropout=0.8)
    net = tflearn.fully_connected(net, 2, activation='softmax')
    net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                             loss='categorical_crossentropy')
    model = tflearn.DNN(net, tensorboard_verbose=0)
    model.load(f"checkpoints/{lang}/{lang}tf.tfl")
    return model


def load_dictionary(lang: str):
    f = open(f"./dictionaries/{lang}dictionary.pickle", "rb")
    dictionary = pickle.load(f)
    f.close()
    return dictionary