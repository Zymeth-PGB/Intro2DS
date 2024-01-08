from src.models_module.train_model import *
from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score

def Linear_Regression(X_test, X_train, y_train):
    """Hàm dự đoán theo mô hình Linear Regression

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.
        X_test: Tập các thuộc tính dùng để test mô hình.

    Returns:
        List: Tập dự đoán của mô hình.
    """
    
    model = Linear_Regression_train(X_train, y_train)
    predict = model.predict(X_test)
    
    return predict

def Random_Forest(X_test, X_train, y_train):
    """Hàm dự đoán theo mô hình Random Forest

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.
        X_test: Tập các thuộc tính dùng để test mô hình.

    Returns:
        List: Tập dự đoán của mô hình.
    """
    
    model = Random_Forest_train(X_train, y_train)
    predict = model.predict(X_test)
    
    return predict

def Decision_Tree(X_test, X_train, y_train):
    """Hàm dự đoán theo mô hình Decision Tree

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.
        X_test: Tập các thuộc tính dùng để test mô hình.

    Returns:
        List: Tập dự đoán của mô hình.
    """
    
    model = Decision_Tree_train(X_train, y_train)
    predict = model.predict(X_test)
    
    return predict

def Gradient_Boosting(X_test, X_train, y_train):
    """Hàm dự đoán theo mô hình Gradient Boosting

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.
        X_test: Tập các thuộc tính dùng để test mô hình.

    Returns:
        List: Tập dự đoán của mô hình.
    """
    
    model = Gradient_Boosting_train(X_train, y_train)
    predict = model.predict(X_test)
    
    return predict

def XGBoost(X_test, X_train, y_train):
    """Hàm dự đoán theo mô hình XGBoost

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.
        X_test: Tập các thuộc tính dùng để test mô hình.

    Returns:
        List: Tập dự đoán của mô hình.
    """
    
    model = XGBoost_train(X_train, y_train)
    predict = model.predict(X_test)
    
    return predict

def Evaluation(y_test, y_pred):
    """Hàm trả về kết quả đánh giá mô hình

    Args:
        y_test: Tập các kết quả đúng.
        y_pred: Tập các kết quả dự đoán được.

    Returns:
        float: Các giá trị đánh giá mô hình.
    """
    
    rmse = mean_squared_error(y_test, y_pred, squared = False)
    mae = mean_absolute_error(y_test, y_pred)
    evs = explained_variance_score(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return rmse, mae, evs, r2