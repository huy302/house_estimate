import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_absolute_error

plt.style.use('ggplot')

'''
Get the ML pipeline, here we use XGBRegressor, one of the best learners for non-linear regression
'''
def get_pipeline():
    return XGBRegressor()

'''
Feed in train/test sets, run regression and plot the result
Here we use 2 evaluation metrics: R2 and MAE
'''
def run_prediction(X_train, X_test, y_train, y_test):
    predictor = get_pipeline()
    predictor.fit(X_train, y_train)
    y_pred = predictor.predict(X_test)
    print(f'R2: {r2_score(y_test, y_pred)}')
    print(f'MAE: {mean_absolute_error(y_test, y_pred)}')

    plt.figure(figsize=(8,8))
    ident = [0.0, 2500000]
    plt.plot(ident,ident,'--',linewidth=3, color='#4C72AF')
    plt.scatter(y_test, y_pred,s=60)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim(0, 2500000)
    plt.xlim(0, 2500000)
    plt.ylabel('Predicted house price', fontsize=12)
    plt.xlabel('Actual house price', fontsize=12)
    plt.show()