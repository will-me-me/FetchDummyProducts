# FetchDummyProducts

A FastAPI application that fetches and serves product data from the DummyJSON API. This project demonstrates how to integrate external APIs with FastAPI to create a robust product management system.

## Features

- Fetch products from DummyJSON API
- RESTful API endpoints for product operations
- Async/await support for better performance
- Data validation with Pydantic models
- Interactive API documentation with Swagger UI
- Error handling and response formatting

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd FetchDummyProducts
```

### 2. Create Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

1. Make sure your virtual environment is activated
2. Start the FastAPI development server:

```bash
fastapi dev main.py
```

The application will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Configuration

The application uses the DummyJSON API (`https://dummyjson.com/products`) as the data source. You can modify the base URL and other settings in the configuration file or environment variables.

## Requirements

The main dependencies include:

- `fastapi` - Web framework for building APIs
- `uvicorn` - ASGI server for running the application
- `httpx` - HTTP client for making requests to external APIs
- `pydantic` - Data validation and settings management

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
isort .
```

### Linting

```bash
flake8 .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [DummyJSON](https://dummyjson.com/) for providing the test API
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 8000 is busy, use a different port:

   ```bash
   fastapi dev main.py --port 8001
   ```

2. **Virtual environment issues**: Make sure you've activated your virtual environment before installing dependencies

3. **API timeout**: If the DummyJSON API is slow, you may need to increase timeout settings in the HTTP client configuration

## Contact

For questions or support, please open an issue on the repository or contact the maintainers.

---

**Happy coding! 🚀**
