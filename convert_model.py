from tensorflow.keras.models import load_model

# Load the old model
model = load_model("next_word_lstm.h5")

# Save it in the updated format
model.save("next_word_lstm_converted.h5")
