
# SSE Demo

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/sse-demo)

A demo repository for showcasing **Server-Sent Events (SSE)** using [Vue.js](https://vuejs.org/) on the frontend and [Litestar](https://litestar.dev/) on the backend.

> **Note:** This demo uses SSE to automatically update the UI whenever changes occur in a monitored file.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Frontend Setup](#frontend-setup)
  - [Backend Setup](#backend-setup)
    - [GNU/Linux / macOS](#gnulinux--macos)
    - [Windows](#windows)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Real-Time Updates:** Uses SSE to push file updates directly to the UI.
- **Modern Frontend:** Built with Vue.js for a reactive and dynamic user experience.
- **Lightweight Backend:** Powered by Litestar to handle asynchronous event streaming.
- **Cross-Platform Support:** Instructions provided for both GNU/Linux/macOS and Windows environments.

---

## Prerequisites

Before getting started, ensure you have the following installed on your system:

- **Node.js** (Latest LTS version recommended) – for the frontend.
- **Python 3.8+** – for the backend.
- **pip** – Python package installer.
- **Git** – to clone the repository.

---

## Installation

### Clone the Repository

Clone the repo to your local machine:

```bash
git clone https://github.com/yourusername/sse-demo.git
cd sse-demo
```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd sse-demo-fe
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

   The frontend should now be running on [http://localhost:3000](http://localhost:3000) (or another port as specified in your configuration).

### Backend Setup

The backend is built with Python and uses Litestar to serve SSE. Follow the instructions below based on your operating system.

#### GNU/Linux / macOS

1. Navigate to the backend directory:

   ```bash
   cd sse-demo-be
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Litestar server:

   ```bash
   litestar run
   ```

#### Windows

1. Open Command Prompt or PowerShell and navigate to the backend directory:

   ```bash
   cd sse-demo-be
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **Command Prompt:**
     ```bash
     venv\Scripts\activate
     ```
   - **PowerShell:**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Litestar server:

   ```bash
   litestar run
   ```

---

## Usage

1. **Run both servers:**  
   - Make sure the frontend and backend are both running.
   
2. **Update the File:**  
   Append new text to `file.txt` to trigger an update:

   ```bash
   echo "more text" >> file.txt
   ```

   Once updated, the changes should automatically be reflected on the UI via SSE.

3. **Explore and Modify:**  
   - Feel free to modify the frontend components or the backend logic to experiment with real-time updates.

---

## Troubleshooting

- **Frontend Not Loading:**  
  Ensure you have the latest version of Node.js installed and that all dependencies are correctly installed using `npm install`.

- **Backend Errors:**  
  Verify your Python version and that you have activated your virtual environment before installing dependencies and running the server.

- **SSE Connection Issues:**  
  Check that there are no firewall or network restrictions blocking SSE connections, and inspect browser console logs for any errors.

For further assistance, please open an issue in this repository.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements. For major changes, open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding!
```

