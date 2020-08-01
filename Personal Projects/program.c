
#include <stdio.h>
#include <stdlib.h>

// This is a C program

main()
{
    char name[15] = "steve";
    int age = 25;
    printf("hello %s, you are %d years old!", name, age);
    int count = 0;

    do {
        printf(" \n\nYAY!\n");
        count++;
    }
    while (count < 5);

    if (count >= 5) {
        count = 0;
    }

    printf(" %d", count);

    while (count < 3) {
        printf("\nC is fun!\n");
        count++;
    }

//    char input[20];
//    for (int x=1; x<=5; ++x) {
//        printf("\n\nWhat is your favorite color: ");
//        scanf("%s", &input);
//    }
    system("echo \"Hello I am your command line\"");
    system("mkdir C:\\me\\");
    system("dir C:\\");
    system("cmd.exe");
}
