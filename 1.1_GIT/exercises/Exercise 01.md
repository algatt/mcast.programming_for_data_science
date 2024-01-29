# GIT Exercise

1. Create a GitHub repository called `mcast.programming_data_science.exercises` and make sure it's private.
2. All of the following steps must be done through terminal (except where stated not to). Take a note of all the commands that you've used.
3. Create a local git repository named the same as the GitHub repository, in any folder of your choosing. You will use this folder for this task.
4. Add a `README.md` file, and in it put a description. This repository will be used to keep track of the work that you do in this unit.
5. Commit this change.
6. Set this repository to link to the GitHub repository.
7. Push this commit to the online repository.
8. Go to `github.com` and check that the files have been uploaded.
9. Create a new branch named `test`, and switch to this branch.
10. Create a folder named `1.1_GIT` and in it create a file `Exercise 01.txt`. Put all the commands that you've used until now inside this file. For this step there is no need to use terminal.
11. Commit all your changes to the `test` branch.
12. Push the changes to GitHub making sure they are pushed to the `test` branch.
13. Merge the `test` branch into the `main` (or `master`) branch.
14. Add the last steps done to the file `Exercise 01.txt` and commit the changes.
15. Go to `https://desktop.github.com/` and install GitHub Desktop.
16. Open this repository in GitHub desktop.
17. From now on, if you prefer, you can use this application to manage your GIT resources.

<details>
    <summary>Answers</summary>
    <code style="display:flex; flex-direction:column; line-height:2rem;">
        <span>cd c:\git-training</span>
        <span>mkdir mcast.programming_data_science.exercises</span>
        <span>cd mcast.programming_data_science.exercises</span>
        <span>git init</span>
        <span>echo This will keep track of all the work done in this unit > README.md</span>
        <span>git add .</span>
        <span>git commit -m "README.md commit"</span>
        <span>git remote add origin https://github.com/algatt/mcast.programming_data_science.exercises.git</span>
        <span>git push -u origin master</span>
        <span>git branch test</span>
        <span>git checkout test</span>
        <span>mkdir 1.1_GIT</span>
        <span>cd 1.1_GIT</span>
        <span>Not in Terminal: Create Exercise 1.txt and paste all statements until now</span>
        <span>git add .</span>
        <span>git commit -m "Added Exercise 1"</span>
        <span>git push -u origin test</span>
        <span>git checkout master</span>
        <span>git merge test</span>
        <span>git add .</span>
        <span>git commit -m "Finished Exercise 1"</span>
        <span>git push</span>
    </span>
</details>
