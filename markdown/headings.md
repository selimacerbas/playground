# This is heading level 1
## This is heading level 2
### This is heading level 3
#### This is heading level 4
##### This is heading level 5
###### This is heading level 6

This is the alternative Syntax for heading 1.
===

This is the alternative syntax for heading 2.
---

Paragraphs
===

This is paragraph. Which is actually plain text.
These are seperate paragraphs and this should work.
As you can see.

Emphasis
===

This is a **bold text**.
This is a __bold text__ as well! But mostly other one is better.

You can also em**pha**sis the middle of the word.

This is an *italic text*.
This is an _italic text_.

You can also i*tali*c the middle of the word!

This is both ***bold and italic***!  
This is both __*bold and italic*__!  
This is both **_bold and italic_**! 

We can not make bold and itallic of the m***iddl***e of the word.

# Quotes

> ## I can  even put heading in it.
> Stay hungry, stay foolish.
I did not put here anything.  
This does not belongs it since there is 2 space at the end of the previous line.
>> - Nesting in the block quotes.
>>> - This is another nesting.

# Lists

1. List item 1
2. List item 2
3. List item 3
    1. First nested item
4) List item 4
5) List item 5   


- List item 1
- List item 2
- List item 3
  - First nested item
- List item 4
- List item 5

+ List item 1
+ List item 2
+ List item 3
  + First nested item
+ List item 4
+ List item 5

+ 20\. this needs to be escaped since dot causes misunderstanding

# Images with Markdown

![Here is the image or video](link)
![Here is the image or video](link "Adding quotation mark lets you hover a writing on the image or video when user hover on it.")
[![Here is the image or video](link)](https://www.google.com) This makes your picture clickable and takes user to the given link. Simply cover up whole link again with []().

# Codes and Codeblocks

`this is a code`

```bash

this is code block


```

# Tables

| Column1 | Column2 | Column3 |
| ------------- | -------------- | -------------- |
| This is cool! | Item1 &#124;Item2 | Item1 |

# Checklists

- [x] Checklist 1
- [] Tasklist 2
 
# Definition Lists

**Term one**  
: This is the definition of term one.  
: This is the second defintion of term two.

# Footnote

This is a simple text with footnote.[^2]

continue  
continue  
continue

[^2]:If you clicked on the footnote it brought you here.

# Subscript and Superscript

H~2~SO~4~

<H~2~SO~4~>

# Text Highlighting

This is a ==**very important**==.

The current price is ~~$59~~ $9.99.

# Esmeralda Note Taking

| Table 1 | Table 2 |
|--- | --- |


```mermaid
C4Context
title Payments Platform – System Context
Person(customer, "Customer")
System_Boundary(b, "Payments Platform") {
  System(api, "Public API", "REST")
  System_Boundary(core, "Core Services") {
    System(service, "Payments Service")
    System(db, "Ledger DB", "PostgreSQL")
  }
}
Rel(customer, api, "Sends requests over HTTPS")
Rel(api, service, "Calls")
Rel(service, db, "Reads/Writes")
