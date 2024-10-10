import tkinter as tk
from tkinter import filedialog, scrolledtext
import boto3
import json
import os

# Initialize AWS clients
s3_client = boto3.client('s3')
rekognition_client = boto3.client('rekognition')

# Specify your bucket name
bucket_name = 'futurecloudimages'  # Replace with your actual bucket name

def upload_and_detect_labels():
    # Open file dialog to select images
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    
    if not file_paths:
        print("No files selected.")
        return

    # Clear the results text area before displaying new results
    result_text.delete(1.0, tk.END)

    for image_file in file_paths:
        # Extract the file name for S3 object key
        s3_image_key = os.path.basename(image_file)
        
        # Upload image to S3
        try:
            s3_client.upload_file(image_file, bucket_name, s3_image_key)
            result_text.insert(tk.END, f"Image '{image_file}' uploaded successfully to '{bucket_name}' as '{s3_image_key}'\n")
        except Exception as e:
            result_text.insert(tk.END, f"Error uploading image '{image_file}' to '{bucket_name}': {e}\n")
            continue

        # Detect labels using Rekognition
        try:
            response = rekognition_client.detect_labels(
                Image={'S3Object': {'Bucket': bucket_name, 'Name': s3_image_key}},
                MaxLabels=5,        # Adjust the number of labels as needed
                MinConfidence=90     # Minimum confidence level for labels
            )

            # Display the detected labels in the result text area
            result_text.insert(tk.END, f"\nDetected labels for '{s3_image_key}':\n")
            for label in response['Labels']:
                result_text.insert(tk.END, f"{label['Name']} - Confidence: {label['Confidence']:.2f}%\n")
            
            # Optionally save results to a JSON file
            with open(f"{s3_image_key}_labels.json", "w") as f:
                json.dump(response, f, indent=4)
                result_text.insert(tk.END, f"Results saved to '{s3_image_key}_labels.json'\n")
        except Exception as e:
            result_text.insert(tk.END, f"Error detecting labels for '{s3_image_key}': {e}\n")

# Set up the main GUI window
root = tk.Tk()
root.title("Image Label Detection with AWS Rekognition")
root.geometry("600x400")

# Create a text area to display the results
result_text = scrolledtext.ScrolledText(root, width=70, height=20)
result_text.pack(pady=10)

# Create a button to select images
select_button = tk.Button(root, text="Select Images", command=upload_and_detect_labels)
select_button.pack(pady=10)

# Run the GUI
root.mainloop()
