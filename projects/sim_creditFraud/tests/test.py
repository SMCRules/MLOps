from src.train import train_model

def test_training_pipeline_runs():
    model = train_model()
    assert model is not None
    assert "model" in model
