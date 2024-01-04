import pickle

def Make_file_pkl(model):
    pickle.dump(model, open('../models/model.pkl', 'wb'))