{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0a74d764-950a-4b2b-af29-7872e514d204",
   "metadata": {
    "tags": []
   },
   "source": [
    "## 1.) Explain the key features of Python that make it a popular choice for programming."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d75a4d3-0692-4699-af5b-7acdfc2b52be",
   "metadata": {},
   "source": [
    "   Ans:\n",
    "    1.)It is very easy to learn.\n",
    "    2.)It has extensive number of libraries.\n",
    "    3.)It has various applications among different insustry like data science,Web development,data  analytics,software development,automation industry etc.\n",
    "    4.)It is used in developing backened , frontend and automation pipelines,can be connected to database, image processing can also be done using python."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a084119-873a-4344-8948-c77a655c3351",
   "metadata": {},
   "source": [
    "## 2.) Describe the role of predefined keywords in Python and provide examples of how they are used in a program?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f356ec83-c9d7-4692-b93d-b50e32c9fa52",
   "metadata": {},
   "source": [
    "Ans:\n",
    "Keywords in python are predefined reserved words which is use to carry out a specific task.\n",
    "For ex: if,else,continue,break,class,while,pass etc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0f31cecc-0dfb-47df-8064-b05807ac0fbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eligible to vote\n"
     ]
    }
   ],
   "source": [
    "#Ex-\"if\" keyword is only reserved for checking condition.\n",
    "age=18\n",
    "if (age>=18):\n",
    "    print(\"eligible to vote\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a6f74510-ec24-4496-affb-fc6f0dd921b3",
   "metadata": {},
   "source": [
    "## 3.) Compare and contrast mutable and immutable objects in Python with examples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "695fc6da-3c7f-4709-8103-3914df257bde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aalu', 'tamatar', 'oil']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Ans:\n",
    "# Mutable Objects in python are the objects which can be changed after there creation . \n",
    "# For ex- lists, dictionary etc.\n",
    "li=[\"aalu\",\"tamatar\",\"oil\"]\n",
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "44e7a154-6045-4669-89ce-3db5df0d3b25",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['aalu', 'tamatar', 'butter']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "li[2]=\"butter\"\n",
    "li"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "14199cb5-1428-46f9-b1a1-d74e2dd17da8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Ram'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Immutable Objects are the objects which cannot be changed after creation.For ex-strings,intergers ,tuples etc.\n",
    "str=\"Ram\"\n",
    "str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2f3143d7-3f97-46fd-88ae-0a1efa60dbff",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[5], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m[\u001b[49m\u001b[38;5;241;43m0\u001b[39;49m\u001b[43m]\u001b[49m\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mS\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28mstr\u001b[39m\n",
      "\u001b[0;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "str[0]=\"S\"\n",
    "str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98fbf414-897e-4925-a5f7-d7542d746017",
   "metadata": {},
   "outputs": [],
   "source": [
    "# as we can see we encounter a error."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5c9e75d-2362-4a81-9352-c0f629891508",
   "metadata": {},
   "source": [
    "## 4.) Discuss the different types of operators in Python and provide examples of how they are used?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "694ab6d2-6852-44c6-80c8-9395867a3cdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "90"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Ans:\n",
    "# There are different types of Operators used in python which are described below:\n",
    "# i)Arithmetic Operators: They are used to carry out different operations like addition,\n",
    "#  substraction,multiplication,division etc. ex- +,-,*,/,% etc.\n",
    "\n",
    "a=40\n",
    "b=50\n",
    "a+b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d1bde08b-ce27-41e9-a87d-586d6dd1680b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# ii)Comparison Operators: they are use to compare one or more than one value or object.ex->'<,>=,<=,==,!=\n",
    "a>b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "38e01215-2113-457f-85b8-f6667f3d16dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Logical Operators: they are used to combine different statement and evalute them as a single boolean expression.\n",
    "# ex- and,or,not\n",
    "a=90\n",
    "(a%2==0) and (a%3==0) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6f94f877-e385-4625-a8ed-0615585f2aac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Assignment Operators: they are used to assign a value to a variable by \n",
    "# using some operand like +,-.For ex- =,+=,-=,*= etc.\n",
    "a=5\n",
    "a*=3\n",
    "a\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "52924005-6081-4826-9057-4c56b4ef19b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#membership operators: they are used to find if a particular thing is present in data or not.\n",
    "a=\"harryPotter\"\n",
    "\"Potter\" in a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "31f36452-584d-422f-9328-d0525b0a4920",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Identity Operator- It compare memory location of two objects.\n",
    "a=8\n",
    "b=9\n",
    "a is b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0d87c96c-de52-4ee5-8f0b-8f1ff364a7ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b=8\n",
    "a is b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9e319ba5-4a2d-469a-8dd5-f1d9ea9459a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# bitwise operator- in this operator operations on done on integer \n",
    "# but converted into binary and took place bit by bit.ex-&,|,^ etc.\n",
    "10 & 10\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81f71b06-7d6b-4fd7-9869-2d5600b746ed",
   "metadata": {},
   "source": [
    "## 5.) Explain the concept of type casting in Python with examples."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "41386646-2415-4936-8ea6-b5b7cbf20500",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Typecasting is to change the datatype of a variable.It is of 2 types :\n",
    "#implicit- where automatically data type changes because size is enough.\n",
    "a=9\n",
    "b = 8.8\n",
    "sum=a+b\n",
    "sum\n",
    "type(sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "daba9f14-1747-469c-b4e1-04f6a930c36b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#explicit- here we need to change the datatype variable forcefully.\n",
    "a=8.8\n",
    "b=2\n",
    "sum=int(a)+b\n",
    "sum\n",
    "type(sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7dda1571-6afd-4d8f-aa7d-a360891e4d35",
   "metadata": {},
   "source": [
    " ## 6.)How do conditional statements work in Python? Illustrate with examples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2b6a9c23-1b6c-404c-b4ba-7aa6171906fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "go home\n"
     ]
    }
   ],
   "source": [
    "# Conditional statements in python are used to check conditions in real life.\n",
    "# there are 3 types of conditional statements in python which are described below:\n",
    "# if statement- it is used to check a single statements and returns whatever written in the body.\n",
    "weather=\"rainy\"\n",
    "if(weather==\"rainy\"):\n",
    "    print(\"go home\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "544bcda6-9fd3-4038-bb52-ed379cf8ddf3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "go and play\n"
     ]
    }
   ],
   "source": [
    "#if-else statement- it is used to check a statement \n",
    "# and go into body if true otherwise it executes the other statement of else.\n",
    "weather=\"sunny\"\n",
    "if(weather==\"rainy\"):\n",
    "    print(\"go home\")\n",
    "else:\n",
    "    print(\"go and play\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c9e9a6e0-df48-473e-8a9d-8e6719d36111",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "have some snacks , u are hungry\n"
     ]
    }
   ],
   "source": [
    "# if-elif-else statement- it is used to check multiple conditions.\n",
    "weather=\"spring\"\n",
    "if(weather==\"rainy\"):\n",
    "    print(\"go home\")\n",
    "elif(weather==\"sunny\"):\n",
    "    print(\"go and play\")\n",
    "else:\n",
    "    print(\"have some snacks , u are hungry\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1232eac7-e805-4ae3-8fdf-b99cd7260848",
   "metadata": {},
   "source": [
    "## 7.) Describe the different types of loops in Python and their use cases with examples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "086ebb71-2b86-41bb-b3a5-2a8f43a281f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loops are used in python to carry out the repetative tasks in one go,it is very time saving.\n",
    "# There are 2 types of loops in python:\n",
    "# while loop- it is a type of loop which executes until the condition gets false.\n",
    "\n",
    "i=1\n",
    "while i<=10:\n",
    "    print(i)\n",
    "    i=i+1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42d98630-3f7a-40fc-bc69-da89fc02af3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for loop - it is used to iterate over a sequence of numbers.\n",
    "for i in (0,10):\n",
    "    print i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dd996ea-f748-4d28-af48-de66753ce8a2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17278d68-aa55-4ab3-9df4-b8ad36018f93",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
