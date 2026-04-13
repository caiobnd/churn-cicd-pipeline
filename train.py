from sklearn.linear_model   import LogisticRegression
from pathlib                import Path
from joblib                 import dump
from model                  import train_logistic_regression
import cleaning

path_data=Path("data/Test_df.csv")
path_model=Path("model/logisticregression.pkl")

df          = cleaning.load_data(path_data)
df_clean    = cleaning.clean_data(df)
df_enconded = cleaning.encoding(df_clean)
X_train, X_test, y_train, y_test = cleaning.split_data(df_enconded)

model = train_logistic_regression(X_train,y_train)

dump(model,path_model)


        
    
