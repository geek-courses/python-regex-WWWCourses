# Regular Expression Challenges

## Objective
Utilize Python's `re` module to solve a series of text manipulation challenges, demonstrating your mastery of regular expressions.

## Tasks
1. Email Anonymizer
2. Date Formatter
3. Phone Number Standardizer
4. Whitespace Normalizer
5. HTML Tag Remover

## Setup

## Running Tests
Execute the following command to run the tests:
```sh
python -m unittest discover -s regex_module/tests
```

## Instructions for Students

### Step 1: Clone the Repository
1. **Open your terminal** (CMD or Git Bash on Windows).
2. **Navigate** to the directory where you want to clone the repository.
3. **Clone the repository** using the following command:
   ```
   git clone https://github.com/your-username/regex_challenges.git
   ```
   Replace `your-username` with the actual GitHub username that hosts the repository.

4. **Navigate** into the project directory:
   ```
   cd regex_challenges
   ```

### Step 2: Create a Separate Branch
1. **Create a new branch** for your work:
   ```
   git checkout -b your-branch-name
   ```
   Replace `your-branch-name` with a meaningful name for your branch, such as `solution` or `exercise`.

2. **Verify** that you are in your new branch:
   ```
   git branch
   ```
   The terminal should display a list of branches, with an asterisk (*) next to your new branch name.

### Step 3: Implement Your Solution
1. **Open the project** in your preferred code editor (e.g., VSCode, PyCharm).
2. **Navigate** to `regex_module/regex_functions.py`.
3. **Implement your solution** in the `regex_functions.py` file, replacing the placeholder comments with your code.

### Step 4: Run Tests
1. **Run the tests** to ensure your solution is correct:
   ```
   python -m unittest discover -s regex_module/tests
   ```
   All tests should pass if your solution is correct.

### Step 5: Commit Your Changes
1. **Stage your changes**:
   ```
   git add .
   ```
2. **Commit your changes** with a meaningful message:
   ```
   git commit -m "Implement solutions for regex challenges"
   ```

### Step 6: Push Your Branch to GitHub
1. **Push your branch** to the remote repository:
   ```
   git push origin your-branch-name
   ```

### Step 7: Create a Pull Request
1. **Navigate** to the repository on GitHub.
2. **Click** on the "Compare & pull request" button next to your branch.
3. **Fill out** the PR form with a title and description of your solution.
4. **Click** on the "Create pull request" button.

Congratulations! You have successfully cloned the repository, created a branch, implemented your solution, and submitted a pull request.

### Notes
- **Keep your branch up-to-date** with the main branch by occasionally running:
  ```
  git checkout main
  git pull origin main
  git checkout your-branch-name
  git merge main
  ```
- **Seek help** from instructors or classmates if you encounter any issues.

Happy coding!
