from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
import xgboost as xg

def Linear_Regression_train(X_train, y_train):
    """Hàm train theo mô hình Linear Regression

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.

    Returns:
        sklearn.linear_model: Mô hình đã huấn luyện.
    """
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

def Random_Forest_train(X_train, y_train):
    """Hàm train theo mô hình Random Forest

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.

    Returns:
        sklearn.ensemble: Mô hình đã huấn luyện.
    """
    
    model = RandomForestRegressor(max_depth = 10)
    model.fit(X_train, y_train)
    
    return model

def Decision_Tree_train(X_train, y_train):
    """Hàm train theo mô hình Decision Tree

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.

    Returns:
        sklearn.tree: Mô hình đã huấn luyện.
    """

    model = DecisionTreeRegressor(max_depth = 6)
    model.fit(X_train, y_train)
    
    return model

def Gradient_Boosting_train(X_train, y_train):
    """Hàm train theo mô hình Gradient Boosting

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.

    Returns:
        sklearn.ensemble: Mô hình đã huấn luyện.
    """
    
    model = GradientBoostingRegressor(random_state = 0)
    model.fit(X_train, y_train)
    
    return model

def XGBoost_train(X_train, y_train):
    """Hàm train theo mô hình XGBoost

    Args:
        X_train: Tập các thuộc tính cần huấn luyện.
        y_train: Tập các kết quả.

    Returns:
        xgboost: Mô hình đã huấn luyện.
    """
    
    model = xg.XGBRegressor(learning_rate = 0.1)
    model.fit(X_train, y_train)
    
    return model