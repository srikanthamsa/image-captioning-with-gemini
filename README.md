# Image Captioning and Tagging with Google Gemini
![image](https://github.com/user-attachments/assets/04d98678-9a8d-4bb0-bad6-a6b104e54a99)

This project is a web application that uses the Google Gemini Cloud Vision API to analyze images and generate descriptive tags based on the content of the uploaded images. Additionally, the application is designed to generate captions and describe what's happening in the photos; however, this feature is currently a work in progress (WIP).

## Live Demo

You can try out the live version of the application [here](https://image-captioning-with-gemini.onrender.com/).

## Features

- **Tag Generation**: Upload an image, and the application will generate relevant tags that describe the contents of the image.
- **Caption Generation (WIP)**: The application is being developed to generate captions and detailed descriptions of what's happening in the image.
- **Beautiful UI**: The user interface is elegantly crafted using just CSS, ensuring a smooth and visually appealing experience.

## Technologies Used

- **Python**: The core programming language used for backend development.
- **Flask**: A lightweight WSGI web application framework used to build the web server.
- **Google Gemini Cloud Vision API**: A powerful image analysis API from Google, used to generate tags and (soon) captions for the images.
- **Render**: The platform where the application is hosted.
- **CSS**: Used to create a beautiful and responsive user interface.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/image-captioning-with-gemini.git

2. **Navigate to the project directory**:
   ```bash
   cd image-captioning-with-gemini
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Set up environment variables**:
   - Create a `.env` file in the project root directory with the following content:
     ```bash
     FLASK_APP=app.py
     FLASK_ENV=development
     GOOGLE_APPLICATION_CREDENTIALS=path_to_your_google_credentials.json
     ```
   - Replace `path_to_your_google_credentials.json` with the actual path to your Google Cloud credentials JSON file.

7. **Run the application**:
   ```bash
   flask run
   ```

8. **Access the application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Navigate to the homepage of the application.
2. Upload an image using the provided upload form.
3. The application will process the image and display a list of tags that describe the content of the image.
4. (Feature in Works) The application will also generate a caption describing what's happening in the image.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or feedback, feel free to reach out:

- **GitHub**: [srikanthamsa](https://github.com/srikanthamsa)
- **Email**: srikanthamsa@gmail.com

---

Thank you for checking out this project! 😊
