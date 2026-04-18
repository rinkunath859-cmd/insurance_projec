import pickle
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train):
    model = RandomForestRegressor(
        n_estimators=10,
        max_depth=5,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    return model


def save_model(model, scaler, columns):
    pickle.dump(model, open("../deployment/model.pkl", "wb"))
    pickle.dump(scaler, open("../deployment/scaler.pkl", "wb"))
    pickle.dump(columns, open("../deployment/columns.pkl", "wb"))