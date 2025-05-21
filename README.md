# Hotel Booking Cancellation Prediction App 🏨🚫

📅 **A Flask-based predictive app** that analyzes hotel booking details to predict cancellation probability. Features optimization improved model accuracy by 8% 📈.


### Try the app! 📱
You can try the it live by clicking [here](https://web-production-42776.up.railway.app/).
> **Note**: The app is deployed on a platform where the deployment includes a limitation of **10 free sessions**. If the app is not working, it's likely because the session limit has been reached.


## Features 🔧
- Predicts hotel booking cancellation likelihood.
- User-friendly web form for inputting key features.
- Provides real-time cancellation prediction & probability.
- Explored and Pruned **Random Forest**, **LightGBM** for **Recall** Optimization
- Randomized Search adn Optuna for **Hyperparameter Tuning**:
- Dynamically Adjusting Threshold to Visualize Performance


## Installation 📝

1. **Clone the repo**:
    ```bash
    git clone https://github.com/amerob/ReservePredict.git
    cd ReservePredict
    ```

2. **Set up virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add your `predict_pipeline.pickle` file** to the root directory.

## Usage 🚀

1. Run the app:
    ```bash
    python app.py
    ```

2. Visit `http://127.0.0.1:5000/` in your browser.

3. **Input features**:
   - Type of Meal Plan 🍽️
   - Room Type Reserved 🛏️
   - Market Segment Type 📊
   - Lead Time 🕰️
   - Average Price per Room 💵
   - Number of Special Requests ✨

4. **Get your result**: The app shows the cancellation prediction and probability!

## File Structure 📂

```bash
hotel-booking-cancellation-prediction/
│
├── app.py                    # Flask app
├── predict_pipeline.pickle   # Trained model
├── templates/
│   └── index.html            # Frontend HTML
├── requirements.txt          # Python dependencies
├── Aptfile                   # System dependencies for deployment
├── Procfile                  # Specifies how to run the app (used by platforms like railway and Heroku)
└── README.md                 # This file



## How It Works ⚙️

1. **Model**: The model predicts cancellation probability based on input features.
2. **Input**: Users input data via the form (meal plan, room type, etc.).
3. **Prediction**: The app processes the input, feeds it into the model, and returns the cancellation likelihood and probability.

## License 📄

MIT License - see the [LICENSE](LICENSE) file for details.

