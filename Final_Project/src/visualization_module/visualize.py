import matplotlib.pyplot as plt

def Visualize(y_test, y_pred):
    """Hàm biểu diễn trực quan bằng scatter

    Args:
        y_test: Tập các kết quả đúng.
        y_pred: Tập các kết quả dự đoán được.

    Returns:
        matplotlib.pyplot: Biểu đồ scatter.
    """
    
    plt.scatter(y_test, y_pred)
    
    