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


python chatbot.py
Example Queries
"Hello"
"What is your name?"
"Tell me a joke"
"How are you?"

Acknowledgements
Developed by Sahazad Alam Ansiri
