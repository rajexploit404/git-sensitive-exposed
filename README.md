# .Git Sensitive Expose Finder

### Description
The **.Git Sensitive Expose Finder** is a tool designed to identify exposed `.git/HEAD` files across a list of URLs. This can help identify potential repositories that have been improperly configured and may contain sensitive information. When a `.git/HEAD` file is found, it indicates the presence of a Git repository that might expose more critical files. The tool uses basic HTTP requests to check for the presence of `.git/HEAD` and checks for 200 OK responses, as well as other status codes like 404 and Bad Requests.

The tool helps security researchers and penetration testers to spot potential vulnerabilities in web applications or websites. For further exploitation, you can use **Git Dumper** to retrieve all files within an exposed Git repository.

### Requirements

To use this tool, you will need the following Python libraries:

- `requests`
- `colorama`
- `urllib3`

To install the required dependencies, you can use the `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the dependencies with:

```bash
pip install requests colorama urllib3
```

### Usage

1. **Prepare your list of URLs:**
   Create a `.txt` file (e.g., `list.txt`) that contains the list of URLs you want to check. Each URL should be on a new line.

2. **Run the tool:**
   Use the following command to start the tool:

   ```bash
   python3 main.py
   ```

3. **Enter the filename:**
   When prompted, enter the name of your URL list file (e.g., `list.txt`):

   ```plaintext
   ================================
   Made by Rajexploit404
   ================================

   Enter filename (e.g., 1.txt or 4.txt): list.txt
   ```

4. **Output:**
   The tool will display the results for each URL, indicating whether `.git/HEAD` was found or not. If a valid `.git/HEAD` is found, it will be saved to `found.txt`. A successful result would look like:

   ```plaintext
   http://sequoiahotel.net - 200 OK - ref: refs/ found
   http://dev.to - 404 Not Found - File .git/HEAD not found
   http://www.goingnet.com.tw - 200 OK - ref: refs/ found
   ```

   At the end of the process, all found URLs with `200 OK` responses will be saved to `found.txt`.

5. **Further Exploitation:**
   If you wish to further exploit the exposed `.git` repositories, you can use **Git Dumper** to dump all the sensitive information from the `.git` folder. Visit the Git Dumper repository for further details on how to use it:

   [Git Dumper Repository](https://github.com/arthaud/git-dumper)

### License
This tool is for educational purposes only. Use it responsibly and only on systems you have permission to test.


### Key Details:
- **Title**: `.Git Sensitive Expose Finder`
- **Description**: Explains the tool's functionality and what it is used for.
- **Requirements**: Lists dependencies and installation instructions.
- **Usage**: Provides detailed steps for running the tool and interpreting the results.
- **Further Exploitation**: Introduces the `Git Dumper` tool for further exploitation if needed.
- **License**: Notes that this tool is for educational purposes only.
