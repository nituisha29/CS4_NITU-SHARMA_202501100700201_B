# CS4_NITU-SHARMA_202501100700201_B
# 📄 Case Study 4 – File Handling and Log Analysis

## 📌 Problem Statement

Given a log file named **CS4.txt**, perform multiple file handling operations using Python. The tasks include reading file contents, classifying logs based on severity levels, writing filtered data into separate files, implementing a search feature, and demonstrating file pointer operations.

---

## 🎯 Objectives

* Understand file reading techniques in Python
* Perform log classification using string matching
* Write filtered data into new files
* Implement user-driven search functionality
* Demonstrate file pointer manipulation using `seek()`

---

## 🧩 Approach

### 🔹 Task 1: Basic File Reading

* Used:

  * `read()` → to read entire file content
  * `readline()` → to read first two lines
  * `readlines()` → to store all lines in a list
* Printed:

  * Total number of lines
  * First 2 lines
  * Last 2 lines

---

### 🔹 Task 2: Log Classification

* Iterated through each line of the file
* Counted occurrences of:

  * `"INFO"`
  * `"WARNING"`
  * `"ERROR"`
* Stored results in a dictionary:

  ```python
  {"INFO": x, "WARNING": y, "ERROR": z}
  ```

---

### 🔹 Task 3: Writing Filtered Files

* Created three separate files:

  * `info_logs.txt`
  * `warning_logs.txt`
  * `error_logs.txt`
* Stored corresponding log lines using:

  * `write()`
  * `writelines()`

---

### 🔹 Task 4: Search Feature

* Took user input (keyword)
* Displayed all matching lines
* Saved results in:

  * `search_result.txt`

---

### 🔹 File Pointer Operations

Performed using `seek()`:

* Read first 50 characters
* Moved pointer to:

  * Beginning → `seek(0)`
  * Middle → `seek(len(file)//2)`
  * End → `seek(-100, 2)` *(using binary mode)*

---

## ⚠️ Important Note

* Negative seek from the end (`seek(-100, 2)`) works only in **binary mode (`rb`)**
* In text mode (`r`), it raises:

  ```
  io.UnsupportedOperation
  ```

---

## 📂 Files Included

* `CS4.txt` (input file)
* `main.py` (Python solution)
* `info_logs.txt`
* `warning_logs.txt`
* `error_logs.txt`
* `search_result.txt`
* Output Screenshot

---

## 🖥️ Sample Output

```
---- Task 1 Output ----
Total number of lines: 10

First 2 lines:
2026-04-01 10:15:32 INFO User login success user_id=101
2026-04-01 10:17:45 ERROR Database connection failed

Last 2 lines:
2026-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully
---- Task 2 Output ----
Log counts: {'INFO': 5, 'WARNING': 2, 'ERROR': 3}

---- Task 3 Output ----
Filtered files created successfully.

Enter keyword to search (INFO/WARNING/ERROR): WARNING
2026-04-01 10:20:10 WARNING Disk usage at 85%
2026-04-01 10:35:40 WARNING Memory usage high

Search results saved in search_result.txt

---- File Pointer Operations ----

First 50 characters:
 2026-04-01 10:15:32 INFO User login success user_i

After seek(0):
 2026-04-01 10:15:32 INFO User login success user_i

From middle:
 necting to server
2026-04-01 10:32:11 INFO User l

Last 100 characters:
 26-04-01 10:45:50 ERROR Failed to write file
2026-04-01 10:50:05 INFO Backup completed successfully
```

---

## ✅ Conclusion

This case study demonstrates practical usage of Python file handling, including reading methods, log processing, file writing, search implementation, and pointer manipulation. It highlights important distinctions between text and binary modes while handling files.

---
