# autocheck-latex-boilerplate

[textidot](https://github.com/sylvainhalle/textidote) verifies spelling, grammar, style, and run other sanity checks directly from a LaTeX file. This boilerplate repository executes textidot to the main.text file in a GitHub Action, generating issues with the found warnings.



## Link repository to an overleaf document

1. Fork this repo
2. Import the GitHub repository in overleaf: 
    ![link](.github/link.png)

    ![link](.github/select.png)

### Sync overleaf with GitHub

- To pull changes from GitHub in overleaf: Click the overleaf icon in the top left and click on the GitHub icon, then pull:
![git](.github/git.png)
![pull](.github/git_pull.png)

- To push changes from overleaf: Click the overleaf icon in the top left and click on the GitHub icon, then push:
![pull](.github/git_push.png)
  - Write the commit message
  ![commit](.github/git_commit.png)

## Automatic report on GitHub


This repository contains an [action script](.github/workflows/spell_checking.yml) to perform spell check in the latex document. The detected errors are reported in a separated branch (`reports`) in pdf and json format resulting from textidot. Also a new issue is opened after each push with the itextdot report. Each warning listed in the issue is connected with the main.tex line, for [example](https://github.com/Jacarte/autocheck-latex-boilerplate/issues/1).



## Spell check with textidot

To manual execute the spell check run the following command after downloading the textifot binary:

```java -jar textidot.jar --check en main.tex```