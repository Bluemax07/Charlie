# Charlie: Your Virtual Assistant

Charlie is a versatile and intelligent virtual assistant designed to enhance productivity and streamline daily tasks. With capabilities ranging from voice recognition to custom command execution, Charlie offers a user-friendly and interactive experience.

## Features

- **Voice Commands:** Activate and control Charlie using voice commands. The assistant listens for specific phrases and performs the corresponding actions.
- **Command Execution:** Run predefined commands to open applications, play videos, send messages, and make calls.
- **Customizable Responses:** Easily modify and extend Charlie's responses and actions to meet your specific needs.
- **Chat Interface:** Interact with Charlie via a chatbox in a web interface, enabling straightforward message exchanges.
- **Integration with Hugging Face:** Leverage Hugging Face's models for advanced conversational abilities.
- **Hotword Detection:** Trigger interactions with Charlie by saying a custom hotword, such as "Charlie."

## Installation

To set up Charlie on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/charlie.git

## Configuration

Customize Charlie's functionality by modifying the following files:

### Voice Recognition

- **File:** `back/feature.py`
- **Description:** Configure the settings for handling voice commands and integrating with external APIs.
- **Steps:**
  1. Open `back/feature.py` in your preferred code editor.
  2. Modify the voice recognition settings and API integration as needed.

### Web Interface

- **Directory:** `front`
- **Description:** Update the HTML and CSS files to adjust the appearance of the chat interface.
- **Files to Modify:**
  - `index.html`: The main HTML file for the chat interface.
  - `styles.css`: The CSS file to style the chat interface.
- **Steps:**
  1. Navigate to the `front` directory.
  2. Open `index.html` and `styles.css` to make visual changes.

### Hotword Detection

- **File:** `back/feature.py`
- **Description:** Configure hotword detection with Picovoice.
- **Steps:**
  1. Open `back/feature.py` in your preferred code editor.
  2. Update the `model_path` variable with the path to your `.ppn` file.
  3. Update the `access_key` variable with your Picovoice access key.


## Usage

Interact with Charlie using the following methods:

### Voice Activation

- **How to Activate:**
  - Click the microphone icon or use the keyboard shortcut (Ctrl+J) to activate Charlie.
  - Issue voice commands to perform various actions.

### Chat Interaction

- **How to Use:**
  - Type messages into the chatbox.
  - Press Enter or click the Send button to communicate with Charlie.

### Custom Commands

- **How to Customize:**
  - Add or modify commands in `back/feature.py` to extend Charlie's capabilities.
  - Examples of custom commands include opening applications, playing media, and sending messages.

## Contributing

Contributions are welcome! To contribute to the project:

1. **Fork the Repository:**
   - Create a personal copy of the repository by forking it on GitHub.

2. **Create a Branch:**
   - Develop new features or fix bugs in a separate branch.

3. **Submit a Pull Request:**
   - Share your changes by submitting a pull request for review.

Please ensure your contributions adhere to the project's coding standards and guidelines.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

## Acknowledgments

- **Hugging Face:** For providing advanced NLP models used in Charlie.
- **Picovoice:** For the hotword detection technology that enables voice activation.
- **pyttsx3:** For the text-to-speech functionality used to communicate responses.
- **SpeechRecognition:** For the speech-to-text capabilities that allow Charlie to understand voice commands.

## Contact

For any questions or support:

- **Open an Issue:** [Open an issue on GitHub](https://github.com/your-username/charlie/issues).
- **Contact the Maintainers:** Reach out to the project maintainers via GitHub or your preferred communication channel.

