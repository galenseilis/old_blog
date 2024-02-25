---
title: Notes On Laszlo Sragner's PyData Talk On Code Smells 
date: 2024-02-25 04:49:15
authors: [galen]
categories: [data-science]
tags: [data-science,code-smells,computer-programming,communication]
math: true
mermaid: true
---

## Introduction
This post is my notes from the video *Laszlo Sragner - Code Smells in Data Science: What can we do about them? | PyData London 2023*. I don't necessary agree with all the points made, but I echo them as they're delivered.

<iframe width="560" height="315" src="https://www.youtube.com/embed/QJ4Z9KpdjIo?si=e9FoCuZ2JLC7HbXM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Notes

### Motivation
Why do we care about code smells?
- Programming is communication
- Communication needs a language
- We read more than we write
- Issues need standardized solutions
- Drive for productivity

Code smells are not bugs, and don't need immediate attention. They're also not technical debt or code rot. Code smell *might* cause problems, but not necessarily. A code smell can prevent changes to the code. There are various named code smells. Code smells have (or should have) recipes to resolve them.

### Readability
- Dead and unreachable code
	- Delete code
- Comments explaining code
	- Delete comments
	- Rename variables
	- Extract helpers
- Excess varaibles
	- Inline
	- Comprehensions
- Improper variable scope
	- Move lines with the same variables together
- Too many levels: if branches
	- Extract gaurd clauses
- Too many levels: for loops
	- Use comprehensions
- Multiple returns

#### Outcomes
- The code is one continuous logical flow
- Guard clauses on the top
- "Happy path" on the left
- Variable lifecycle is contained
- Return in the last line

### Bloaters
- Bloaters -> Extract class
	- Long parameter lists
	- Data clumps
	- Primative obsession
- Couplers -> Extract method
	- Feature envy
- Boolean parameters -> Dependency Injection
	- Move code to a class
	- Instantiate and call it in `main()`
- Couplers
	- Empty class
	- Middle man
	- Message chain
	- [Speculative generality](https://refactoring.guru/smells/speculative-generality)

### Establishing Culture
- Code review
	- Programming is communication
- Total cost of ownership
	- Managing long and short term goals
- Developer happiness
	- Autonomy
	- Mastery
	- Relatedness
- Drive cultural change
	- Increase velocity

### Takeaways
- Programming is communication
- Concentrate on the dataflow
- Identity problem areas
- Prepare the code
- Identity code smells
- Use refactoring recipes
- Evaluate the TCO of code
- Establish a culture

## Commentary

I agree that programming is sometimes a form of communication. It can be a form of communication to others or yourself in the future. There is no objective way to do this. Some person will look at a piece of code and then decide it is very clear, but another person could look at that code and decide that it is very unclear. How code is written for communication matters, but it matters in a statistical way. And yet high-quality empirical research to characterize this is rare because producing such studies requires an extraordinary amount of work.

Communication doesn't necessarily require a language, at least in the linguist's sense of the term. You can communicate with pets or wildlife that do not have a language. For computer programmers a useful language is obviously the source code. But not just the source code. Patrick Viafore's *Robust Python: Write clean and maintainable code* discusses multiple modes of communication (executable) code, comments,version control history, tests, wikis, in-project documentation, video recordings, design documentation, agile boards, email, instant messaging, direct communication, talks, code review, and meetings. Each of these modes vary by their cost and the degree of proximity required. Some modes are synchronous, and others asychronous.

I've heard this "we read more than we write" claim before. I don't know if it is true in general. On some projects I have read way more than I coded, and other times I coded pretty much the whole time. I suspect this just depends too much on context.

Having standardized solutions to well-understood issues makes sense. Issues that are not well-understood are not ready for a standard solution.

Productivity is definitely an important aspect of programming that the end-users/clients often appreciate. As long as it is genuine productivity and not just speed running towards something mediocre or worse.

Code smells are pretty much just people's intuitions about what is good or bad. They can come up with rationalizations, but they should often be taken with a grain of salt since what is good for human productivity isn't always intuition and sometimes there is subjectivity about what is better/worse anyway.

## Additional Links

- [Refactoring Guru](https://refactoring.guru/)
