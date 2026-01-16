# Streamlit Applications

This module covers building interactive web applications using Streamlit, integrating machine learning models, and creating data visualization dashboards.

## 📚 What I Learned

- Building interactive web apps with Streamlit
- Session state management
- File upload and processing
- Integrating Hugging Face models
- Caching for performance optimization
- Chat interfaces and RAG systems
- Real-time data visualization
- Deployment concepts

## 🎯 Learning Resources

- Streamlit Official Documentation
- Streamlit API Reference
- Session State Tutorial
- Caching Best Practices

## 📝 Tasks Completed

### Task 1: Simple Greeting App
**File:** `app.py`

Build a basic interactive greeting application:
- Accept user name and message
- Generate random AI responses
- Display response with timestamp
- Session state management
- Form handling

**Features:**
- Text input for name
- Text area for messages
- Dynamic response generation
- Response history tracking
- Timestamp logging

**Run:**
```bash
streamlit run app.py
```

**Visit:** `http://localhost:8501`

### Task 2: CSV File Upload & Summary
**File:** `Task2Streamlit.py`

Data analysis tool with file upload:
- Upload CSV files
- Preview data
- Display dataset info (rows, columns)
- Show summary statistics
- Data exploration interface

**Features:**
- File uploader widget
- DataFrame display
- Statistics calculation
- Data preview
- Info display

**Run:**
```bash
streamlit run Task2Streamlit.py
```

**Usage:**
1. Upload any CSV file
2. View dataset preview
3. See statistics automatically

### Task 3: Text Generation with Hugging Face
**File:** `Task3Streamlit.py`

Interactive text generator using GPT-2:
- Text area for prompt input
- Generate multiple text variations
- Use beam search and sampling
- Display generated text
- Model caching for performance

**Features:**
- GPT-2 model integration
- Configurable generation parameters
- Multiple sequences generation
- Beam search implementation
- Cached model loading

**Parameters:**
- max_length: 80 tokens
- num_return_sequences: 3
- num_beams: 3
- early_stopping: True

**Run:**
```bash
streamlit run Task3Streamlit.py
```

### Task 4: Chat Application with GPT-2
**File:** `Task4Streamlit.py`

Interactive chat interface powered by GPT-2:
- Real-time text generation
- Chat history tracking
- Persistent session state
- Spinner for loading indication
- Response generation

**Features:**
- Text input for user messages
- Chat history management
- Model caching
- Loading spinner
- Response display

**Run:**
```bash
streamlit run Task4Streamlit.py
```

### Task 5: RAG System with Streamlit
**File:** `Task5RagStreamlit.py` & `Task5RagStreamlit1.py`

Advanced RAG (Retrieval Augmented Generation) system:
- Document upload and processing
- Vector embedding generation
- ChromaDB integration
- Semantic search
- Question answering interface
- Context-aware responses

**Features:**
- PDF/text document upload
- Chunking and embedding
- Vector database storage
- Query processing
- Context retrieval
- RAG pipeline

**Run:**
```bash
streamlit run Task5RagStreamlit.py
```

## 🚀 How to Run All Tasks

### Prerequisites
```bash
pip install streamlit
pip install pandas
pip install transformers torch
pip install sentence-transformers chromadb
```

### Individual Task Execution

**Task 1:** Greeting App
```bash
streamlit run app.py
```

**Task 2:** CSV Upload & Analysis
```bash
streamlit run Task2Streamlit.py
```

**Task 3:** Text Generation
```bash
streamlit run Task3Streamlit.py
```

**Task 4:** Chat Application
```bash
streamlit run Task4Streamlit.py
```

**Task 5:** RAG System
```bash
streamlit run Task5RagStreamlit.py
```

## 🔧 Key Streamlit Concepts

### Session State
```python
if "key" not in st.session_state:
    st.session_state["key"] = initial_value
```

### Caching
```python
@st.cache_resource
def load_model():
    return model
```

### Forms
```python
with st.form("form_key"):
    input = st.text_input("Input")
    submitted = st.form_submit_button("Submit")
```

### File Upload
```python
uploaded_file = st.file_uploader("Upload file")
if uploaded_file is not None:
    data = process(uploaded_file)
```

## 💡 Key Features Used

- **Widgets:** text_input, text_area, button, file_uploader, dataframe
- **Display:** title, write, subheader, info, warning, spinner
- **State Management:** session_state for data persistence
- **Performance:** @st.cache_resource for model caching
- **Interactivity:** Forms and real-time updates

## 🎨 UI Components

| Component | Purpose | File |
|-----------|---------|------|
| Form | Grouped inputs | app.py, Task4 |
| File Upload | CSV/PDF input | Task2, Task5 |
| Text Area | Multi-line input | Task3, Task4 |
| Button | Trigger actions | All files |
| DataFrame | Data display | Task2, Task5 |
| Spinner | Loading indicator | Task3, Task4 |

## ⚠️ Important Notes

1. **Caching:** Models are cached per session for performance
2. **Session State:** Data persists during session lifetime
3. **Rerun:** Every interaction triggers app rerun
4. **Performance:** Large models may take time on first run
5. **Deployment:** Can deploy on Streamlit Cloud for free

## 📊 Performance Tips

- Use `@st.cache_resource` for heavy models
- Use `@st.cache_data` for data processing
- Avoid reloading models on every interaction
- Limit batch sizes for large datasets
- Use session state for state management

## 🚀 Deployment

### Local Testing
```bash
streamlit run app.py
```

### Streamlit Cloud Deployment
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy automatically

### Docker Deployment
```dockerfile
FROM python:3.10
RUN pip install streamlit transformers
COPY . /app
WORKDIR /app
CMD ["streamlit", "run", "app.py"]
```

## 🔗 Live Features

- Real-time updates
- File upload and processing
- Model inference
- Chat interactions
- Data visualization
- Session persistence

---

