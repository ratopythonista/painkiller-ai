import pickle

from painkiller.repository.patient import PatientRepository

from sklearn import svm
from sklearn.model_selection import cross_val_score

from jonas.services.filesystem import FileSystem

from loguru import logger

class ModelBussines:
    def train():
        data_matrix, feature_row = list(), list()
        for patient in PatientRepository.get_all():
            data_matrix_row = list()
            data_matrix_row.append(patient.patient_id)
            feature_row.append(1 if patient.condition_id == 1 else 0)
            for measurement in PatientRepository.get_measurements(patient.patient_id):
                data_matrix_row.append(measurement.value)
            data_matrix.append(data_matrix_row)

        model = svm.SVC()
        recall = cross_val_score(model, data_matrix, feature_row, cv=5, scoring='recall_macro')
        model.fit(data_matrix, feature_row)
        binary_model = pickle.dumps(model)
        return FileSystem().insert(binary_model, {"recall": recall})

    def get_metrics(model_id: str):
        return FileSystem().get_recall(model_id)

    def predict(model_id: str, predict_data: dict):
        model_binary = FileSystem().get_model(model_id)
        model: svm.SVC = pickle.loads(model_binary)
        predict_result = model.predict([list(predict_data.values())])
        return predict_result.tolist()