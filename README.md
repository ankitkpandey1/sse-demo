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
