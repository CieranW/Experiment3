# Experiment3: Hermit Crab Essay
def intro():
    input('\n'"Welcome to my essay for Experiment #3. Press Enter on your keyboard to continue unless prompted otherwise."'\n')
    input("This is a script designed to be in Hermit Crab essay format."'\n')
    input("Throughout the experiment, I will be utilizing the different types of Python functions and programs as shells, and my words/writings as fillers for the aforementioned shells."'\n')


def yes_or_no():
    count = 0
    yes = "y"
    no = "n"
    while count == 0:
        # Give reader a choice.
        choice = str(input("So, shall we begin? (Enter y or n to start)"'\n'))

        if choice is not no or choice is not yes:
            print("Please enter a valid answer."'\n')
            count += 0

        if choice == no:
            count += 1
            print("Sorry to see you go :)")
            break  # Ends the program.

        if choice == yes:
            count += 2


def main_body():
    input('\n'"Fantastic!"'\n'"Gather around, kids. It's story time!"'\n')

    input("It all began with an assignment prompt, write an essay using hermit crab format. In all honesty, I had no idea how to start it or what I wanted to do. Did I want to use a brochure format? A wikipedia article style? I had no clue, no idea on how to begin writing; and that was the least of my concerns, how would my professor react to me using a python script as a shell for my essay? Would it be deemed acceptable or would I get an immediate fail for not adhering to the prompt? So many questions and issues, why do I do this to myself?"'\n')

    input("Given the circumstances, it is highly plausible that I would have been drawn to something simpler, say a travel brochure or a cookbook. However, it is either insanity or sheer stupidity that drove me to attempt to use a programming language to write my essay. I don't even have AutoCorrect, so I am probably gonna have to run this through Word later to make sure I've got this down. But I digress, programming is beautiful. I have done so much in the short amount of time I have spent learning and practicing my programming skills; and today I will attempt to impress upon you, dear reader, the capacity and length of my skill and range."'\n')

    input("As mentioned earlier, I will attempt to utilize different types of functions to assist in my quest of writing a hermit crab essay with python."'\n')

    input("An example if you will: Say I requested a sentence or phrase of your own choosing which will be typed by you, dear reader. I can then take that particular sentence that you have typed out so carefully, and insert it into a paragraph of my own."'\n')


def questions():
    # Store inputted string
    q1 = str(input(
        "Allow me to demonstrate. Please type a sentence/phrase of your own in the line below:"'\n'))

    input('\n'"Taking in your sentence/phrase, I can insert it randomly however I want. I can call it in two sentences from now, or I could call it in at the end of the essay. However, there are certain limitations to how I could implement said sentence, obviously a result in part due to my novicity and limited understanding of the joy of python."'\n')

    input("Let me call on your sentence/phrase now."'\n')

    # Calls upon the inputted string from earlier
    input(q1)

    input('\n'"If you had entered it correctly, then your sentence should have shown up after I had typed 'Let me call on your sentence now.'."'\n')

    input("But words and sentences are not the only thing I can take in from you and call upon later. Python is capable of doing that with numbers too."'\n')

    # Stores number 1
    n1 = int(
        input("Please indulge me and enter a whole number of your own choosing:"'\n'))
    # Stores number 2
    n2 = int(input('\n'"Now enter a second number:"'\n'))

    input("Why don't we take those two numbers and turn it into an equation?"'\n')
    input("Try a simple x^2 + y^2."'\n')
    input("Taking in your numbers from earlier, we should get the following:"'\n')

    # x^2 + y^2
    a1 = (n1*n1) + (n2*n2)
    input(a1)

    input("As shown, {n1}^2 should give us {0}, and {n2}^2 is {1}. And together they give us {a1}.".format(
        (n1*n1), (n2*n2)))

    input('\n'"We can even take in your numbers from earlier and put it into a different type of equation, say a tax calculator."'\n')

    # Calculate tax based on numbers 1 and 2
    tax = round((n1 * (1 + (n2/100))), 2)

    # Using the tax formula, calculate price and round to two decimal places
    price = round((n1*n2)*(1+(n2/100)), 2)

    input("Using the first number as your initial price (${n1}), and your second number as your tax percentage ({1}), we can get the following:".format(
        round((n2/100), 2)))

    input('\n''\t'"Your final price is: ${tax}.")

    input(
        '\n'"This is done through the following calculation: ${n1} x (1+({n2}/100)) = ${tax}."'\n')
    return q1, n1, n2, price


def story_time():
    input("Let's put your sentence and numbers to good use."'\n')

    # Story time, takes in the string and numbers inputted by reader and turns it into a story.
    input('\t'"A man walks into a small, quaint shop that sells doughnuts (I'm craving doughnuts as I'm typing this).")
    input(
        "He exclaims, 'How much for one, kind sir?', to which the owner replies, 'Why my good man, it is ${n1} a piece.'")
    input("'I will take {n2} then', the man remarks.")
    input(
        "'Fantastic choice, lad. Truly worth every penny. Your total for today is ${price}, tax included, of course.'")
    input(
        "'Wonderful, my good lord. {q1} I bid thee good day.'")
    input('\t'"And so ends our wonderful story of a man in a doughnut shop."'\n')


def ending():
    no = "n"
    yes = "y"
    # Loop to run program again.
    q2 = str(input("Would you like to run that again? (y/n)"'\n'))
    if q2 == no:
        input("Thank you for coming along on my little adventure. Whether or not I will attempt to do this again remains to be seen, depending on the grade I get. Although I perhaps may not have followed the prompt assigned, it was my ambition to use a programming language as a medium or an avenue for my essay. Regardless of the result, I have had quite the time writing this, which is nothing to laugh at as I have spent a deal greater than I would have should I have stuck with writing it out in Microsoft Word. There were many challenges that I have faced, bugs to debug, and formats to change, many of which, given the time I had have not solved nor figured out. An example being getting the paragraphs and sentences to format correctly in the terminal. Nevertheless, I very much enjoyed doing this and would hope to commit in the future."'\n')

        input('\t'"The End."'\t')
        # break

    if q2 == yes:
        count -= 2


# Calls upon the function, main
intro()
yes_or_no()
main_body()
questions()
story_time()
ending()
