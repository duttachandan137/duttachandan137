from flask import Flask, render_template, request, redirect, url_for, send_file # type: ignore
import pandas as pd # type: ignore

app = Flask(__name__)

# Landing page - Upload form
@app.route('/')
def index():
    return render_template('index.html')

# Upload CSV files and process allocation
@app.route('/upload', methods=['POST'])
def upload():
    # Check if files are uploaded
    if 'group_file' not in request.files or 'hostel_file' not in request.files:
        return redirect(url_for('index'))

    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']

    # Check if files are CSV
    if group_file.filename == '' or hostel_file.filename == '':
        return redirect(url_for('index'))

    if group_file and hostel_file:
        # Read CSV files
        groups_df = pd.read_csv(group_file)
        hostels_df = pd.read_csv(hostel_file)

        # Process allocation (implement allocation logic here)

        # Dummy output for demonstration
        allocation_data = [
            {"Group ID": 101, "Hostel Name": "Boys Hostel A", "Room Number": 101, "Members Allocated": 3},
            {"Group ID": 102, "Hostel Name": "Girls Hostel B", "Room Number": 202, "Members Allocated": 4},
            {"Group ID": 103, "Hostel Name": "Boys Hostel A", "Room Number": 102, "Members Allocated": 2},
            {"Group ID": 104, "Hostel Name": "Girls Hostel B", "Room Number": 202, "Members Allocated": 5}
        ]

        # Create a new CSV file for allocation results
        allocation_filename = 'allocation.csv'
        pd.DataFrame(allocation_data).to_csv(allocation_filename, index=False)

        # Provide the download link to the user
        return render_template('result.html', allocation_data=allocation_data, filename=allocation_filename)

    return redirect(url_for('index'))

# Download allocated rooms CSV file
@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
