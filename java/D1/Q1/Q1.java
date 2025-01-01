// Array Manipulation: Write a program to find the largest and smallest elements in an array.

import java.util.Scanner;

public class Q1 {
    public static void main(String[] args) {
        int Arra[] = { 12, 3, 45, 77, 1, 23 };
        int largestIndex = 0;
        int smallestIndex = Arra[0];
        for (int i = 0; i < Arra.length; i++) {
            if (Arra[i] > largestIndex) {
                largestIndex = Arra[i];
            }
        }
        for (int i = 0; i < Arra.length; i++) {
            if (Arra[i] < smallestIndex) {
                smallestIndex = Arra[i];
            }
        }
        System.out.println(largestIndex);
        System.out.println(smallestIndex);
    }

}
