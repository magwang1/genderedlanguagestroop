# Gendered Language Stroop Task
## Overview

This PsychoPy project is a modified Stroop experiment exploring whether stereotype-congruent and stereotype-incongruent gender cues influence reaction time and accuracy during word categorization. 

Research Question: "Do gender-coded visual cues interfere with reaction time and accuracy when participants categorize masculine- and feminine-coded trait words?"
## Aim

The goal of this experiment is to examine whether stereotypical gendered visual cues interfere with semantic processing of gendered language. The experiment seeks to understand if participants respond more slowly or less accurately when a masculine-coded word is presented in a feminine-coded color, or vice versa. This is based on principles of Stroop interference and gender schema theory.

Gender schemas are learned cognitive frameworks shaped by cultural and social norms, and they perpetuate stereotypes about what is "masculine" and "feminine." For example, the color pink is associated with femininity and the color blue is associated with masculinity as a result of learned mental frameworks. These schemas can influence interpersonal interactions, self-concept, behavior, perception, and memory. 

In a classic Stroop task, people are slower in response time when word meaning conflicts with ink color. In other words, when the color conflicts with the word category, participants may experience cognitive interference.
This particular modified Stroop task seeks to examine whether socially learned gender schemas can create a cognitive conflict when a word’s stereotypical meaning is incongruent with the gender-coded color visual cue.

## Experimental Design
### Independent Variables
- Word category (masculine-coded vs. feminine-coded)
- Congruency condition (congruent vs. incongruent color pairing)
### Dependent Variables
- Reaction time (RT)
- Accuracy
- Gender ratings of words

### Stroop Task

The participants are shown various personality, appearance, and behavioral trait words that were selected due to strong associations with common stereotypes of masculinity or femininity. The words are displayed in either a stereotype-congruent or stereotype-incongruent color condition (pink and blue) and participants must categorize the meaning of the word as "masculine" or "feminine" while ignoring the color condition of the text.

Participants will press "**M**" for masculine-coded words or press "**F**" for feminine-coded words while ignoring the color of the words.

Example:
- "dominant" shown in blue would be congruent
- "dominant" shown in pink would be incongruent

### Word-Rating Task
After the Stroop task, participants will rate each word on a scale of 1 to 5 with 1 being "strongly feminine" and 5 being "strongly masculine." This task is used to further explore the variability in gender perception across participants as well as assess how well the selected words reflect culturally common gender stereotypes.

## Instructions for Running the Experiment
Open genderstroop.psyexp in PsychoPy Builder.

Download both csv. files and make sure they are located in the appropriate folder as the experiment files.

Click the "Run" button and follow the onscreen instructions.

### Files Included
- genderstroop.psyexp: PsychoPy Builder experiment file
- genderstroop_lastrun.py: automatically generated PsychoPy Builder script
- genderstroopclean.py: clean copy of pseudocode
- stimuli.csv: Stroop task stimulus file
- ratings.csv: Word-rating task stimulus file 

### Packages Needed
This experiment was created using Python in PsychoPy Builder.

Python libraries used: psychopy, pandas

### Analysis
The primary analysis would compare reaction time and accuracy between stereotype-congruent and stereotype-incongruent trials. Mean reaction times would be compared between congruent and incongruent trials. Accuracy rates would be compared across congruency conditions. The average ratings for each word would analyzed to determine whether the stimuli were perceived as stereotypically assumed and to identify which words were viewed as more strongly gendered. Additionally, individual Stroop interference magnitude could be related to the participant's own ratings of the words.

### Implications
It is hypothesized that participants will respond more slowly on stereotype-incongruent trials and make more errors on incongruent trials compared to congruent trials. These findings would suggest that stereotypical gendered visual cues may automatically interfere with the semantic processing of gendered language, indicating a Stroop-like cognitive interference that reflects the role of gender schemas. 
