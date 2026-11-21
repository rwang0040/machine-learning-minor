"""Provided CPU teaching trainer. Students supply output_delta and update callbacks."""

import numpy as np


def initialize():
    rng = np.random.default_rng(20261003)
    return {
        "W1": rng.normal(0, 0.2, (2, 2)),
        "b1": np.zeros(2),
        "W2": rng.normal(0, 0.2, (2, 1)),
        "b2": np.zeros(1),
    }


def forward(X, params):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[1] != 2 or not len(X) or not np.isfinite(X).all():
        raise ValueError("X must be finite nonempty (n,2)")
    for key, shape in {"W1": (2, 2), "b1": (2,), "W2": (2, 1), "b2": (1,)}.items():
        if params[key].shape != shape or not np.isfinite(params[key]).all():
            raise ValueError(key)
    z1 = X @ params["W1"] + params["b1"]
    h = np.maximum(0.0, z1)
    score = h @ params["W2"] + params["b2"]
    p = np.exp(-np.logaddexp(0.0, -score))
    return {"z1": z1, "h": h, "score": score, "probability": p}


def loss(score, y):
    if score.shape != y.shape or score.ndim != 2 or score.shape[1] != 1 or not len(y):
        raise ValueError("score and y must share nonempty (n,1) shape")
    if not np.isfinite(score).all() or not np.isin(y, [0, 1]).all():
        raise ValueError("invalid score/target")
    return float(np.mean(np.logaddexp(0.0, score) - y * score))


def gradients(X, y, params, output_delta):
    cache = forward(X, params)
    loss(cache["score"], y)
    ds = output_delta(cache["probability"], y)
    if ds.shape != y.shape or not np.isfinite(ds).all():
        raise ValueError("invalid output gradient")
    # All derivatives below use the same, not-yet-updated parameter snapshot.
    dw2 = cache["h"].T @ ds
    db2 = ds.sum(axis=0)
    dh = ds @ params["W2"].T
    dz = dh * (cache["z1"] > 0)  # ReLU'(0)=0 convention
    return {"W1": X.T @ dz, "b1": dz.sum(axis=0), "W2": dw2, "b2": db2}


def train(
    X, y, X_valid, y_valid, initial, learning_rate, output_delta, update, steps=200
):
    if not np.isfinite(learning_rate) or learning_rate < 0:
        raise ValueError("learning_rate must be nonnegative")
    params = {key: value.copy() for key, value in initial.items()}
    history = []
    for epoch in range(steps + 1):
        training = forward(X, params)
        validation = forward(X_valid, params)
        history.append(
            {
                "epoch": epoch,
                "train_loss": loss(training["score"], y),
                "validation_loss": loss(validation["score"], y_valid),
            }
        )
        if epoch == steps:
            break
        grad = gradients(X, y, params, output_delta)
        params = update(params, grad, learning_rate)
    return params, history
