from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt


def rf_feat_importance(model, X, plot=False):
    '''
    Creates a dataframe of feature importances from the random forest model ( works also for catboost models)
    Parameters:
    X : the Dataframe used for training ( X_train )
    model : The trained Model
    plot : Whether to plot the feature importance ( default : False)
    Returns:
    pd.DataFrame:Feature Importance DataFrame
    '''
    fi = pd.DataFrame({'cols': X.columns, 'imp': model.feature_importances_}
                      ).sort_values('imp', ascending=False)
    if plot:
        fi[:20].plot.barh(x="cols", y="imp", figsize=(10, 10))
        plt.show()
    return fi
