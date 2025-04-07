# Static Site Generator

A simple Python-based static site generator that transforms Markdown content into a complete, styled HTML website.  
Supports customizable templates, asset copying, and basic site configuration.

---

## Features

- **Markdown to HTML**: Converts `.md` files to `.html` using your choice of template  
- **Customizable Templates**: Use Jinja2 templates for flexible layouts  
- **Asset Management**: Copies CSS, JS, images, and other static assets to the output  
- **Site Configuration**: Central `config.yaml` for site-wide settings (title, author, theme, etc.)  
- **Simple CLI**: Build and serve commands for local preview  

---

## Requirements

- Python 3.7+  

---

## Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/shaharbn/Static-Site-Generator.git
   cd Static-Site-Generator
