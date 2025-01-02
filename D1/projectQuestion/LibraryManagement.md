 
library_question = """
# Library Management System - Python Console Program

### **Problem Statement**

Design and implement a Python console-based **Library Management System** that allows users to interact with the library for various operations. The system should include the following features:

### **Features:**

1. **Book Search:**
   - Users should be able to search for a book by **title**, **author**, or **ISBN**.
   
2. **Book Checkout:**
   - Users should be able to **checkout** books. The system should check if the book is available in the library before allowing the checkout. The system should also record the **due date** for returning the book.
   
3. **Book Return:**
   - Users should be able to **return** books. The system should calculate the number of days the book was overdue, if applicable, and apply a **fine** for overdue books.

4. **Book Reservation:**
   - Users should be able to **reserve** a book if it's not currently available. The system should notify the user when the book becomes available.
   
5. **User Registration:**
   - The system should allow new users to **register**. Each user should have a **unique ID** and their personal details stored in the system.

6. **Overdue Fines:**
   - For each book that is returned after the due date, the system should charge an overdue fine. The fine should be a fixed amount per day of being overdue (for example, $1 per day).

7. **View Available Books:**
   - Users should be able to view the list of **available books** in the library, including book title, author, and ISBN.

8. **View Borrowed Books:**
   - Users should be able to view the list of books they have borrowed, including due dates and fine status.

### **Your Task:**
Implement a Python program that satisfies the above features. The program should:
- Allow users to search for books and view available ones.
- Allow users to checkout, return, and reserve books.
- Handle overdue fines.
- Register new users and track their borrowed books.

### **Example Scenario:**
1. A user named "Emma" registers with the system. She checks out a book titled "The Great Gatsby." The system records the due date.
   
2. Emma returns the book **3 days late**. The system applies a **fine** of $3 (if the fine is $1 per day).
   
3. A user named "Jake" searches for a book titled "1984" by George Orwell. If the book is available, he can check it out.
   
4. Jake reserves "To Kill a Mockingbird" because it is currently unavailable, and he is notified when it becomes available.
"""

 