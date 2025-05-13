***********Python Chatbot Application***************

A simple and interactive chatbot application built with Python. This project combines speech recognition, text-to-speech synthesis, and a graphical user interface (GUI) for an engaging user experience.

Key Features
Voice and Text Interaction: Interact via voice commands or text input.
Text-to-Speech Output: Chatbot responds aloud using pyttsx3.
Predefined Responses: Answers common queries effectively.
Continuous Listening: Multithreading ensures seamless voice input.
User-Friendly GUI: Features a chatbot avatar, chat history, and input field.
Libraries Used
pyttsx3: For text-to-speech.
SpeechRecognition: Converts voice to text.
Tkinter: GUI development.
Pillow: Displays the chatbot avatar.
Threading: Handles continuous listening.
How It Works
Launch: Opens a Tkinter GUI with the chatbot avatar.
Input: Accepts voice or text queries.
Response: Matches queries with predefined responses.
Output: Displays response in chat and speaks it aloud.
Extensibility
Enhance this project by:

Adding real-time APIs (e.g., weather, news).
Implementing NLP for smarter conversations.
Personalizing user interactions.
Prerequisites
Python 3.6+
Install dependencies:
bash

pip install pyttsx3 speechrecognition pillow
Usage
Clone the repository:
bash



git clone https://github.com/sahazadalam/ChatBot_Using_Python.git
cd python-chatbot
Add the chatbot avatar image (bot3.png) to the directory.
Run the chatbot:
bash









PART B
1.	Write a program to implement Kruskal’s minimum cost spanning tree using Greedy Method

public class Kruskal {

    static int[] parent;

    static int find(int i) {
        while (parent[i] != i)
            i = parent[i];
        return i;
    }

    static void union(int i, int j) {
        int a = find(i);
        int b = find(j);
        parent[a] = b;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int V = sc.nextInt();

        System.out.print("Enter number of edges: ");
        int E = sc.nextInt();

        int[][] edges = new int[E][3];

        System.out.println("Enter each edge as: src dest weight");
        for (int i = 0; i < E; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Arrays.sort(edges, Comparator.comparingInt(a -> a[2]));

        parent = new int[V];
        for (int i = 0; i < V; i++)
            parent[i] = i;

        int totalCost = 0;
        System.out.println("Edges in the MST:");

        for (int i = 0; i < E; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];

            if (find(u) != find(v)) {
                union(u, v);
                totalCost += w;
                System.out.println(u + " - " + v + " : " + w);
            }
        }

        System.out.println("Total cost of MST: " + totalCost);
        sc.close();
    }
}

OUTPUT:
Enter number of vertices: 4
Enter number of edges: 5
Enter each edge as: src dest weight
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
Edges in the MST:
2 - 3 : 4
0 - 3 : 5
0 - 1 : 10
Total cost of MST: 19











print('MENU DRIVEN PROGRAM')
print('1. Find the Perfect number or not')
print('2. Find the Armstrong number or not')
print('3. Find the Palindrome number or not')
print('4. Exit')

while True:
    print('\n*******************************')
    Choice = int(input('\nEnter a Choice: '))

    if Choice == 1:
        print('\nPERFECT NUMBER OR NOT')
        num = int(input('Enter a number: '))
        Sum = 0
        for i in range(1, num):
            if num % i == 0:
                Sum += i
        if Sum == num:
            print(num, 'is a Perfect Number.')
        else:
            print(num, 'is not a Perfect Number.')

    elif Choice == 2:
        print('\nARMSTRONG NUMBER OR NOT')
        num = int(input("Enter a number: "))
        Sum = 0
        temp = num
        n = len(str(num))
        while temp > 0:
            digit = temp % 10
            Sum += digit ** n
            temp //= 10
        if num == Sum:
            print(num, "is an Armstrong number.")
        else:
            print(num, "is not an Armstrong number.")

    elif Choice == 3:
        print('\nPALINDROME NUMBER OR NOT')
        num = int(input('Enter a number: '))
        temp = num
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num = num // 10
        print('Reverse of', temp, 'is', rev)
        if temp == rev:
            print('So, Entered Number is Palindrome.')
        else:
            print('So, Entered Number is not Palindrome.')

    elif Choice == 4:
        print("Exited")
        break

    else:
        print('Invalid Choice!')





