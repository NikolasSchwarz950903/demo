# Demo
Demo-Repository for school

## Requirements
- Git installed and configured locally
- Python installed

## Task
1. Fork the remote repository at `https://github.com/HealYouDown/demo`
2. Clone the forked repository using `git clone https://github.com/<your_username>/demo`
3. Create your own branch using `git checkout -b <breanch_name>` (Preferably your name)
4. Implement the function found in `src/prim.py`:
    - The function takes an parameter `n`, and returns all prim numbers up to (including) `n` in any iterable container
    - You are **not** allowed to change the function name
5. Stage the changes using `git add src/prim.py` or `git add .` (to add all files to staging)
6. Create a meaningful commit message using `git commit -m  <msg>`
7. Push the changes to the remote repository using `git push -u origin <branch_name>`
8. To create a pull request, open the repository in your browser.
   1. Click on the tab "Pull requests"
   2. Click on "New pull request"
   3. For base branch, select `main`. For the comparing branch, select the branch you just created.
      1. Github will now show all commits done to the branch and a diff for all files.
   4. Now click on "Create pull request"
      1. You can now change the title and add a description. You can also assign reviewers if you want to.
   5. For the last time, click on "Create pull request"
9. Now code runners will check your branch and test the implemented function. You will see the status on your pull request page.
   1. If the status (except for reviews) is not green, you will have to check the error log and fix those issues.

You now finished the task.
