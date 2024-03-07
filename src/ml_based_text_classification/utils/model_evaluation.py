"""Module that contains common functions used in model evaluation"""


from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def classifier_metrics_report_generator(y_true, y_pred, ndigits=4):
    """Generate a metrics report to a classifier"""
    report = {}
    report["accuracy"] = round(accuracy_score(y_true, y_pred), ndigits)
    report["average_precision"] = round(
        precision_score(y_true, y_pred, average="weighted"), ndigits
    )
    report["average_recall"] = round(
        recall_score(y_true, y_pred, average="weighted"), ndigits
    )
    report["average_f1"] = round(f1_score(y_true, y_pred, average="weighted"), ndigits)
    return report
