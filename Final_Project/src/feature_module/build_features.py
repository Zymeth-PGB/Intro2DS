from sklearn.preprocessing import LabelEncoder

def convert(value):
    label_encoder = LabelEncoder()
    return label_encoder.fit_transform(value)