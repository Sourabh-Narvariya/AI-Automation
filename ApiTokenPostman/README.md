# API Development with Flask and Postman

This module covers building RESTful APIs with Flask and testing them using Postman.

## 📚 What I Learned

- Building RESTful APIs with Flask
- HTTP methods: GET, POST, PUT, DELETE
- JSON request/response handling
- API testing with Postman
- Token-based authentication concepts
- CRUD operations via APIs

## 🎯 Learning Resources

- Flask RESTful API Documentation
- Postman Official Guides
- HTTP Methods Best Practices

## 📝 Tasks Completed

### Task 2.2: POST Request with JSON Data
**File:** `Task2.2.py`

Created a Flask API that:
- Accepts POST requests at `/api/echo` endpoint
- Receives JSON payload
- Validates JSON data
- Echoes back the received data with a personalized message
- Handles error cases (missing JSON)

**Testing with Postman:**
```json
POST http://127.0.0.1:5000/api/echo
Body: {"name": "Sourabh"}
Response: {"message": "Hello, Sourabh!", "received": {"name": "Sourabh"}}
```

### Task 2.3: Full CRUD API (GET, POST, PUT, DELETE)
**File:** `Task2.3.py`

Built a complete RESTful API with in-memory data store:

**Endpoints:**
- `GET /api/items` - Get all items
- `GET /api/items/<item_id>` - Get specific item
- `POST /api/items` - Create new item
- `PUT /api/items/<item_id>` - Update existing item
- `DELETE /api/items/<item_id>` - Delete item

**Features:**
- CRUD operations
- Error handling (404 for not found)
- Proper HTTP status codes (200, 201, 404)
- JSON request/response format

**Postman Test Examples:**
```
POST /api/items
Body: {"name": "Laptop", "price": 50000}

GET /api/items

PUT /api/items/1
Body: {"name": "Gaming Laptop", "price": 75000}

DELETE /api/items/1
```

### Task 2.4: (Empty File - To Be Implemented)
**File:** `Task2.4.py`

Status: Placeholder file

### Task 2.6: Square Number API
**File:** `Task2.6.py`

Created a Flask API for mathematical operations:
- Accepts POST requests at `/api/square` endpoint
- Takes a number as JSON input
- Returns the square of the number
- Validates input and handles errors
- Returns proper error messages for invalid data

**Testing with Postman:**
```json
POST http://127.0.0.1:5000/api/square
Body: {"number": 5}
Response: {"number": 5.0, "squared": 25.0}
```

**Error Handling:**
- Missing number field: 400 error
- Invalid number format: 400 error with message

## 🚀 How to Run

### Prerequisites
```bash
pip install flask
```

### Running the APIs

**Task 2.2 - Echo API:**
```bash
python Task2.2.py
```
Visit: `http://127.0.0.1:5000/api/echo` (POST)

**Task 2.3 - CRUD API:**
```bash
python Task2.3.py
```
Visit: `http://127.0.0.1:5000/api/items` (GET/POST/PUT/DELETE)

**Task 2.6 - Square API:**
```bash
python Task2.6.py
```
Visit: `http://127.0.0.1:5000/api/square` (POST)

## 🧪 Testing with Postman

### Setup:
1. Install Postman from [postman.com](https://www.postman.com/)
2. Create a new collection "Flask APIs"
3. Add requests for each endpoint

### Example Test Cases:

**Echo API:**
- Method: POST
- URL: `http://127.0.0.1:5000/api/echo`
- Headers: `Content-Type: application/json`
- Body: `{"name": "Your Name"}`

**CRUD API:**
- Create: POST `/api/items` with body `{"name": "Item", "price": 100}`
- Read All: GET `/api/items`
- Read One: GET `/api/items/1`
- Update: PUT `/api/items/1` with body `{"name": "Updated", "price": 200}`
- Delete: DELETE `/api/items/1`

**Square API:**
- Method: POST
- URL: `http://127.0.0.1:5000/api/square`
- Body: `{"number": 10}`

## 💡 Key Takeaways

- ✅ Understanding RESTful API design principles
- ✅ Implementing CRUD operations
- ✅ Proper HTTP status code usage
- ✅ JSON data handling in Flask
- ✅ Error handling and validation
- ✅ API testing with Postman
- ✅ Request/Response cycle understanding

## 🔧 API Best Practices Applied

1. **Clear Endpoint Naming:** `/api/items`, `/api/echo`, `/api/square`
2. **HTTP Method Semantics:** GET (read), POST (create), PUT (update), DELETE (delete)
3. **Status Codes:** 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found)
4. **JSON Format:** Consistent request/response structure
5. **Error Messages:** Descriptive error responses

---

**Module Status:** ✅ Completed (3/4 tasks)  
**Next Steps:** Complete Task 2.4 and explore authentication tokens