file = open("data1.txt", 'x')
file.write("hello!")
file.close()

file = open("data1.txt", "r")
print(file.read())
file.close()

file = open("data1.txt", "r")
data = file.read()
print("Number of characters in a file: {}".format(len(data)))
file.close()

file = open("data1.txt", "r")
data = file.read()
words = data.split()
print("Number of words in a file: {}".format(len(words)))
file.close()

file = open("data1.txt", "r")
data = file.readlines()
print("Number of lines in a file: {}".format(len(data)))
file.close()

print("\nAfter appending: ")
file = open("data1.txt", "a")
file.writelines("\npython programming\nperl programming\nweb programming")
file.close()

file = open("data1.txt", "r")
print(file.read())
file.close()

file = open("data1.txt", "r")
data = file.read()
print("Number of characters in a file: {}".format(len(data)))
file.close()

file = open("data1.txt", "r")
data = file.read()
words = data.split()
print("Number of words in a file: {}".format(len(words)))
file.close()

file = open("data1.txt", "r")
data = file.readlines()
print("Number of lines in a file: {}".format(len(data)))
file.close()










REVA
UNIVERSITY
Python Programming Lab (B23DA0405)
Demonstrate the usage of math and cmath module to find the roots of a
1
Quadratic Equation)
import math
import cmath
a=float (input ("Enter the value of a"))
b=float (input ("Enter the value of b"))
c=float (input ("Enter the value of e"))
d= (b**2) - (4*a*c)
i f d==0:
print("the rots are equal and real")
root1=(-btmath. sqrt (d) ) / (2*a)
root2=(-b-math. sqrt (d) ) / (2*a)
print ("root1=", root1)
print ("root2=", root2)
e l i f d>0:
print("the roots a r e distinct and real")
root1=(-btmath. sqrt (d) ) / (2*a)
root2=(-b-math. sqrt (d) ) / (2*a)
print ("root1=", root1)
print ("root2=", root2)
else:
print ("the roots are imaginary and real")
root1=(-btcmath. sgrt (d)) / (2*a)
root2=(-b-cmath. sgrt (d)) / (2*a)
print("root1=", root1)
print ("root2=", root2)
PROF. NAGARAJU S, CSA 1
R E VA
UNIVERSITY
Python Programming Lab (B23DA0405)
OUTPUT 1
E n t e r t h e v a l u e o f a 1
E n t e r t h e v a l u e o f b 2
E n t e r t h e v a l u e o f c 1
t h e r o o t s a r e e q u a l a n d r e a l
r o o t 1 = - 1 . 0
r o o t 2 = - 1 . 0
OUTPUT 2
E n t e r t h e v a l u e o f a 1
E n t e r t h e v a l u e o f b 7
E n t e r t h e v a l u e o f c 1 2
t h e r o o t s a r e d i s t i n c t a n d r e a l
r o o t 1 = - 3 . 0
r o o t 2 = - 4 . 0
OUTPUT 3
E n t e r t h e v a l u e o f a 1
E n t e r t h e v a l u e o f b 1
E n t e r t h e v a l u e o f c 1
t h e r o o t s a r e i m a g i n a r y a n d r e a l
O 0 t 1 = （ - 0 . 5 + 0 . 8 6 6 0 2 5 4 0 3 7 8 4 4 3 8 6 コ ）
0 0 t 2 = （ - 0 . 5 - 0 . 8 6 6 0 2 5 4 0 3 7 8 4 4 3 8 6 コ ）
PROF. NAGARAJU S, CSA 2





python chatbot.py
Example Queries
"Hello"
"What is your name?"
"Tell me a joke"
"How are you?"

Acknowledgements
Developed by Sahazad Alam Ansiri
