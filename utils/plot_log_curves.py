def display_precision_recall_curve(log_model):
    test_prob=log_model.predict_proba(scaled_X_test)[::,1] #probability prediction whether it is 0 or 1
    precision, recall, _= precision_recall_curve(y_test,  test_prob)

    plt.plot(precision,recall)
    plt.ylabel('Precision')
    plt.xlabel('Recall')
    plt.show()

def display_roc_curve(log_model):
    test_prob=log_model.predict_proba(scaled_X_test)[::,1] #probability prediction whether it is 0 or 1
    fpr, tpr, _ = roc_curve(y_test,  test_prob)

    plt.plot(fpr,tpr)
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
