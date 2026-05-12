from psychopy import visual, core, event, data
import pandas as pd

# Load stimuli
stimuli = pd.read_csv("stimuli.csv")
ratings = pd.read_csv("rating_stimuli.csv")

# Create window
win = visual.Window(
    size=(1000, 700),
    color="black",
    units="height"
)

# Fixation cross
fixation = visual.TextStim(
    win,
    text="+",
    color="white",
    height=0.08
)

# Trial stimulus
word_stim = visual.TextStim(
    win,
    height=0.10
)

# Rating scale text
rating_scale = visual.TextStim(
    win,
    text="""
1 = strongly feminine

4 = neutral

7 = strongly masculine
""",
    pos=(0, -0.25),
    color="white",
    height=0.04
)

# INSTRUCTIONS SCREEN

instructions = visual.TextStim(
    win,
    text="""
Welcome to the Gendered Language Stroop Task.

You will see words related to personality traits, appearance, and behavior on the screen.

Your task is to categorize the WORD, not the color.

Please press:
M = masculine-coded word
F = feminine-coded word

Ignore the color of the text.

Please respond as quickly and accurately as possible.

Press SPACE to begin.
""",
    color="white",
    height=0.04
)

instructions.draw()
win.flip()

event.waitKeys(keyList=["space"])

# Trial loop
for index, trial in stimuli.iterrows():

    # Show fixation cross
    fixation.draw()
    win.flip()
    core.wait(1.0)

    # Present word stimulus
    word_stim.text = trial["word"]
    word_stim.color = trial["color"]

    word_stim.draw()
    win.flip()

    # Start reaction time clock
    rt_clock = core.Clock()

    # Collect response
    keys = event.waitKeys(
        keyList=["m", "f"],
        timeStamped=rt_clock
    )

    response, rt = keys[0]

    # Determine accuracy
    correct = response == trial["correct_key"]

    # Print trial data
    print(
        "Word:", trial["word"],
        "| Condition:", trial["congruency"],
        "| Response:", response,
        "| Correct:", correct,
        "| RT:", rt
    )

    # Brief blank interval
    win.flip()
    core.wait(0.5)
# Rating instructions
rating_instructions = visual.TextStim(
    win,
    text="""
Now you will rate each word.

For each word, rate how gender-coded it feels to you on a scale of 1-5.

Press:
1 = strongly feminine
2 = slightly feminine
3 = neutral
4 = slightly masculine
5 = strongly masculine

Press SPACE to begin.
""",
    color="white",
    height=0.04
)

rating_instructions.draw()
win.flip()

event.waitKeys(keyList=["space"])
# Word rating task
for index, row in ratings.iterrows():

    # Display word
    word_stim.text = row["word"]
    word_stim.color = "white"
    word_stim.pos = (0, 0.2)

    word_stim.draw()
    rating_scale.draw()

    win.flip()

    # Collect rating
    rating = event.waitKeys(
        keyList=["1", "2", "3", "4", "5", "6", "7"]
    )[0]

    # Save rating
    print(
        "Word:", row["word"],
        "| Rating:", rating
    )

# END SCREEN
end_text = visual.TextStim(
    win,
    text="""
Thank you for participating!

The experiment is now complete.

Press SPACE to exit.
""",
    color="white",
    height=0.05
)

end_text.draw()
win.flip()

event.waitKeys(keyList=["space"])

win.close()
core.quit()