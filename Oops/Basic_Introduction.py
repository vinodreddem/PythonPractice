"""so there's several different programming paradigms and up until now in this

course we've been mainly using the imperative style of programming

imperative programming involves providing a series of instructions for

the computer to follow in a defined order now object oriented programming

aims to combine data and the processes that act on that data into objects which is

called encapsulation.

before I continue it's important to realize that the different paradigms are

not necessarily exclusive and object-oriented programming makes use of

imperative programming within the methods that objects used to manipulate

the data also as we will see shortly our imperative programming in Python has

actually made extensive use of objects we just didn't know that so the approach that

we've been using so far in the course is very similar to a recipe for cooking a

meal so the recipe starts with the ingredients and utensils it will be need

which corresponds to a programs data and then continues with the description of

the steps that must be performed on that data to produce in this case for the

recipe

finished meal an object oriented approach relies on the objects such as

the eggs milk spoon etc knowing how to perform certain operations so

the program just tells them to do so

concept of an egg that knows how to fry itself is a little bizarre but that

really shows that the imperatives approach to cooking a meal is more

appropriate than an object-oriented approach

now a good example of the encapsulation of data and function might be self lighting

cigarettes well actually its a bad example and I certainly wouldn't

want to suggest that smoking is good but it does demonstrate the concept quite well

so without object oriented programming the steps to smoking a cigarette might

be place cigarette in mouth that's number one number two light match number three

hold match to cigarette and number four inhale now encapsulating the functions

that can be performed on the cigarette into the cigarette reduces the code to

place cigarette in mouth and inhale so the cigarette knows how to light itself so

that's not something that the smoker needs to be concerned with

the details of how it lights itself are built into it when it's manufactured or

in the case of programming it's programmed into it when it's defined

and the actual implementation is of no interest to anything that uses the

object now I've exercise a little license they're self lighting cigarettes were

produced for short time the 1960's coincidentally around the same time that

object oriented programming was conceived and had a igniter

built into them that had to be struck like a match the advanced type that I described only

existed in science fiction stories now modern electronic cigarettes take this

concept a little bit further but it's only the details of the implementation

that have changed so the method use remains pretty much the same as the

science-fiction variety now that's important concept of object oriented

programming as we will see replacing one object with another one that performs

the same task without having to concern ourselves with the details of how it

performs the task is central to object oriented programming so another and

hopefully much more healthier example might be an electric kettle now the

imperative approach to boiling water for hot drink might be step 1 fill kettle with

water

step 2 light stove step 3 place kettle on stove step 4 for monitor kettle until

water boils step 5 make the drink now it would then have to be a function that

deals with lighting the stove which might involve further functions to collect

water or coal or was switched on the gas a function to light the match and so on but

in object orientated terms a kettle would have a boil method that is triggered by

operating a switch so the object oriented program comes down to step

one fill kettle with water

step 2 switch kettle on step 3 when kettle switches off make drink so the

imperative approach will also have to identify the type of stove being used as

its futile and probably a bit dangerous to hold a match to electric cooker

now these examples may make it look like we've got something for nothing because

performing the tasks using an object oriented approach involves fewer steps

but there's no magic involved here now the steps are still had to be programmed

but their built into the objects so that anything that using the object doesn't have to be

concerned about them so the object orientated kettle has been built to contain an

element or whatever method it employs could be a ceramic disc or even a small

nuclear reactor and the operation of the heating mechanism has been wired up to

the switch where the kettle was made so a lot of work has gone into the production on

the kettle in other words far more so that the work that goes into making a kettle

for use on the stove but subsequent use of the kettle is there much easier

because it knows how to perform its function itself so one thing that may

not be obvious and I haven't yet mentioned is that everything in Python is an object so Python

is unusual in this respect because even though Python uses objects extensively you

don't actually have to be aware of that to use so Python can be used for

object-oriented programming but can also be used to write purely imperative

programming code so in fact the Wikipedia entry for Python which I'm going to just load

up the screen now you can see the link in the top left hand corner you can see

just down here it says that Python supports multiple programming paradigms

including object oriented imperative and functional programming or procedural

styles so in Java which is considered a class-based object-oriented language

there are primitive types such as an

int and a double so if you've come to Python from Java the following code which I'm

about to show might seem very odd at first so lets just go back to IntelliJ and I've created a

new project here and a new Python file so if you come back come from Java type in

code like this....

....so if we just run this see that it does

work and we get the same result each time so line 3...and

that's pretty normal for a programming language like Java

but the code on line 4 would probably be a bit bizarre and that's because the a even though

it's been defined as you can see on line 12 as a number you could see that a has

got an add method even though its an integer so if I command click add

and that is control click on a PC or Linux you can see that there's a method this is the

built-ins definition of the add method and interestingly enough if I go back to oop

our file and click on the plus note that it has gone to the same method in the built ins

so what you can see by that is that whether you use this __add__

or use a plus it's calling the same code that is built-in

builtins.py file and in this case add two numbers together and smart enough to

figure out the parameters you can see there that the second argument in the

case of line 3 is then added and line 4 the parameters b is added to the value

of a now if this is your first programming language and either you see

nothing at all strange about this or it will make very little sense but don't worry

I'm gonna explain what it all means but I wanted to warn you that you know if

you've come from other programming languages such as Java or C++ you

probably gonna see some aspects of Python that seem surprising to you at

least initially now when I said that everything in Python is an object I meant

everything even types are implemented as classes now I will come

back to that but for now I'm gonna focus on making sense of what I've just done

their so object-oriented programming uses classes and methods to provide object

that encapsulates both data and the functions that operate on that Data now the

method is just another word for function and you have seen me use those terms

interchangeably in this course but being big correct here when a function is part of

a class in Python we call it a method now in Python there is a slight

difference between a function and a method but writing a method is the same

as writing functions now what we gonna do is start with a very simple example

to introduce the concept of a class and show how classes work in Python now this

example be a simple implementation of the electric

kettle so let's go ahead and do that's so close the run window and I'm just gonna

delete this code and we start by creating a kettle class and its gonna model an

electric kettle

so.....and notice how its has been indented for us

automatically and we're going to create a method so....

....

....will talk about this shortly...

we just type in the code for now so...

....

...so looking at this it can be helpful to think of a class as a template from

which objects can be created so when we create objects of this kettle class they

all have a name and a price now they won't have the same name nor the same price

each instance of the class will have its own values for name and price so classes

as I said is a template from which objects can be created and all the objects

created from the same class will share the same characteristics now an instance

is just another name for an object created from a class definition so if I now create a

kettle called Kenwood then Kenwood will be an instance of the kettle class you can also

say that kenwood is an object of type kettle so I'm gonna create a couple of

kettle objects so we can see this in practice so let's continue typing and

we will go to line 8 here and type...

....

.....

.....and lets make another kettle...

...and I should really have two lines there

separating the class definition to be consistent with our code so the code on

line 9 creates an instance of the kettle class and we've given it the name

kenwood and other instances is created on line 16 and this time it's called the

Hamilton so each instance has its own values for naming and price and their access

by using . annotations so we type in Kenwood.price or Hamilton.make for

argument sake to access that information so a good analogy here is for plans for

building a house so the plan itself just describes what the house will look like

its size how many rooms it will have etc now this is similar

the plan to the class which is just a template for creating objects once you

have a plan you can then create it as many houses as you want based on that

plan and the same is true of classes once a class has been defined like how

kettle class that we define on line one we can then create as many instances of that

classes as we want now just as you can't do anything with the house plan other than

build houses based on it you can't really do anything with the class other

than create instances of it once the instances have been created you can then call

their methods and access their variables so on line 11 Kenwood.price retrieves

the price from the instance called Kenwood and Hamilton.price will get the

price of the Hamilton instance we can also give the price a new value as we see on line

13 where we set the price to $12.75 so we've been using dot notation extensively in our

programs in this course

when you seen that when we've used the append method to add items to a list for example

also all the TK widgets are objects that have .pack and grid methods amongst

many others to allow them to be placed in the window manager so lets add another

example in this program so I'm going to start typing and put on some code on line 18

gonna type...

.....

....and you can see here models kenwood equals$12.75 and Hamilton equals $14.55 so it's

retrieved the values out of each instance of the 2 kettle objects that

we've created so the parameters in the format method are the make price data attributes of

the Kenwood and Hamilton objects another bit of jargon here the

attributes so we've become used to talking about variables but when a

variable is bound to an instance of a class then it's referred to as a data

attribute in Python now their other object-oriented programming terms for

the same things you might find variable attributes also called fields in

languages such as Java or data members in C++ now I'll introduced yet another term

shortly probably in the next video one that's been borrowed from the small talk

language but lets end this video here and in then next video we'll continue our discussion about

objects see you in the next video



"""