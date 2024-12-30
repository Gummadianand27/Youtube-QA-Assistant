# **YouTube Q/A Assistant**

### **Project Overview**
The **YouTube Q/A Assistant** is a user-friendly tool designed to answer questions about the content of YouTube videos. By providing a video URL and a query, this assistant retrieves the video transcript and generates detailed responses using OpenAI's GPT models and LangChain.  

This project has two main components:

  1. Frontend: A Streamlit-based interface for user interaction.
  2. Backend: A LangChain-powered script that handles transcript retrieval, storage, and querying using FAISS and OpenAI APIs.

By utilizing Streamlit-based user interface for seamless interaction and LangChain's advanced features, such as FAISS for transcript storage and retrieval, it ensures efficient and precise query handling.

---

### **Installations**
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed, then execute:
   ```bash
   pip install -r requirements.txt
   ```
   Key libraries include:
   - `streamlit`
   - `langchain`
   - `faiss-cpu`
   - `openai`
   - `python-dotenv`

3. **Set Up Environment**:
   - Create a `.env` file to securely store your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

---

### **Usage**
1. **Launch the Application**:
   Start the Streamlit interface using:
   ```bash
   streamlit run yt_main.py
   ```

2. **Interact with the Assistant**:
   - Input the YouTube video URL in the provided field.  
   - Enter your query related to the video’s content.  
   - Provide your OpenAI API key (kept secure).  

3. **Submit Your Query**:
   - The assistant extracts the video transcript, stores it in a FAISS database, and retrieves the most relevant information through a similarity search.  
   - A detailed, factual answer is generated based on the transcript and displayed in the interface.

---

### **Results**
The **YouTube Q/A Assistant** delivers:  
- Clear and verbose answers derived directly from the transcript of the video.  
- Example Output:  
  ![YouTube QA Assistant.png](#)
- An image showcasing the application's interface and response.

---

### **Acknowledgements**  
**freeCodeCamp.org**: This project draws inspiration from [freeCodeCamp.org's video on YouTube](https://www.youtube.com/watch?v=lG7Uxts9SXs). The concepts and techniques discussed in the video played a significant role in shaping this project. A big thanks to Rishab Kumar for the insightful content!
