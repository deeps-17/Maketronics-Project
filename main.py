from flask import Flask, render_template, request
import pandas as pd
print("file is running ")
app = Flask(__name__)

# Load CSV once at startup
df = pd.read_csv("mobiles_with_images.csv")

@app.route('/')
def index():
    # Get filter inputs
    keyword = request.args.get('keyword', '').lower()
    min_price = int(request.args.get('min_price', 0))
    max_price = int(request.args.get('max_price', 100000))
    min_camera = int(request.args.get('min_camera', 0))
    min_battery = int(request.args.get('min_battery', 0))

    # Apply filters
    filtered = df[
        (df['Price (₹)'] >= min_price) &
        (df['Price (₹)'] <= max_price) &
        (df['Camera (MP)'] >= min_camera) &
        (df['Battery (mAh)'] >= min_battery)
    ]

    if keyword:
        filtered = filtered[filtered['Description'].str.lower().str.contains(keyword)]

    return render_template("index.html", phones=filtered.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
 
