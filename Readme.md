# 🚀 URL Shortener CLI Tool 🌐

## ⚙️ Setup and Installation

### Prerequisites

Ensure you have the following installed:
- 🐍 Python 3.7+
- 📦 `requests` (installed automatically)

### Installation Steps

1. Clone the repository:
   - Open your terminal or command prompt.
   - Run: `git clone https://github.com/yadavkapil23/url-shortener-cli.git`
   - Navigate to the project directory: `cd url-shortener-cli`

2. Set up a virtual environment (optional):
   - Create a virtual environment: `python -m venv venv`
   - Activate it:
     - On Linux/Mac: `source venv/bin/activate`
     - On Windows: `venv\Scripts\activate`

3. Install the CLI tool:
   - Run: `pip install urlzap`

4. Run the CLI:
   - Type `zap` in the terminal to start using the tool.

   Now, your CLI tool is ready to use! 🎉

## 🛠️ Features

- **URL Shortening**: Create concise URLs with detailed output.
- **Validation**: Verify URLs without modifying them.
- **History**: Track and review past shortenings.
- **Batch Mode**: Process multiple URLs from a file.
- **User-Friendly**: Includes a comprehensive help system.

## 🛡️ Security

- 🔐 No sensitive data storage.
- 🔒 Operates over HTTPS for secure requests.

## 🚀 Usage

### Basic Commands
| Command       | Description                              |
|---------------|------------------------------------------|
| `zap shorten <url>` | Shorten a URL with detailed output |
| `zap validate <url>` | Validate a URL                   |
| `zap history`      | Display history of shortened URLs       |
| `zap batch <file>` | Shorten URLs from a text file           |
| `zap info`         | Display tool information                |
| `zap version`      | Show tool version                       |

Run `zap --help` for detailed examples and options.

## 🧠 How It Works

The `shorten` and `batch` commands send GET requests to the TinyURL API:

The API returns the shortened URL in plain text. History is stored in `url_history.json`, and batch results are saved to a timestamped text file.

## 🚀 Deployment

No additional deployment is required; the tool runs locally via the `zap` command.

## 🧠 Future Enhancements

- 🔄 **Custom Domains**: Support for custom short URL domains.
- 🤖 **Advanced Validation**: Enhance URL validation with regex patterns.
- 📊 **Analytics**: Add usage statistics for shortened URLs.

## 🤝 Contributing

Want to contribute? Fork this repository, submit a pull request, or open an issue. All contributions are welcome! 🛠️

## 📄 License

This project is licensed under the MIT License.

---

🎉 **Thank you for checking out the URL Shortener CLI Tool!** If you have questions or suggestions, feel free to reach out or open an issue. Let's build something amazing!
