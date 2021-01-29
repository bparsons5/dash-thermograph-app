##### UNCLASSIFIED
# Contributing to Thermograph Tool

When contributing to the development of Thermograph Tool, please first discuss the change you wish to make via issue, email, or any other method with the maintainers before making a change.

Please note we have a [Code of Conduct](#code-of-conduct), please follow it in all
your interactions with the project.

## Table of contents
1. [Ways to Contribute](#how-can-i-contribute?)
2. [Creating an issue](#creating-a-gitlab-issue)
3. [Template](#issue-template)
4. [Pull requests](#pull-request-process)
5. [Code of Conduct](#code-of-conduct)
6. [Styleguide](#styleguide)
7. [Acknowledgments](#acknowledgments)
8. [Contact Us](#contact)

## How Can I Contribute?

Here in OSO-DA, we want to utilize your skills as a resource. You have your own perspective and creativity that gives an outside look on the Thermograph Tool tool. Below are some ways we know you can help us be better and produce a better product. Start by checking out the [Creating a Gitlab Issue](#creating-a-gitlab-issue) section.

- Report Bugs
- Suggest or Build New Features
- Design Decisions & Insights
- Adding or Updating Documentation & Comments

## Creating a Gitlab Issue

There are many ways you can contribute to Thermograph Tool, and all of them involve creating issues
in [Thermograph Tool issue tracker](). This is the entry point for your contribution.

To create an effective and high quality ticket, try to put the following information on your
ticket:

 1. A detailed description of the issue or feature request
     - For issues, please add the necessary steps to reproduce the issue.
     - For feature requests, add a detailed description of your proposal.
 2. A checklist of Development tasks
 3. A checklist of Design tasks
 4. A checklist of QA tasks

### Issue template
```
[Title of the issue or feature request]

Detailed description of the issue. Put as much information as you can, potentially
with images showing the issue or mockups of the proposed feature.

If it's an issue, add the steps to reproduce like this:

## Computer Specs
* [ ] computer OS
* [ ] version of python 3
* [ ] version of Visual Studio (IDE or code editor)
* [ ] any additional relevant specs

## Steps to reproduce

## Design Tasks

* [ ]  design tasks

## Development Tasks

* [ ]  development tasks

## QA Tasks

* [ ]  qa (quality assurance) tasks
```

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below in the [Contact](#contact) section.

## Pull Request Process

1 - Create folder in the desired directory labeled *Thermograph Tool*.

2 - Open a command prompt or git bash within the *Thermograph Tool* folder and create a git repository in that folder by running the following:
```bash
cd <folder-path>
git init
```

3 - Clone the OSO-DA *Thermograph Tool* project.
```bash
git remote add origin git@sc.appdev.proj.coe.ic.gov:qt41594-nga/thermograph-tool.git
git pull origin master
```

4 - Create a new branch for your own work and push to gitlab. Name your branch according to the new feature you wish to add.
```bash
git checkout -b <new-branch-name>
git push origin <new-branch-name>
```

5 - Now in RStudio's console, ensure that all dependencies are installed. See the Dependencies section in the README.md for a list. See below to see how to install a python library.
```python
python3 -m pip install <python-package-name>'
```

7 - Once all dependencies are installed, open a terminal in the route folder (Visual Studio will do this for you when you select Terminal > New Terminal). Then run the below command to run the app.
```python
python3 app.py
```

8 - When the app loads, you can start coding the new feature.

9 - Once finished, you may merge once you have the sign-off of the maintainers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.


## Code of Conduct

### Summary

OSO-DA creates software for a better world. We achieve this by behaving well towards
each other.

Therefore this document suggests what we consider ideal behaviour, so you know what
to expect when getting involved in OSO-DA. This is who we are and what we want to be.
There is no official enforcement of these principles, and this should not be interpreted
like a legal document.

### Advice

 * **Be respectful and considerate**: Disagreement is no excuse for poor behaviour or personal
     attacks. Remember that a community where people feel uncomfortable is not a productive one.

 * **Be patient and generous**: If someone asks for help it is because they need it. Do politely
     suggest specific documentation or more appropriate venues where appropriate, but avoid
     aggressive or vague responses such as "RTFM".

 * **Assume people mean well**: Remember that decisions are often a difficult choice between
     competing priorities. If you disagree, please do so politely. If something seems outrageous,
     check that you did not misinterpret it. Ask for clarification, but do not assume the worst.

 * **Try to be concise**: Avoid repeating what has been said already. Making a conversation larger
     makes it difficult to follow, and people often feel personally attacked if they receive multiple
     messages telling them the same thing.


In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

## Styleguide

Please abide by [Google's python Style Guide]().



## Acknowledgments
- T Rex
- OSO-DA colleagues

## Contact

OSO-DA Team  |  Title  |  Email  |  Phone number
--------------  |  --------------  |  --------------  |  --------------
Robert Brett Parsons  |  Computer & Data Scientist  |  bparsons@apogeeintegration.com  |  757-773-6699
Rachel Carrig  |  Lead Data Scientist  |  rcarrig@apogeeintegration.com  |  713-504-6575
> **Note:** You can also contact Brett Parsons at his Apogee Integration Email at bparsons@apogeeintegration.com for any unclassified questions.
