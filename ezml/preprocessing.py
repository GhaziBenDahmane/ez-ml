from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt


class MultiColumnLabelEncoder:
    '''
    A Multi Column Label Encoder to use for Pandas dataframe based on Sklearn LabelEncoder
    example usage : 
    me = MultiColumnLabelEncoder()
    X_train_transformed = me.fit_transform(X_train)
    me.transform(X_test)
    me.inverse_transform(X_train_transformed)
    '''

    def __init__(self):
        self.transformers = {}

    def fit_transform(self, dframe):
        '''
        Fits and transforms the dataframe using LabelEncoder
        Parameters:
        dframe : DataFrame to transform

        Returns:
        pd.DataFrame:Encoded Dataframe

        '''
        data = {}
        for column in dframe.columns:
            self.transformers[column] = LabelEncoder()
            data[column] = self.transformers[column].fit_transform(
                dframe[column])
        return pd.DataFrame(data)

    def transform(self, dframe):
        '''
        Transforms the dataframe using LabelEncoder
        Parameters:
        dframe : DataFrame to transform

        Returns:
        pd.DataFrame:Encoded Dataframe

        '''
        data = {}
        for column in dframe.columns:
            data[column] = self.transformers[column].transform(dframe[column])
        return pd.DataFrame(data)

    def inverse_transform(self, dframe):
        '''
        Returns the original Data Frame from the encoded one .
        Parameters:
        dframe : Transformed DataFrame

        Returns:
        pd.DataFrame:Original Dataframe

        '''
        data = {}
        for column in dframe.columns:
            data[column] = self.transformers[column].inverse_transform(
                dframe[column])
        return pd.DataFrame(data)


def missing_values(df, plot=False):
    '''
    Creates a Dataframe with the percentage of missing values for each column
    Parameters:
    df : Input DataFrame
    plot : Whether to plot the missing values percentages ( default : False)

    Returns:
    pd.DataFrame: Missing Values DataFrame
    '''
    percent_missing = df.isnull().sum() * 100 / len(df)
    missing_value_df = pd.DataFrame({'percent_missing': percent_missing})
    if plot:
        missing_value_df['percent_missing'][:20].plot.barh()
        plt.show()
    return missing_value_df
