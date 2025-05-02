import os
import sys
import tensorflow as tf
from tensorflow.keras.models import load_model

def find_model_file():
    """Search for the model file in various locations"""
    model_filename = "cnn8grps_rad1_model.h5"
    possible_paths = [
        os.path.join(os.getcwd(), f"sign_language/models/Sign-Language-To-Text-and-Speech-Conversion-master/{model_filename}"),
        os.path.join(os.getcwd(), f"lg/sign_language/models/Sign-Language-To-Text-and-Speech-Conversion-master/{model_filename}"),
        os.path.abspath(f"sign_language/models/Sign-Language-To-Text-and-Speech-Conversion-master/{model_filename}"),
        os.path.abspath(f"lg/sign_language/models/Sign-Language-To-Text-and-Speech-Conversion-master/{model_filename}")
    ]
    
    print(f"Current working directory: {os.getcwd()}")
    
    for path in possible_paths:
        print(f"Checking path: {path}")
        if os.path.exists(path):
            print(f"Found model at: {path}")
            return path
    
    # If not found in standard locations, search the directory tree
    print("Searching for model file in directory tree...")
    for root, dirs, files in os.walk(os.getcwd()):
        if model_filename in files:
            path = os.path.join(root, model_filename)
            print(f"Found model at: {path}")
            return path
    
    return None

def test_load_model():
    """Test loading the model"""
    print(f"Python version: {sys.version}")
    print(f"TensorFlow version: {tf.__version__}")
    
    model_path = find_model_file()
    
    if model_path is None:
        print("ERROR: Model file not found!")
        return
    
    try:
        print(f"Loading model from {model_path}...")
        model = load_model(model_path)
        print("Model loaded successfully!")
        print(f"Model summary: {model.summary()}")
    except Exception as e:
        print(f"Error loading model: {e}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    test_load_model() 