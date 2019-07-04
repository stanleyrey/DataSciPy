def _cross_entropy(df, coefs):
    return -sum(
        -z*(1-y) - np.log(1+np.exp(-z)) 
        for z, y 
        in zip(logodds(df, coefs), df['Survived'].values)
    ) / df.shape[0]
        
def cross_entropy(df, coefs):
    y = df["Survived"].values
    z = logodds(df, coefs)
    logliks = -z * (1 - y) - np.log(1 + np.exp(-z))
    return -logliks.mean()

def gradient_descent(df, coefs, η=0.01):
    X = df[['Sex', 'Age', 'Pclass']].values
    Y = df['Survived'].values
    nsamples = Y.shape[0]
    
    Yhat = expit(logodds(df, coefs))
    δ = Yhat - Y
    grad = X.T @ δ / nsamples
    assert grad.shape == grad.shape
    return grad - η * grad